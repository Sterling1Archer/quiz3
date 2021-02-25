from guizero import App, Slider, TextBox
from threading import Thread
from gpiozero import LEDBoard, Button
from time import sleep
import RPi.GPIO as GPIO

led_NS = LEDBoard(21,20,16)
led_EW = LEDBoard(19,13,6)
led_blue = LEDBoard(26)

def blue_light(self):
    blue_light_trigger = 1
    print("blue_light = ", blue_light_trigger)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(5, GPIO.RISING, callback=blue_light, bouncetime=100)
    
if __name__ == '__main__':
    led_array_NS = [[1,0,0],
                    [0,1,0],
                    [0,0,1]]
    led_array_EW = [[0,0,1],
                    [1,0,0],
                    [0,1,0],
                    [0,0,1]]
    sleep_green = 3
    sleep_orange = 1
    sleep_red = 1
    sleep_blue = 1
    i = 0
    j = 0
    global blue_light_trigger
    #blue_light_trigger = 0
    led_EW[2].on()
    while True:
        for j in range(len(led_array_NS)):#For North-South
            for i in range(len(led_array_NS[i])):
                if led_array_NS[j][i]==1:
                    led_NS[i].on()
                elif led_array_NS[j][i]==0:
                    led_NS[i].off()
            sleep(1)
            #print("blue_light_trigger: ",blue_light_trigger)
            
        if blue_light_trigger == 1:
            print("executed")
            led_blue[1].on()
            sleep(sleep_blue)
            led_blue[1].off()
            
        for j in range(len(led_array_EW)):
            for i in range(len(led_array_EW[i])):#For East-West
                if led_array_EW[j][i]==1:
                    led_EW[i].on()
                elif led_array_EW[j][i]==0:
                    led_EW[i].off()
            sleep(1)
    
    led_NS.off()
    led_EW.off() 
    led_blue.off()
