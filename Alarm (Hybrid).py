import ntplib
from time import ctime
from time import sleep
from playsound import playsound
x, y, z = input('Hour : '), input('Min : '), input('Sec : ')
c = ntplib.NTPClient()
response = c.request('pool.ntp.org')
receive = ctime(response.tx_time)
h, m, s = receive[11:13], receive[14:16], receive[17:19]
while True:
    h, m, s = int(h), int(m), int(s)
    s += 1
    if s > 59:
        s = 0
        m += 1
    if m > 59:
        m = 0
        h += 1
    if h > 23:
        h = 0
    if s < 10:
        s = '0' + str(s)
    if m < 10:
        m = '0' + str(m)
    if h < 10:
        h = '0' + str(h)
    if [str(h), str(m), str(s)] == [x, y, z]:
        break
    sleep(1)
while True:
    playsound('<example>.wav')   # Edit this line.
