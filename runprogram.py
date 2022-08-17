import time as tmes
from datetime import datetime as dt

eins = "ein"

while eins == "ein":
    time = dt.now()
    minutes = time.minute
    hours = time.hour
    seconds = time.second
    day = time.weekday()

    if minutes == 26:
        exec(open('script.py').read())