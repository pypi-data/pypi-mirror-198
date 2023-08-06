# Kills python + all subprocesses, restarts with the same args, Windows only, works with pyinstaller

### pip install babyonemoretime

```python

from babyonemoretime import restart_everything
from time import sleep
import subprocess
import sys

sleep(4)
if sys.argv[1] == "n":
    subprocess.Popen("notepad.exe")
else:
    subprocess.Popen("word.exe")

sleep(4)
restart_everything(pyfile=__file__, sysarv=sys.argv, restart=False)  # kills everything
restart_everything(pyfile=__file__, sysarv=sys.argv, restart=True) # kills everything and restarts




# python.exe resa.py n

```
