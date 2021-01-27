# Hedgeometer
## A device to track our hedgehog's running distance.
### With Twilio, the Hedgometer texts us every morning with a report on how much Hedgie ran in the night. This helps us keep track of his overall health and wellbeing.

## Twilio Programmable SMS API
### https://www.twilio.com/docs/sms/api/message-resource?code-sample=code-create-a-message&code-language=Python&code-sdk-version=6.x

![Create message with Twilio](https://github.com/mugelstad/hedgeometer/blob/main/readme-content/create-message.jpg?raw=true)

## Raspberry Pi B+
### https://www.raspberrypi.org/documentation/usage/gpio/
![Raspberry Pi B+ Pinout](https://github.com/mugelstad/hedgeometer/blob/main/readme-content/raspberryPi-pinout.jpg?raw=true)


## Adafruit Magnetometer MLX-90393
### https://learn.adafruit.com/mlx90393-wide-range-3-axis-magnetometer?view=all
![Raspberry Pi plus Magnetometer Wiring](https://github.com/mugelstad/hedgeometer/blob/main/readme-content/python-wiring.jpg?raw=true)

## Setup
### Hardware
#### Follow Adafruit's Guide: https://learn.adafruit.com/mlx90393-wide-range-3-axis-magnetometer/circuitpython

### Enable I2C Interface
```
sudo raspi-config
```
#### Select "Interfacing Options", then "I2C", "Yes", and "Finish"
```
reboot
```
### Enable Hardware Interfaces
```
sudo nano /boot/config.txt
```
#### Uncomment ```dtparam=i2c_arm=on``` and ```dtparam=i2c1=on```

### Run the following commands to install the necessary libraries.
### Create a Virtual Environment
```
python3 -m venv .env
source .env/bin/activate
```

### Twilio Client
```
pip3 install twilio
```
### Time
```
pip3 install datetime
pip3 install pytz
```
### CircuitPython by Adafruit
```
pip3 install adafruit-blinka
```
### Magnetometer
```
pip3 install adafruit-circuitpython-mlx90393
```
## Running the Application
```
python3 magnet.py
```
### Environment Variables
#### Replace the information in ```filename``` with your private information.

![Hedgometer Setup](https://github.com/mugelstad/hedgeometer/blob/main/readme-content/setup.jpg?raw=true)

## Optional setup
### Use a Twilio SIM card for connectivity instead of WiFi. Connect the LTE Pi Hat and antennas to the Raspberry Pi and insert the SIM card.
### Similar setup to Twilio's Developer Kit: https://www.twilio.com/docs/iot/wireless/get-started-twilio-developer-kit-broadband-iot#the-hardware
### Order Twilio SIM cards in Console here: https://www.twilio.com/console/iot/orders/new
