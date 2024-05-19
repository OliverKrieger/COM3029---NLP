import time
import matplotlib.pyplot as plt
import os

from utils.paths import static_figs_performance_path
from entity_recogniser.recogniser import run_model

def time_to_requests(time_in_seconds, model_type, input, graph_name:str="time_to_requests"):
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
    ax.set_title(f"Make Requests for {time_in_seconds} {model_type}")
    plt.xlabel("Number of Requests")
    plt.ylabel("Time")
    fig_path = os.path.join(static_figs_performance_path, (graph_name+'.png'))
    plt.savefig(fig_path)
    return "./static/figs/performance/"+(graph_name+".png")
    
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
    ax.set_title(f"{nor} Requests over Time {model_type}")
    plt.xlabel("Number of Requests")
    plt.ylabel("Time")
    fig_path = os.path.join(static_figs_performance_path, (graph_name+'.png'))
    plt.savefig(fig_path)
    return "./static/figs/performance/"+(graph_name+".png")

def evaluate_model_performance(model_type:str, input:str, time_for_requests:int, n_of_requests:int):
    imgs:list[tuple[str, str]] = []
    imgs.append(("time request", time_to_requests(int(time_for_requests), str(model_type), str(input), "time_for_requests")))
    imgs.append(("time request", request_over_time(int(n_of_requests), str(model_type), str(input), "time_for_requests")))
    return imgs