class Colors:
    def __new__(self, e = True, *_arg, **args) -> str:
        self.enabled = e
        
        self.fgKeys = ['foreground', 'fg', 'f']
        self.bgKeys = ['background', 'bg', 'b']
        self.decKeys = ['decorations', 'decor', 'deco', 'dec', 'd']
        self.tKeys = ['text', 't']
        self.pKeys = ['preset', 'p']
        
        self.default = ['9', 'def', 'res', 'default', 'auto']
        self.black = ['0', 'bl', 'x', 'black']
        self.red = ['1', 'r', 'red']
        self.green = ['2', 'g', 'green']
        self.yellow = ['3', 'y', 'yellow']
        self.blue = ['4', 'b', 'blue']
        self.magenta = ['5', 'm', 'p', 'magenta', 'pink', 'purple']
        self.cyan = ['6', 'c', 'lb', 'cyan', 'lightblue']
        self.white = ['7', 'w', 'white']
        
        self.bold = ['1', 'bold', 'black', 'b']
        self.italic = ['3', 'italic', 'i']
        self.underline = ['4', 'underline', 'link', 'url', 'uri', 'u', 'l', '_']
        self.strike = ['9', 'strikethrough', 'strike', 'cross', 'dash', 'del', 's', 'd']
        
        self.escapeCode = '\033['      
        self.res = '\x1b[0m'
        
        self.foreground = False
        self.background = False
        self.decorations = False
        self.text = False
        self.preset = False
        
        self.fgVal = None
        self.bgVal = None
        self.decVal = None
        self.tVal = None
        self.pVal = None
        
        if not self.enabled:
            return ''
        
        for arg, val in args.items():
            if arg in self.fgKeys:
                self.foreground = True
                self.fgVal = val
                
            if arg in self.bgKeys:
                self.background = True
                self.bgVal = val
                
            if arg in self.decKeys:
                self.decorations = True
                self.decVal = val
                
            if arg in self.tKeys:
                self.text = True
                self.tVal = val
                
            if arg in self.pKeys:
                self.preset = True
                self.pVal = val
                
        if 'link' in _arg:
            print('link found')
            return self.__decorateLink__()
        
        if self.foreground:
            if self.fgVal in self.default:
                self.__makeFg__(self, self.default[0])
                
            if self.fgVal in self.black:
                self.__makeFg__(self, self.black[0])    
                
            if self.fgVal in self.red:
                self.__makeFg__(self, self.red[0])
                
            if self.fgVal in self.green:
                self.__makeFg__(self, self.green[0])
                
            if self.fgVal in self.yellow:
                self.__makeFg__(self, self.yellow[0])
                    
            if self.fgVal in self.blue:
                self.__makeFg__(self, self.blue[0])
                
            if self.fgVal in self.magenta:
                self.__makeFg__(self, self.magenta[0])
                
            if self.fgVal in self.cyan:
                self.__makeFg__(self, self.cyan[0])
                
            if self.fgVal in self.white:
                self.__makeFg__(self, self.white[0])                     
                
        if self.background:
            if self.bgVal in self.default:
                self.__makeBg__(self, self.default[0])
                
            if self.bgVal in self.black:
                self.__makeBg__(self, self.black[0])    
                
            if self.bgVal in self.red:
                self.__makeBg__(self, self.red[0])
                
            if self.bgVal in self.green:
                self.__makeBg__(self, self.green[0])
                
            if self.bgVal in self.yellow:
                self.__makeBg__(self, self.yellow[0])
                    
            if self.bgVal in self.blue:
                self.__makeBg__(self, self.blue[0])
                
            if self.bgVal in self.magenta:
                self.__makeBg__(self, self.magenta[0])
                
            if self.bgVal in self.cyan:
                self.__makeBg__(self, self.cyan[0])
                
            if self.bgVal in self.white:
                self.__makeBg__(self, self.white[0])
                
        if self.decorations:
            decorations = self.decVal.split(' ')
            for decorator in decorations:
                if decorator in self.bold:
                    self.__makeDec__(self, self.bold[0])
                    
                if decorator in self.italic:
                    self.__makeDec__(self, self.italic[0])
                
                if decorator in self.underline:
                    self.__makeDec__(self, self.underline[0])
                    
                if decorator in self.strike:
                    self.__makeDec__(self, self.strike[0])
                    
        if self.preset:
            if self.pVal == 'link':
                self.__makeFg__(self, self.blue[0])
                self.__makeDec__(self, self.italic[0])
                self.__makeDec__(self, self.underline[0])
        
                
        if self.text:
            return self.__finalEscapeCode__(self) + self.tVal + self.res
        
            
        return self.__finalEscapeCode__(self)


    def __makeFg__(self, color:str) -> None:
        self.escapeCode += f'3{color}'

        
    def __makeBg__(self, color:str) -> None:
        self.escapeCode += f';4{color}'

        
    def __makeDec__(self, dec:str) -> None:
        self.escapeCode += f';{dec}'
        
        
    def __decorateLink__(self) -> str:
        if not self.text:
            return ''
        
        self.__makeFg__(self, self.blue[0]) 
        self.__makeDec__(self, self.italic[0])
        self.__makeDec__(self, self.undeline[0])
        link = self.__finalEscapeCode__(self) + self.tVal + self.res
        
        return link
        
        
    def __finalEscapeCode__(self) -> str:
        return self.escapeCode + 'm'