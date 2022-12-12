# Sheet-Metal-Fatigue-Fixture
Software implemented on a Raspberry Pi 3 and an Arduino Uno R3 to run the electronic components of a sheet metal fatigue test apparatus.

This project was developed in conjunction with Schweitzer Engineering Labs as part of an aparatus that tests the fatigue point of sheet metal as a capstone project at the University of Idaho.

The Main Sensor test file was the implementation of a sensor that tracked the revolutions of the main motor for the device.  This allowed for the calculation of both active rpm and total cycles completed before failure.

The breakdetection.py file implements a current detection method that would indicate when the sheet metal had broken and could be used to signal the end of the test.

Hx711py-master has all files associated with and necessary for running the load cell including a custom lib for the hx711 load cell.
