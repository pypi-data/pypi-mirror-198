from time import time
import numpy as np
from getpass import getuser
from glob import glob
from keras.models import Model, load_model
from typing import Dict, TypedDict, List
import json
from io import BytesIO
from os import stat, environ, path
import iperf3
from pythonping import ping
from getpass import getuser
import tensorflow as tf
import psutil
import gc
from multiprocessing import Pool
import contextlib
import uuid
from pympler.asizeof import asizeof

class Config(TypedDict):
    model_test_number_of_repeats: int
    model_test_batch_size: int
    bandwidth_test_duration_sec: int
    latency_test_count: int
    free_memory_multiplier:float

config: Config

INPUT_MULTIPLIER = 10
# def load_benchmark_configs()->Config:
#     # TODO: read from environment variables
#     global config
#     config = Config(
#         model_test_batch_size=100,
#         model_test_number_of_repeats=100,
#         bandwidth_test_duration_sec=1,
#         latency_test_count=1000,
#         free_memory_multiplier = 0.5)

def load_benchmark_configs()->Config:
    global config
    config = Config(
        model_test_batch_size=int(environ.get("MODEL_TEST_BATCH_SIZE")),
        model_test_number_of_repeats=int(environ.get("MODEL_TEST_NUMBER_OF_REPEATS")),
        bandwidth_test_duration_sec=int(environ.get("BANDWIDTH_TEST_DURATION_SEC")),
        latency_test_count=int(environ.get("LATENCY_TEST_COUNT")),
        free_memory_multiplier=float(environ.get("FREE_MEMORY_MULTIPLIER"))
    )
    

def isDebug()->bool:
    return int(environ.get("DEBUG")) == 1



def get_available_memory():
    return psutil.virtual_memory().free

# https://gist.github.com/jamesmishra/34bac09176bc07b1f0c33886e4b19dc7
def memory_usage(model, *, batch_size: int):
    default_dtype = tf.keras.backend.floatx()
    shapes_mem_count = 0
    internal_model_mem_count = 0
    for layer in model.layers:
        if isinstance(layer, tf.keras.Model):
            internal_model_mem_count += memory_usage(
                layer, batch_size=batch_size
            )
        single_layer_mem = tf.as_dtype(layer.dtype or default_dtype).size
        out_shape = layer.output_shape
        if isinstance(out_shape, list):
            out_shape = out_shape[0]
        for s in out_shape:
            if s is None:
                continue
            single_layer_mem *= s
        shapes_mem_count += single_layer_mem

    trainable_count = sum(
        [tf.keras.backend.count_params(p) for p in model.trainable_weights]
    )
    non_trainable_count = sum(
        [tf.keras.backend.count_params(p) for p in model.non_trainable_weights]
    )

    total_memory = (
        batch_size * shapes_mem_count * INPUT_MULTIPLIER
        + internal_model_mem_count
        # + trainable_count
        # + non_trainable_count
    )
    return total_memory

def load_network_benchmark_ips() -> List[str]:
    target_networks = environ.get("PAPDL_WORKERS").split(" ")
    print(target_networks,flush=True)
    return target_networks

def get_available_memory():
    return psutil.virtual_memory().free


user_folder = glob(f"/home/*/")[0]
model_paths = glob(f"{user_folder}models/*/")
papdl_workers = load_network_benchmark_ips()

def benchmark_network(papdl_workers:List[str]) -> Dict:
    global config
    result = {}
    for ip in papdl_workers:

        # BANDWIDTH TEST
        client = iperf3.Client()
        client.duration = config["bandwidth_test_duration_sec"]
        client.server_hostname = ip
        client.port = 5201
        r_iperf: iperf3.TestResult = client.run()
        r_ping = ping(ip, count=config["latency_test_count"])

        result[ip] = {
            "bandwidth": {
                "sent_bps": r_iperf.sent_bps,
                "received_bps": r_iperf.received_bps
            },
            "latency": {
                "rtt_min_ms": r_ping.rtt_min_ms,
                "rtt_avg_ms": r_ping.rtt_avg_ms,
                "rtt_max_ms": r_ping.rtt_max_ms
            }
        }
        print(result[ip],flush=True)
        del client
    return result

def single_model_benchmark(args:Dict):
    mp = args["mp"]
    fmm = args["fmm"]
    mtbs = args["mtbs"]
    

    free_memory = get_available_memory()
    model:tf.keras.Model = load_model(mp)
    model_memory_usage = memory_usage(model=model,batch_size=config["model_test_batch_size"])
    model_name = model.name
    dimensions = (mtbs,) + model.input_shape[1:]
    print(f"Loaded model : {model_name} from path: {mp} with input_dims: {dimensions}",flush=True)
    
    if(model_memory_usage > free_memory * fmm):
        print(f"Skipping benchmarking as memory threshold {model_memory_usage} has been met {free_memory}.",flush=True)
        result = {}
        result["benchmark_size"] = float("inf")
        result["benchmark_time"] = float("inf")
        result["benchmark_memory_usage"] = model_memory_usage
        result["model_name"] = model_name
        del model
        tf.compat.v1.reset_default_graph()
        gc.collect()
        return result

    print(f"Running benchmarking as memory threshold {free_memory} has not been met for model {model_memory_usage}")
    sample_input = np.random.random_sample(dimensions)
    start = time()
    for i in range(mtbs):
        tmp_out = model(sample_input,training=False)
        del tmp_out
        gc.collect()
    end = time()
    
    output:np.array = model(sample_input,training = False)
    # file_name = f"fsize_{str(uuid.uuid4())}"
    # np.save(file_name,"output")
    
    # size = stat(f"{file_name}.npy").st_size
    size = asizeof(output)
    result = {}
    result["benchmark_size"] = size
    result["benchmark_time"] = (end - start) / mtbs
    result["benchmark_memory_usage"] = model_memory_usage
    result["model_name"] = model_name

    del model
    del output
    del sample_input
    tf.compat.v1.reset_default_graph()
    return result
    


def benchmark_models(model_paths=model_paths):
    global config
    result = {}
    with contextlib.closing(Pool(1)) as po:
        pool_args = []
        for mp in model_paths:
            pool_args.append({"mp":mp, "fmm":config["free_memory_multiplier"], "mtbs": config["model_test_batch_size"]})

        pool_result = po.map_async(single_model_benchmark, pool_args)
        completed_pool_results = pool_result.get()
        for r in completed_pool_results:
            result[r["model_name"]] = {}
            result[r["model_name"]]["benchmark_size"] = r["benchmark_size"]
            result[r["model_name"]]["benchmark_time"] = r["benchmark_time"]
            result[r["model_name"]]["benchmark_memory_usage"] = r["benchmark_memory_usage"]
    return result
        

load_benchmark_configs()
print(f"Loaded config: {config}",flush=True)
benchmark_result = {"free_memory": get_available_memory()}
benchmark_result["network_performance"] = benchmark_network(papdl_workers=papdl_workers)
benchmark_result["model_performance"] = benchmark_models(model_paths=model_paths)

def convert_np(o):
    if isinstance(o, np.int64): return int(o)  
    raise TypeError
print("[BENCHMARK]" + json.dumps(benchmark_result,default=convert_np),flush=True)