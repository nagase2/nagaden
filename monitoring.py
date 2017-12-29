# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# HDC1000
# This code is designed to work with the HDC1000_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Temperature?sku=HDC1000_I2CS#tabs-0-product_tabset-2
print('program start !')
import smbus
import time
import RPi.GPIO as GPIO
import os
import logging
from logging.handlers import RotatingFileHandler
from logging import getLogger, StreamHandler, FileHandler,INFO,DEBUG


#logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s %(message)s')
#filename='/tmp/nagase.log',filemode='w', level=logging.INFO)
formatter= logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s')

logger = logging.getLogger(__name__)

fileHandler = RotatingFileHandler('/home/pi/Desktop/nagase-denki/log/monitoring.log',maxBytes=10000,backupCount=5)
fileHandler.setLevel(DEBUG)
fileHandler.setFormatter(formatter)
streamHandler = StreamHandler()
streamHandler.setLevel(DEBUG)
streamHandler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
                          

# interval in sec
LOOP_INTERVAL=10

API_KEY =   'aa62d842819f547e4213edd1b9a19e92'
DEVICE_ID = 'df834a7986e9a52d5d28e46dd97e87df'
count=0


try:
  while True:
    try:
      from m2x.client import M2XClient
      client = M2XClient(API_KEY)
      device = client.device(DEVICE_ID)
      #device = client.create_device(
      #    name='currenttime',
      #    description='Store current time ',
      #    visibility= 'public'
      #)
      temp_stream = device.stream('temperture')
      humidity_stream = device.stream('humidit')
      #set up GPIO
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(10, GPIO.OUT)
      
      # Get I2C bus
      bus = smbus.SMBus(1)
    
      #turn the LED on
      GPIO.output(10,1)
      # HDC1000 address, 0x40(64)
      # Select configuration register, 0x02(02)
      #		0x30(48)	Temperature, Humidity enabled, Resolultion = 14-bits, Heater on
      bus.write_byte_data(0x40, 0x02, 0x30)
      
      # HDC1000 address, 0x40(64)
      # Send temp measurement command, 0x00(00)
      bus.write_byte(0x40, 0x00)
      
      time.sleep(0.5)
      
      # HDC1000 address, 0x40(64)
      # Read data back, 2 bytes
      # temp MSB, temp LSB
      data0 = bus.read_byte(0x40)
      data1 = bus.read_byte(0x40)
      
      # Convert the data
      temp = (data0 * 256) + data1
      cTemp = (temp / 65536.0) * 165.0 - 40
      fTemp = cTemp * 1.8 + 32
      
      # HDC1000 address, 0x40(64)
      # Send humidity measurement command, 0x01(01)
      bus.write_byte(0x40, 0x01)

      #turn the LED off
      GPIO.output(10,0)
      time.sleep(0.5)
      
      # HDC1000 address, 0x40(64)
      # Read data back, 2 bytes
      # humidity MSB, humidity LSB
      data0 = bus.read_byte(0x40)
      data1 = bus.read_byte(0x40)
      
      # Convert the data
      humidity = (data0 * 256) + data1
      humidity = (humidity / 65536.0) * 100.0
      
      # Output data to screen
      #print (time.ctime())
      logger.debug ("Relative Humidity : %.2f %%" %humidity)
      logger.debug ("Temperature in Celsius : %.2f C" %cTemp)
      # print "Temperature in Fahrenheit : %.2f F" %fTemp


      count+=1
      if (count ) >= LOOP_INTERVAL:
        #turn the LED on
        GPIO.output(10,1)
        logger.info('---sending data to m2x....---')
        #send data to m2x
        humidity_stream.add_value(humidity)
        temp_stream.add_value(cTemp)
        #reset count
        count=0
        
      #else:
        
      #timee.sleep(LOOP_INTERVAL)
      
    except:     
      GPIO.cleanup()
      logger.warning('connection error! program will sleep for 5 sec before restart')
      time.sleep(5)
      
except KeyboardInterrupt:
  logger.error ('program will exit since Ctl+C pressed.')


