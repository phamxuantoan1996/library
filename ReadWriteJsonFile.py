import json
class ManipulationJsonFile:
    def __init__(self,path:str):
        self.__pathName = path
        self.__pointerFile = None
    def openFile(self,mode:str) -> bool:
        try:
            self.__pointerFile = open(file=self.__pathName,mode=mode)
            return True
        except Exception as e:
            return False
    def writeFile(self,content:dict) -> bool:
        try:
            json.dump(content,self.__pointerFile)
            return True
        except Exception as e:
            return False
        
    def deleteAllContent(self) -> bool:
        try:
            self.__pointerFile.truncate(0)
            return True
        except Exception as e:
            return False
        
    def readFile(self) -> dict:
        try:
            content = None
            content = json.load(self.__pointerFile)
        except Exception as e:
            pass
        return content
        
    def closeFile(self) -> None:
        self.__pointerFile.close()
        

if __name__ == '__main__':
    mission_save = ManipulationJsonFile(path='mission_save.json')
    mission_save.openFile(mode='r+')
    # mission_save.deleteAllContent()
    # mission_save.writeFile(content={'key2':1})
    print(mission_save.readFile())
    mission_save.closeFile()

        