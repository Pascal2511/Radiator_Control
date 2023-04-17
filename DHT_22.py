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
pi@raspberrypi:~/Temp-Control $ cat DHT_22.py
import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

dhtDevice = adafruit_dht.DHT11(board.D4)

min_temp = 10
max_temp = 25
heater   = 17
delay    = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(heater, GPIO.OUT)
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if temperature_c is not None:
            if temperature_c <= min_temp:
                GPIO.output(heater, GPIO.HIGH)
            elif temperature_c >= max_temp:
                GPIO.output(heater, GPIO.LOW)
            else:
                print("Perfect Temperature")
        print(GPIO.input(heater))
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(delay)
