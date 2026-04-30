# Voltage Monitoring

import sys
import select
from time import sleep

pedo = machine.ADC(28)

while True:
    
    # Check if data is available on the serial interface
    if select.select([sys.stdin], [], [], 0)[0]:
        # Read command
        command = sys.stdin.readline().strip()     # select.select(read_list, write_list, error_list, timeout)

        if command == "*IDN?":
            print("Rasberry Pie Pico 2 W")
            
        elif command == "How:are:you?":
            print("WHATSUPPPPP!!!!")
        
        elif command == "MEAS:RAW?":
            value = pedo.read_u16()
            print(value)
        
        elif command == "MEAS:VOLT?":
            value = pedo.read_u16()  * 3.3 / 65535
            print(value)
        else:
            print("ERROR!!!!")
        
            
    sleep(0.2)
