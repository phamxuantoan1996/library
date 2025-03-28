import requests
import time

class APR_Led_Color:
    Non = 0
    Red = 8
    Yellow = 10
    Green = 2

class APR_Convoyer:
    Stop = 0
    CW = 1
    CCW = 2

class APR_Stopper:
    Non = 0
    Close = 1
    Open = 2

class APR_Hold_Addr:
    Led = 0
    Lift = 1
    Convoyer = 2
    Stopper = 3

class Server_ID:
    Led = 1
    Control_Board = 2
    Sensor_Door1 = 3
    Sensor_Door2 = 4

class AGF_Control:

    def set_hold_reg(self,val:list,slave_id:int) -> bool:
        url_post = "http://127.0.0.1:8002/hold_regs"
        hold_reg = {
            "slave_id":slave_id,
            "hold":val
        }
        try:
            response = requests.post(url=url_post,json=hold_reg)
            if response.status_code == 201:
                return True
        except Exception as e:
            print(e)
        return False
    
    def get_input_reg(self,slave_id:int) -> list:
        url_get = "http://127.0.0.1:8002/input_regs?slave_id=" + str(slave_id)
        try:
            response = requests.get(url=url_get)
            if response.status_code == 200:
                content = response.json()
                if 'input' in content.keys():
                    return content['input']
        except Exception as e:
            print(e)
        return []
    
    def SetLed(self,color:APR_Led_Color):
        values = [{"address" : APR_Hold_Addr.Led,"value" : color}] 
        self.set_hold_reg(val=values,slave_id=1)
        print('--set_led--')

    def SetLift(self,lift:int):
        values = [{"address" : APR_Hold_Addr.Lift,"value" : lift}] 
        self.set_hold_reg(val=values,slave_id=2)
        print('--set_lift--')

    def SetConvoyer(self,dir:APR_Convoyer):
        values = [{"address" : APR_Hold_Addr.Convoyer,"value" : dir}] 
        self.set_hold_reg(val=values,slave_id=2)
        print('--set_convoyer--')

    def SetStopper(self,status:APR_Stopper):
        values = [{"address" : APR_Hold_Addr.Stopper,"value" : status}] 
        self.set_hold_reg(val=values,slave_id=2)
        print('--set_stopper--')
    
    def Test(self,value:int):
        values = [{"address" : 0,"value" : value}] 
        self.set_hold_reg(val=values,slave_id=2)
        print('--set_stopper--')
    

if __name__ == '__main__':

    apr_board_control = AGF_Control()
    # apr_board_control.SetLed(color=APR_Led_Color.Red)
    while True:
        apr_board_control.Test(value=0)
        time.sleep(1)
        apr_board_control.Test(value=1)
        time.sleep(1)