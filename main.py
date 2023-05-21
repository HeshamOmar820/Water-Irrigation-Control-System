# Importing libraries
import RPi.GPIO as GPIO
import time

# Pin numbers for GPIO communication
sensor_pin = 14
pump_pin = 18

def setup():
    # Setting GPIO pin numbering mode to BCMv
    GPIO.setmode(GPIO.BCM)
    # Setting pump pin as output
    GPIO.setup(pump_pin, GPIO.OUT)
    # Setting sensor pin as input
    GPIO.setup(sensor_pin, GPIO.IN)

def read_moisture():
    # Reading sensor pin value
    return GPIO.input(sensor_pin)

def control_irrigation():
    # Adjusting this value based on sensor readings
    moisture_threshold = 500  
    # Reading the current moisture level
    moisture_level = read_moisture()

    if moisture_level < moisture_threshold:
        # Activating water pump
        GPIO.output(pump_pin, GPIO.HIGH)
        print("Watering the plants...")
        # Irregation duration
        time.sleep(5) 
        # Deactivating water pump
        GPIO.output(pump_pin, GPIO.LOW)
        print("Finished watering.")
    else:
        print("No need for irrigation.")

# Main program
if __name__ == '__main__':
    # Initializing GPIO pins
    setup()
    # Controling the irrigation process
    control_irrigation()