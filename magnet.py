# raspberry pi imports
import busio
import board

# environment variables setup
import os

# raspberry pi setup
I2C_BUS = busio.I2C(board.SCL, board.SDA)

# magnetometer import
import adafruit_mlx90393

# magnetometer setup
SENSOR = adafruit_mlx90393.MLX90393(I2C_BUS, gain=adafruit_mlx90393.GAIN_1X)

# time imports
import time
from datetime import datetime
import pytz

# time setup
zoneName = os.environ['TIMEZONE']
timezone = pytz.timezone(zoneName)
currentTime = datetime.now(tz=timezone)

# twilio imports
from twilio.rest import Client

# twilio setup
accountSid = os.environ['TWILIO_ACCOUNT_SID']
authToken = os.environ['TWILIO_AUTH_TOKEN']
twilioPhone = os.environ['TWILIO_PHONE_NUMBER']
recipient01 = os.environ['RECIPIENT_01']
recipient02 = os.environ['RECIPIENT_02']

# laps setup
magnet = False
laps = 0
distance = 0

# when running this script
while True:
    # set up x, y, z axes for the sensor
    MX, MY, MZ = SENSOR.magnetic
    
    # check for significant changes in axis z
    if (MZ < -500 or MZ > 500):
        print("MAGNET SENSED", MX, "  Y", MY,"  Z", MZ)
        # the magnet is near
        magnet = True
    else:
        print(MX," ",MY,"  ",MZ)
        # the magnet is far
        if magnet == True:
            magnet = False
            laps = laps + 1
   
   # update recipients every morning at 9am local time
    if currentTime.isoformat()[11:19] == "09:00:00":
        # hedgehog wheel circumference is 37 inches
        distance = (laps*37)/63360
        print (distance, " miles have been run")
        
        # text recipients the miles ran
        if (distance > 3):
            message = client.messages.create(
                body='Good Morning! Hedgie ran ' + str(distance) + ' miles last night. What a good boy.',
                from_=twilioPhone,
                to=recipient01
            )
            message = client.messages.create(
                body='Good Morning! Heggie ran ' + str(distance) + ' miles last night. What a good boy.',
                from_=twilioPhone,
                to=recipient02
            )
            
        else:
            message = client.messages.create(
                body='Hedgie ran ' + str(distance) + ' miles last night. We should check on him.',
                from_=twilioPhone,
                to=recipient01
            )
            message = client.messages.create(
                body='Alert! Alert! Heggie ran ' + str(distance) + ' miles last night. Alert!',
                from_=twilioPhone,
                to=recipient02
            )
        # reset laps and distance each morning after sending the text
        laps = 0
        distance = 0
    
    # sensor status displayed when script is stopped
    if SENSOR.last_status > adafruit_mlx90393.STATUS_OK:
        SENSOR.display_status()
    
    # check for magnet every quarter second
    time.sleep(0.25)
    
    