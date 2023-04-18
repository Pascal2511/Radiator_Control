#!/bin/bash

echo "Welcome to the Install-assistant!"

sudo apt-get update
sudo apt-get upgrade

sudo apt-get install build-essential python-dev python-openssl git
sudo pip3 install adafruit-circuitpython-dht
sudo apt-get install libgpiod2
sudo apt-get install python3-pip
chmod +x DHT_22.py
echo "Creating a linux daemon!"
sudo cp radiator.service /etc/systemd/system/
sudo cp DHT_22.py /opt/
echo "Enable the linux daemon by typing:"
sudo systemctl daemon-reload
sudo systemctl enable radiator.service
echo "Checking the status of the service:"
sudo systemctl status radiator.service
echo "Thanks for waiting"
