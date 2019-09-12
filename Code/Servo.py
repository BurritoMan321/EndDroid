import RPi.GPIO as gpio
import time

servoPIN = 22
gpio.setmode(gpio.BOARD)
gpio.setup(servoPIN, gpio.OUT)

p = gpio.PWM(servoPIN, 50) # gpio 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
    x = input()
    for s in range(0,1):
        if(x == "h"):
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(10)
            time.sleep(0.5)
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
        else:
            print("Choose h!")
except KeyboardInterrupt:
  p.stop()
  gpio.cleanup()
