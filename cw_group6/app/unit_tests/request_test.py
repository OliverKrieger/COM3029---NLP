import time
import matplotlib.pyplot as plt
import os

from utils.paths import unit_test_path
from entity_recogniser.recogniser import run_model

def make_requests(time_in_seconds, model_type, input, graph_name:str="make_requests_fig"):
    start_time = time.time()
    number_of_requests = 0
    request_times = []
    while(time.time() - start_time < time_in_seconds):
        run_model(model_type, input)
        request_times.append([number_of_requests, (time.time()-start_time)])
        number_of_requests += 1
    print(f"MR - number of requests made {number_of_requests} over time {time_in_seconds}s for model {model_type}")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot([rt[0] for rt in request_times], [rt[1] for rt in request_times])
    plt.savefig(os.path.join(unit_test_path, "figs", (graph_name+'.png')))
    
def request_over_time(nor, model_type, input, graph_name:str="requests_over_time"):
    start_time = time.time()
    number_of_requests = 0
    request_times = []
    for i in range(nor):
        run_model(model_type, input)
        request_times.append([number_of_requests, (time.time()-start_time)])
        number_of_requests += 1
    print(f"ROT - number of requests made {number_of_requests} over time {time.time()-start_time}s for model {model_type}")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot([rt[0] for rt in request_times], [rt[1] for rt in request_times])
    plt.savefig(os.path.join(unit_test_path, "figs", (graph_name+'.png')))
    