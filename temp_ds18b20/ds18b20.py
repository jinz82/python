import glob,os

sensor_device_path  =   "/sys/bus/w1/devices/"
sensor_file         =   "w1_slave"

sensor_checksum_ok  =   "YES"
DALLAS_class        =   "28-*"
checksum_index      =   -3
temperature_index   =   -5
sensor_divisor      =   1000
sensor_precision    =   4

def ds18b20_sensor_get():
    """Gets a sensor path and returns the same for DALLAS devices."""
    os.chdir(sensor_device_path)
    sensor_dir = glob.glob(DALLAS_class)
    # Though we have a list of all sensor classes we are interested only in first.
    return sensor_dir.pop()

def ds18b20_read():
    """Routine to read temperature value in celcius"""
    sensor_dir = ds18b20_sensor_get()
    if sensor_dir:
        sensor_path = os.path.join(sensor_device_path,sensor_dir,sensor_file)
        with open(sensor_path) as sensor_handle:
            sensor_lines = sensor_handle.readlines()
            # First line has checksum.
            checksum = sensor_lines.pop(0).strip()[checksum_index:]
            if checksum == sensor_checksum_ok:
                # Second line has temperature if checksum is ok.
                sensor_temperature = sensor_lines.pop(0).strip()[temperature_index:]
                return str(float(sensor_temperature)/float(sensor_divisor))[:sensor_precision]
            else:
                return 0

    else:
        return 0

