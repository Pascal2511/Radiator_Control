import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

# Initial the dht device, with data pin connected to:
# dhtDevice = adafruit_dht.DHT22(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# change to adafruit_dht.DHT22 if used
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

min_temp = 15
max_temp = 20
heater   = 17


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
            elif temperature_c > max_temp:
                GPIO.output(heater, GPIO.LOW)

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
        
    time.sleep(2)
