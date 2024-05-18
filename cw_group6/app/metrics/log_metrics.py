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