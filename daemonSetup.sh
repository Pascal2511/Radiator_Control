#!/bin/bash

echo "Welcome to the daemon-setup!"
echo "Creating a linux daemon!"
sudo cp radiator.service /etc/systemd/system/
sudo cp DHT_22.py /opt/
echo "Enable the linux daemon by typing:"
sudo systemctl daemon-reload
sudo systemctl enable radiator.service
sudo systemctl start radiator.service
echo "Checking the status of the service:"
sudo systemctl status radiator.service
