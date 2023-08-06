# Search for values in regedit 


```python

$pip install reggisearch

r"""
.reg file:

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks_nxt]
"LogDir"="C:\\ProgramData\\BlueStacks_nxt\\Logs\\"
"DataDir"="C:\\ProgramData\\BlueStacks_nxt\\Engine\\"
"InstallDir"="C:\\Program Files\\BlueStacks_nxt\\"
"UserDefinedDir"="C:\\ProgramData\\BlueStacks_nxt"

"""

from reggisearch import search_values

di=search_values(mainkeys=r"HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks_nxt", subkeys=("DataDir", "InstallDir"))
print(di)
{'HKEY_LOCAL_MACHINE\\SOFTWARE\\BlueStacks_nxt': {'DataDir': 'C:\\ProgramData\\BlueStacks_nxt\\Engine\\', 'InstallDir': 'C:\\Program Files\\BlueStacks_nxt\\'}}


```
