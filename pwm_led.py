from machine import Pin, PWM
import utime

#the pin is GPIO 0 (GP0)
pwm = PWM(Pin(0))

#frequency. If you slow this down to around 40,
#you can see it blinking really fast.
pwm.freq(120)

#brightness of LED. 0 - 65025
dutycycle = 65025

#run loop
while True:
    #this for loop will count up from 0 to 65025
    for duty in range(dutycycle):
        pwm.duty_u16(duty)
        #this is the delay in between counting
        utime.sleep(.0001)
    #this for loop will count down from 65025 to 0
    for duty in range(dutycycle, 0, -1):
        pwm.duty_u16(duty)
        #this is the delay in between counting
        utime.sleep(.0001)