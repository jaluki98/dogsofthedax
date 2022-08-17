import os
import time as tmes
from datetime import datetime as dt

os.system("gnome-terminal -e 'bash -c \"python3 script.py\" '")

while 1 == 1:
    time = dt.now()
    minutes = time.minute
    hours = time.hour
    seconds = time.second
    day = time.weekday()

    if minutes == 35 and hours == 14:
        os.system("gnome-terminal -e 'bash -c \"python3 script.py\" '")

    print('Läuft frei. Uhrzeit: ', minutes, ' Minuten - ', hours, 'Stunden - ', day, 'Tag')
    tmes.sleep(60)