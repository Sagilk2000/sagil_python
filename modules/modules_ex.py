
"""
javascript object notation
a python module can be defined as python program file which contains a python code including python functions,class or variables


"""
import now as now

#value passing
import sample
from sample import sum
# print(sum(4,6))

#builtin modules
#math module
import math

# print(math.sqrt(5))
# print(math.factorial(5))
# print(math.pi)
# r=5
# print(math.pi*r*r)

"""
OS module
it is possible to automatically perform many operatinf system tasks. the os module in python provides functions for creatimg and removing 
a directory(folder) fetch its contents ,changing and identifying the curret directory
"""
import os
# os.mkdir(r"C:\Users\Sagil\PycharmProjects\pythonProject1\modules\test")
# os.rmdir(r"C:\Users\Sagil\PycharmProjects\pythonProject1\modules\test")

#change directory
#
# print(os.getcwd())
# os.chdir('D:/')
# print(os.getcwd())
#
# os.chdir('C:/')
# print(os.getcwd())

#RANDOM MODULE
import random

# print(random.randrange(100))
# print(random.randint(1,6))
#
# a=[1,2,3,4,5]
# random.shuffle(a)
# print(a)
#
# str='computer'
# print(random.choice(str))


#DATE ABD TIME


import datetime
from datetime import date

#
# today = date.today()
# print(today)
#
# tim = now.strftime("%H:%M:%S")
# print(tim)
#
# tym=datetime.datetime.now()
# print(tym)

# print(random.randint(1,10)*7)
"""generate random hex colors"""
# color="#%06x"%random.randint(0,0xffffff)
# print(color)

