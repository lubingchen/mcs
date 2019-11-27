#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Use physical pin numbers
GPIO.setmode(GPIO.BCM)
# Set up header pin 22 (GPIO25) as an input
buttonPin = 24
print ("Setup Pin 22")
GPIO.setup(buttonPin, GPIO.IN)


while True:
  #take a reading
  input = GPIO.input(24)
  #if the last reading was low and this one high, print
  if (input):
    print("Button pressed")
  else :
    print("release")
  #slight pause to debounce
  time.sleep(0.05)
