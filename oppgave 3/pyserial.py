import serial 
import time 
from datetime import datetime 

ser = serial.Serial(
'COM4', 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=1
)
while True:
    ts = time.gmtime()

    try:
        s = str(ser.readline(100).decode())
       
        if s !="":
          f = open("Adgangslogg.txt", "a+")
          f.write(time.strftime("%m, %d, %H: %M: %S", ts )) 
          f.write("\n")
          f.write(s)
          f.close()

    except:
        print('ERROR')
        break
   
    time.sleep(1)