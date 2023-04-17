import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
dhtDevice = adafruit_dht.DHT11(board.D4)

min_temp = 10
max_temp = 25
heater   = 17
delay    = 0.5

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(heater, GPIO.OUT)

GPIO.output(heater, True)
time.sleep(1)
GPIO.output(heater, False)

GPIO.cleanup()
