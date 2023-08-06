import datetime
import re

from ColadaUtility.PowerColor import Colors as c
res = 'res'

class Logger():
    def __init__(self) -> None:
        self.writeDateToTerminal = True
        self.writeDataToFile = True
        self.coloredTerminal = False
        self.outputFile = ''
        self.outputFiles = []
        self.tune()
    
    
    def tune(self) -> None:
        if self.outputFile != '':
            self.outputFiles.append(self.outputFile)
        self.encoding = 'utf-8'
        self.dateFormat = f'%Y-%m-%d ||{c(e=self.coloredTerminal, f="y")} %H:%M:%S{c()} || '
    
    
    def d(self, inf: str) -> None:
        message =  f'{self.__getDate__()}{c(e=self.coloredTerminal, f="lb", d="b", text="DEBUG")} : {inf}' 
        terminalMessage, fileMessage = self.__generateMessage__(message)
        print(terminalMessage)
        self.__logToFiles__(fileMessage)
        
        
    def i(self, inf: str) -> None:
        message = f'{self.__getDate__()}{c(e=self.coloredTerminal, f="y", d="b", text=" INFO")} : {inf}'
        terminalMessage, fileMessage = self.__generateMessage__(message)
        print(terminalMessage)
        self.__logToFiles__(fileMessage)
        
    
    def w(self, inf: str) -> None:
        message = f'{self.__getDate__()}{c(e=self.coloredTerminal, f="p", d="b", text=" WARN")} : {inf}'
        terminalMessage, fileMessage = self.__generateMessage__(message)
        print(terminalMessage)
        self.__logToFiles__(fileMessage)


    def e(self, inf: str) -> None:
        message = f'{self.__getDate__()}{c(e=self.coloredTerminal, f="r", b="x", d="b", text="ERROR")} : ' +\
        f'{c(e=self.coloredTerminal, f="r", d="i")}{inf}{c()}'
        terminalMessage, fileMessage = self.__generateMessage__(message)
        print(terminalMessage)
        self.__logToFiles__(fileMessage)     
                    
    
    def __logToFiles__(self, message: str) -> None:
        for _file in self.outputFiles:
            try:
                with open(_file, mode='r') as f:
                    f.close()
            
            except(FileNotFoundError):
                self.__createLogFile__(_file)
                
            finally:
                with open(_file, mode='a', encoding=self.encoding) as f:
                    f.write(message + '\n')
                    f.close()
                    
    
    def __createLogFile__(self, filepath: str) -> None: 
        try:
            with open(filepath, mode='w') as f:
                f.close()
                self.i(f'Created file {filepath}')
                
        except:
            self.i(f'Unable to create file: {filepath}')
    
                    
    def __generateMessage__(self, message:str):
        terminal = message
        filem = re.sub(r'([^m]*)m', '', message)
        
        return terminal, filem
                            
                
    def __getDate__(self) -> str:
        date = datetime.datetime.now().strftime(self.dateFormat)       
        return str(date)
    