from plantower import pt_pms5003
import time
import sys

def aqi_main():
    """ main routine which reads reading relentlessly"""
    readout = pt_pms5003('/dev/ttyAMA0')
    while True:
        pma,pmb,pmc=readout.pt_pms5003_read()
        print("************************************************************")
        print("Air Quality (Atmospheric   ) >> PM 1.0: "+str(pma)+
              " PM 2.5: "+str(pmb)+" PM 10: "+str(pmc))
        time.sleep(1)
aqi_main()
