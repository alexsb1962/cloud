#!usr/bih/env python3
import sys
import struct
import os
from translit import translit_str
from trans import trans


from math import *
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0,5.0,0.01)
y = 2.0*np.exp(-x/1.1)

plt.plot(x,y)
plt.show()


s= translit_str('This is Проверка'); print(s)
s= trans('This is Проверка'); print(s)

flist=os.listdir()
print(flist)

for fl in os.scandir('.'):
    if fl.is_file():
        try:
            os.rename(fl.name,translit_str(fl.name))
        except:
            print('Не переименовано ',fl.name)

