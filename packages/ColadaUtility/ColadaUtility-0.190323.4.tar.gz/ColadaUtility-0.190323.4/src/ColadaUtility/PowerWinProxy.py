import winreg

class Proxy():
    def __init__(self) -> None:
        self.__regpath__ = r'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings'
    
    def set(self, addr: str) -> bool:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 self.__regpath__,
                                 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'ProxyServer', 0, 1, addr)
            winreg.CloseKey(key)
            return True
        
        except:
            return False
        
    
    def enable(self) -> bool:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 self.__regpath__,
                                 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'ProxyEnable', 0, 4, 1)
            winreg.CloseKey(key)
            return True
        
        except:
            return False
        
    
    def disable(self) -> bool:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 self.__regpath__,
                                 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, 'ProxyEnable', 0, 4, 0)
            winreg.CloseKey(key)
            return True
        
        except:
            return False
        
    
    def getCurrentProxy(self) -> str:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 self.__regpath__,
                                 0, winreg.KEY_READ)
            proxy = winreg.QueryValueEx(key, 'ProxyServer')
            winreg.CloseKey(key)
            return proxy[0]
        except:
            return 'Failed to get current proxy'
        

    def getProxyStatus(self) -> bool:
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 self.__regpath__,
                                 0, winreg.KEY_READ)
            status = winreg.QueryValueEx(key, 'ProxyEnable')
            winreg.CloseKey(key)
            return bool(status[0])
        
        except:
            raise(RuntimeError)