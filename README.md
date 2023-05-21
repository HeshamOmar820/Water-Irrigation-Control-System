# Smart Home Water Irrigation Control System

## Overview

This Python script implements a smart home project that controls water irrigation based on a soil moisture sensor. The system uses a Raspberry Pi and GPIO (General Purpose Input/Output) pins to interact with the soil moisture sensor and a water pump.

## Requirements

To run this code, you need the following hardware components:

- Raspberry Pi (any model with GPIO pins)
- Soil moisture sensor
- Water pump
- Jumper wires for connections

Make sure you have the necessary Python libraries installed, such as `RPi.GPIO`.

## Pin Configuration

The code assumes the following GPIO pin configuration:

- `sensor_pin`: GPIO pin number connected to the soil moisture sensor (input pin)
- `pump_pin`: GPIO pin number connected to the water pump (output pin)

Ensure that you have made the correct connections between the Raspberry Pi, soil moisture sensor, and water pump.

## Functionality

The code performs the following operations:

1. Imports the necessary libraries: `RPi.GPIO` for GPIO control and `time` for time-related operations.

2. Defines the pin numbers for the GPIO communication, `sensor_pin` and `pump_pin`.

3. Defines the `setup()` function, which initializes the GPIO pins. It sets the GPIO pin numbering mode to BCM and configures `pump_pin` as an output pin and `sensor_pin` as an input pin.

4. Defines the `read_moisture()` function, which reads the moisture level from the soil moisture sensor. It uses the `GPIO.input()` function to retrieve the sensor value.

5. Defines the `control_irrigation()` function, responsible for controlling the water irrigation process based on the moisture level. It performs the following steps:
   - Sets a `moisture_threshold` value, which can be adjusted based on sensor readings.
   - Reads the current moisture level using the `read_moisture()` function.
   - If the moisture level is below the threshold, it activates the water pump by setting `pump_pin` to a high state using `GPIO.output()`.
   - Prints a message indicating that watering is in progress.
   - Pauses the program execution for a specified duration (5 seconds in this example) using `time.sleep()`.
   - Deactivates the water pump by setting `pump_pin` to a low state.
   - Prints a message indicating that watering is finished.
   - If the moisture level is above or equal to the threshold, it prints a message indicating that irrigation is not required.


7. In the main program, it checks if the script is being run directly and not imported as a module (`if __name__ == '__main__'`).
   - Sets up the GPIO pins using the `setup()` function.
   - Calls the `control_irrigation()` function to control the irrigation process.
   - Catches the `KeyboardInterrupt` exception to handle program termination via Ctrl+C.

## Usage

1. Make the necessary hardware connections between the Raspberry Pi, soil moisture sensor, and water pump.

2. Install the required Python libraries, such as `RPi.GPIO`.

3. Save the Python script to a file, e.g., `irrigation_control.py`.

4. Run the script using `python irrigation_control.py` or a similar command.

5. Observe the console output, which will indicate whether watering is needed and control the water pump accordingly.

