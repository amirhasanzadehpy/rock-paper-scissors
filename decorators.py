from datetime import datetime
from datetime import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hours = duration.seconds // 3600
        minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        print(
            f"⏰ Elapsed time: {hours}h {minutes}m {seconds}s"
        )
        return result
    return wrapper
