import time
import RPi.GPIO as GPIO

heater_pin = 17
min_delay = 0.05
max_delay = 0.15
delay_step = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setup(heater_pin, GPIO.OUT)

delay = max_delay

while True:
    # Turn heater on
    GPIO.output(heater_pin, GPIO.HIGH)
    time.sleep(delay)

    # Turn heater off
    GPIO.output(heater_pin, GPIO.LOW)
    time.sleep(delay)

    # Decrease delay time
    delay -= delay_step
    delay = max(delay, min_delay)

    if delay <= min_delay:
        break

GPIO.cleanup()
