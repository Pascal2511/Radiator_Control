#!/bin/bash

echo "Welcome to the Install-assistant!"

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential python-dev python-openssl git
sudo pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
sudo apt-get install python3-pip
chmod +x DHT_22.py
echo "Installation complete! Thanks for waiting"
sudo python DHT_22.py
