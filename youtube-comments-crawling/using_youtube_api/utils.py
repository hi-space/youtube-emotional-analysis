import os
import datetime
from config import LOG_FILE


def get_now():
    return datetime.datetime.now()

def log(data):
    now = str(get_now())
    log_message = "[" + now + "] " + data
    
    print(log_message)
    with open(LOG_FILE, "a") as f:
        f.write(log_message + "\n")

def file_list_in_directory(path, extension='.csv'):
    file_list = os.listdir(path)
    csv_file_list = [file for file in file_list if file.endswith(extension)]
    return csv_file_list