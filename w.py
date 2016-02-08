#!usr/bih/env python3
import sys
import struct
import os
import translit



s= translit_str('This is Проверка')

print(s)

flist=os.listdir()
print(flist)

for fl in os.scandir('.'):
    fname=fl.name
    print('Очередное имя ',fname)
    if fl.is_file():
        os.rename(fl.name,low_case_str(fl.name))

vd=[1,2,3,4,5,6,7,8,9]


some_str='str for examplE СТРОКА для ПРИМЕРА'
for symbol in some_str:
    print(symbol)

print(some_str.__sizeof__())


print(some_str.lower())