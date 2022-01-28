from datetime import datetime
from playsound import playsound
from time import sleep
h = input('Hour : ')
m = input('Min : ')
s = input('Sec : ')
while True:
    c = str(datetime.now())
    year, month, date, hour, minute, second = c[0:4], c[5:7], c[8:10], c[11:13], c[14:16], c[17:19]
    
    if [hour, minute, second] == [h, m, s]:
        break
    sleep(0.99)
while True:
    playsound('<example>.wav')   # Edit this line.
