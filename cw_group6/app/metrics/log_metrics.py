import os
from datetime import datetime

from utils.paths import logs_path

def test_log_file(fpath) -> bool:
    return os.path.exists(fpath)
        
def log_metric(info:dict):
    logfile_path = os.path.join(logs_path, "log_file.log")
    info["time"] = str(datetime.now())
    with open(logfile_path, "a+") as f:
        log_line = str(info)+"\n"
        f.write(log_line)
        f.close()

def get_log_metrics() -> list[tuple]:
    logs = []
    logfile_path = os.path.join(logs_path, "log_file.log")
    f = open(logfile_path, 'r')
    lines = f.readlines()
    for line in lines:
        line_dict = eval(line)
        logs.append((line_dict["input"], line_dict["prediction"], line_dict["model_type"], line_dict["time"]))
    return logs
