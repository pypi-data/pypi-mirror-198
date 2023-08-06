**Some useful stuff**
---

``` bash 
$ pip install ColadaUtility
```
---

``` python3
from ColadaUtility.PowerColor import Colors as c
from ColadaUtility.PowerLogger import Logger


log = Logger()
log.coloredTerminal = True
log.outputFile = 'C:\\Git\\Playground\\log.txt'
log.tune()

log.d('Chilly debug message')
log.i('Usual INFO log, whatever')
log.w('Warning? Warning!!!')
log.e(f'Some big UH-OH happened here...')
log.d(c(p="link", text="http://www.google.com"))
log.i(f'Unusual but {c(f="g", d="i u b")}pretty{c()} INFO {c(b="g", t="log")} ~!')
```
---
<img src="https://i.ibb.co/vBzRBzL/Colada-Utility.png" alt="Colada-Utility" border="0">