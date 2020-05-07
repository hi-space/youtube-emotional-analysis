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
