from datetime import datetime


def get_current_time():
    """
    is used in an app.py.
    returns current time
    """
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")
