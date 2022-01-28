import ntplib
from time import ctime
from playsound import playsound

h = input('Hour : ')
m = input('Min : ')
s = input('Sec : ')

c = ntplib.NTPClient()

while True:

    response = c.request('pool.ntp.org')
    receive = ctime(response.tx_time)
    hour, minute, second = receive[11:13], receive[14:16], receive[17:19]
    #print(hour, minute, second)
    if [hour, minute, second] == [h, m, s]:
        break  
while True:
    playsound('Kalki.wav')


