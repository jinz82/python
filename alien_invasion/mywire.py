import wiringpi2 as wiringpi

def serial_read():
 wiringpi.wiringPiSetup()
 serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
#	wiringpi.serialPuts(serial,'hello world!')
 while(1):
  print(hex(wiringpi.serialGetchar(serial)))
 
serial_read()
