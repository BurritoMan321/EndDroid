import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def backward():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)

    
def forward():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)

def left():
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)


def right():
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    
    
    

def stop():
    gpio.cleanup()    
    
    
    
    
def menu():
    text()
    while(1):
        x = input()
    
        if(x == 'f'):
            print("forward")
            forward()
        elif(x == 'b'):
            print("backward")
            backward()
        elif(x == 'l'):
            print("left")
            left()
        elif(x == 'r'):
            print("right")
            right()
        elif(x == 's'):
            print("stop")
            stop()
        elif(x == 'e'):
            print("exit")
            break;
        else:
            print("Please choose between f-forward, b-backward, l-left, r-right, s-stop or e-exit")
            
def text():
    print("Choses: f-forward, b-backward, l-left, r-right, s-stop or e-exit")
menu()