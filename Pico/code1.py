# Import necessary libraries
import board
import busio
from adafruit_dps310.basic import DPS310
import adafruit_mcp9808
import adafruit_adxl34x

# Initialize I2C communication
i2c = busio.I2C(scl=board.GP27,sda=board.GP26)

# Initialize sensors
dps310 = DPS310(i2c)
mcp = adafruit_mcp9808.MCP9808(i2c)
adxl343 = adafruit_adxl34x.ADXL343(i2c)

# Continuous data reading loop
while True:
    print("dps310 Temperature = %.2f C" % dps310.temperature)
    print("dps310 Pressure = %.2f hPa" % dps310.pressure)   
    print("mcp9808 Temperature = %.2f C" % mcp.temperature) 
    print("adxl343 accelerometer %f %f %f" % adxl343.acceleration)


