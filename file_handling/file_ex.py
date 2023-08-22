"""
file handling

create = x
write  = w
read   = r
delete = remove
add    = append


"""
import os.path

# file = open('sample.txt','w')
# file.write("hii sagil")
# file.close()
#
# file=open('sample.txt','r')
# print(file.read())
# file.close()
#
# file=open('sagil.py','r')
# print(file.read())
# file.close()
#
# file=open('sample.txt','a')
# file.write(" how are you")
# file.close()
#
# file=open('sample.txt','r')
# print(file.read())
# file.close()

# with open("sample.txt",'r') as file:
#     print(file.read())
#     file.close()

#
# with open("sagil.py",'r') as file:
#     print(file.read())
#     file.close()
#
#
# with open("sagil.py",'w')as file:
#     file.write("the program is successfully excecuted and the output is verified")
#     file.close()

"""create a file  and remove file with os module"""
# with open("sample2.txt",'w')as file:
#     file.write('hellogooys')
#     file.close()
#
# import os
# os.remove('sample2.txt')


"""
to check wether a file is existing or not
"""

filepath=r'sagil.py'
x=os.path.exists(filepath)
if x:
    print(filepath,"file is existing")
else:
    print(filepath,"not existing")


""" to get a file size"""

# filesize = r'sample.txt'
# x=os.path.getsize(filesize)
# print(x)

"""To count the number of lines in a file using Python"""

# with open(r'sagil.py','r')as file:
#     line=len(file.readline())
#     print(line)
#
# """to count the length"""
# with open(r'sagil.py','r')as file:
#     line=len(file.readlines())
#     print(line)

# with open(r'sagil.py','r')as file:
#     x=file.read()
# n=input("enter a word:")
# if n in x:
#     print("the word already in this file")
# else:
#     print("not exist")


"""read a specific line in a text file"""
import linecache
# x=linecache.getline('sagil.py',2)
# print(x)
#another method
# n=int(input("enter a number:"))
# with open('sagil.py','r')as file:
#     x=file.readlines()
#     print(x[n-1])


"""delete line in a text file"""
# with open('sagil.py','r')as file:
#     x=file.readlines()
#     pri

""" write list to a file in python"""
# with open('sample.txt','r')as file:
#     x=file.read()
#     y=list(x)
#     print(type(y))
#     file=open('sagil.py','a')
#     file.write(y)
#     file.close()

# nemes=['asss','dddd','ddddffg']
#

import csv

# with open('csv_ex.csv','r')as file:
#     reader= csv.reader(file)
#     for row in reader:
#         print(row)
#         file.close()

# with open('csv_ex.csv','w')as file:
#     writer=csv.writer(file)
#     writer.writerow(['ECTA.S19A1', '2009.03', '40629.4', '', 'F', 'sagil', '6', 'Electronic Card Transactions (ANZSIC06) - ECT', 'Total values - Electronic card transactions A/S/T by division', 'Actual', 'RTS total industries', '', '', ''])
#     file.close()

# with open('csv_ex.csv','w')as file:
#     fieldnames=["name","age","course","place"]
#     writer=csv.DictWriter(file,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({"name":"sagil","age":23,"course":"python","place":"ekm"})
#     writer.writerow({"name":"sarang","age":24,"course":"python","place":"pkl"})
#     file.close()
# #
# with open('csv_ex.csv','r')as file:
#     x=csv.DictReader(file)
#     for row in x:
#         print(row)

import fileinput
# file='sagil.py'
# x=[2,4]
# def delete_lines(file,x):
#     with fileinput.input(file,inplace=True)as file:
#         for i in file:
#             if file.lineno() not in x:
#                 print(i.rstrip())
# delete_lines(file,x)

import os
"""
1.list files in a directory
2.count no of files in a directory
3.list files in a directory with extension.txt
"""
# list=os.listdir(r'C:\Users\Sagil\PycharmProjects\pythonProject1\file_handling')
# print("list:",list)
# print(len(list))
#
# list1=os.listdir(r'C:\Users\Sagil\PycharmProjects\pythonProject1\functions')
# def count_list(list1):
#     count=0
#     listfiles = os.listdir(list1)
#     for i in listfiles:
#         count+=1
#         print(count)

#
# for i in list:
#     if i.endswith("py"):
#         print("files with extension:",i)


"""python to write a list"""
# list1=['mango','apple']
# with open('sagil.py','w')as sag:
#     for i in list1:
#         sag.write(str(i)+'\n')
# sag.close()


"""python program to get file creation and modification date time"""

import os.path,time
# newf=open("sagil.py",'w')
# newf.write('hello gooys')
# print("created time:",time.ctime(os.path.getctime("sagil.py")))
# print("last modified time:",time.ctime(os.path.getmtime("sagil.py")))

"""specific line from a text file"""
# with open("sagil.py",'r')as file:
#     x=file.readlines()
#     print(x)
#     print(len(x))
# n=int(input("enter a line number you want:"))
# print(x[n-1])



""""""
# list_items=["apple","orange","mango","grape"]
# with open('fruits.txt','w')as file:
#     for i in list_items:
#         file.write(i+'\n')

