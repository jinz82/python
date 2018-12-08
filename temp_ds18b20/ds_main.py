from time import sleep
from ds18b20 import ds18b20_read

def temp_main():
    """ Main loop"""
    while(True):
        current_temperature = ds18b20_read()
        if (current_temperature):
            print(current_temperature)
        else:
            print("None")
        sleep(1)

temp_main()
