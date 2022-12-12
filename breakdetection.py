#! usr/bin/python3


import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

#connect i2c
i2c_bus = board.I2C()

ina219 = INA219(i2c_bus)

print("ina219 test")

#display fields at startup
#relevant fields for current testing are voltage and current

print("Config register:")
print(" bus voltage_range:  0x%1X" % ina219.bus_voltage_range)
print(" gain:               0x%1X" % ina219.gain)
print(" bus_adc_resolutions:0x%1X" % ina219.bus_adc_resolution)
print(" shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
print(" mode:               0x%1X" % ina219.mode)
print("")



current = ina219.current
print(current)
i=0

#check/display current visible voltage and
while Current > 0.016: 
    current = ina219.current
    bus_voltage = ina219.bus_voltage
    i +=1
    print("Voltage (VIN-) : {:6.3f} V".format(bus_voltage))
    print("Shunt Current : {:8.5f} A".format((current/1000)))
    print(i)
#    time.sleep(1)
