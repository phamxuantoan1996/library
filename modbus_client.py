from abc import ABC,abstractmethod
import minimalmodbus
import serial
import time

class Modbus_Function_Code:
    #input
    ReadInputRegs = 4
    ReadHoldRegs = 3
    
    #holding
    WriteHoldRegs = 16
    WriteHoldReg = 6

class Modbus_Client(ABC):
    def __init__(self,slave_id:int,number_of_input:int,number_of_hold:int,timeout_modbus:int) -> None:
        super().__init__()
        self.timeout_modbus = timeout_modbus
        self.timeout_response = 10
        self._number_of_input = number_of_input
        self._number_of_hold = number_of_hold
        self._modbus_error = True
        self._input_regs = []
        self._hold_regs = [0] * self._number_of_hold
        self._slave_id = slave_id

    @abstractmethod
    def connect_to_server(self) -> bool:
        pass

    @abstractmethod
    def read_input_regs(self):
        pass

    @abstractmethod
    def write_hold_regs(self):
        pass

    @abstractmethod
    def poll_server(self):
        pass
    @property
    def number_of_input(self):
        return self._number_of_input
    @property
    def number_of_hold(self):
        return self._number_of_hold
    @property 
    def slave_id(self):
        return self._slave_id
    
class Modbus_Serial_Client(Modbus_Client):
    def __init__(self, slave_id:int, number_of_input: int, number_of_hold: int,port:str,baudrate:int,timeout_modbus:int) -> None:
        super().__init__(slave_id,number_of_input, number_of_hold)
        self.port = port
        self.baudrate = baudrate
        
        
    def connect_to_server(self) -> bool:
        super().connect_to_server()
        try:
            # os.chmod(self.port,stat.S_IRWXO)
            self.client = minimalmodbus.Instrument(port=self.port,slaveaddress=self._slave_id,mode=minimalmodbus.MODE_RTU)
            self.client.serial.baudrate = self.baudrate
            self.client.serial.bytesize = 8
            self.client.serial.parity = serial.PARITY_NONE
            self.client.serial.timeout = self.timeout_modbus
            self.client.serial.stopbits = 1
            return True
        except Exception as e:
            # self.logfile.writeLog(type_log='error',msg=str(e))
            print('error : ' + str(e))
            return False
        
        return True
    
    def read_input_regs(self,address:int,count:int) -> list | None:
        super().read_input_regs()
        try:
            value = self.client.read_registers(registeraddress=address,number_of_registers=count,functioncode=Modbus_Function_Code.ReadInputRegs)
            return value
        except Exception as e:
            print(str(e))
            return None
    
    def write_hold_regs(self,address:int,value:list) -> None:
        super().write_hold_regs()
        try:
            self.client.write_registers(registeraddress=address,values=value)
            return True
        except Exception as e:
            print(str(e))
            return False
    
    def poll_server(self):
        super().poll_server()
        while True:
            time.sleep(1)

            
        

mb_client = Modbus_Serial_Client(number_of_input=10,number_of_hold=10,port='COM1',baudrate=115200)
mb_client.connect_to_server()




