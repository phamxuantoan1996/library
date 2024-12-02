import serial
import minimalmodbus
import os
import stat
from logfile import LogFile

class Modbus_Function_Code:
    #input
    ReadInputRegs = 4
    ReadHoldRegs = 3
    
    #holding
    WriteHoldRegs = 16
    WriteHoldReg = 6

import time
class Modbus_Serial_Client:
    def __init__(self,port_mb:str,baudrate:int,slave_id:int,timeout:int,log:LogFile) -> None:
        self.port = port_mb
        self.slave_id = slave_id
        self.baudrate = baudrate
        self.timeout_modbus = timeout
        self.timeout_response = 10
        self.log = log
        
        
    def connnect_modbus_server(self) -> bool:
        try:
            os.chmod(self.port,stat.S_IRWXO)
            self.client = minimalmodbus.Instrument(port=self.port,slaveaddress=self.slave_id,mode=minimalmodbus.MODE_RTU)
            self.client.serial.baudrate = self.baudrate
            self.client.serial.bytesize = 8
            self.client.serial.parity = serial.PARITY_NONE
            self.client.serial.timeout = self.timeout_modbus
            self.client.serial.stopbits = 1
            return True
        except Exception as e:
            self.log.writeLog(type_log='error',msg = "Error : " + str(e))
            return False
    

    #custom
    #set rgb