#!usr/bih/env python3
import sys
import struct
import os
from translit import translit_str



s= translit_str('This is Проверка')

flist=os.listdir()
print(flist)

for fl in os.scandir('.'):
    if fl.is_file():
        try:
            os.rename(fl.name,translit_str(fl.name))
        except:
            print('Не переименовано ',fl.name)

