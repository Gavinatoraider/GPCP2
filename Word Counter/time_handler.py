# time_handler.py
from datetime import datetime

def get_current_timestamp():
    """Returns the current timestamp formatted as YYYY-MM-DD HH:MM:SS."""
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")
