from gpiozero import LineSensor
from signal import pause
import datetime
import pigpio


pi = pigpio.pi()
total_revolutions = 0
time1 = None
time2 = None

#function to connect to break sensor and run when test has completed


def total():
    global total_revolutions
    print("Total Revolutions: ", total_revolutions)


def test():
    global time1
    global time2
    global total_revolutions
    total_revolutions+=1
    if(time1 is None):
        time1 = pi.get_current_tick() 
    else:
        if(time2 is None):
            time2 = pi.get_current_tick()
    if(time1 != None and time2 != None):
        rev_time = (time2 - time1)
        RPM = 60000/(rev_time/1000)
        print("RPM = ",RPM)
        time1 = None
        time2 = None
        
#assign sensor variable to correct pin


sensor = LineSensor(4)


#run until break sensor signal is implemented
#runs test() and total() once each, on change in sensor status during a full revolution

sensor.when_line = lambda: total() 
sensor.when_no_line= lambda:test() 
pause()


