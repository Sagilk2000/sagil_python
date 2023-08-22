"""
multipy all the numbers in a list using function
"""
import math

# num=[1,2,3,4,5]
# def multi(num):
#     s = 1
#     for i in num:
#         s=s*i
#     print(s)
# multi(num)
#
"""
sum of  all the numbers in a list using function
"""
# num=[1,5,9,7,6,5]
# def sum(num):
#     s=0
#     for i in num:
#         s=s+i
#     print(s)
# sum(num)

"""
write a program to reverse a string
"""
# string='1234abcd'
# def reverse_strng(string):
#     x=list(string)
#     x.reverse()
#     print(''.join(x))
# reverse_strng


# string='1234abcd'
# def revers(string):
#     rev=''
#     for i in string:
#         rev = i+rev
#     print(rev)
# revers(string)

"""
factorial of a number
"""
# def fact(num):
#     f=1
#     for i in range(1,num+1):
#         f=f*i
#     print(f)
# num=int(input("enter a number:"))
# fact(num)


"""
write a python program function that take place a number as a parameter and check the prime or not
"""
# def num(numb):
#     if numb%1==0 and numb%2!=0:
#         print(numb,"is prime")
#     else:
#         print(numb,"is not prime")
# numb=int(input("enter a number:"))
# num(numb)

# def is_prime(num):
#     if num<=1:
#         return False
#     elif num==2:
#         return True
#     elif num%2==0:
#         return False
#     else:
#         sqrt_num=math.sqrt(num)
#         for i in range(3,sqrt_num+1,2):
#             if num%i==0:
#                 return False
#         return True
#
# print(is_prime(17))
#not completed this prime num program

"""
fibonacci series using function
"""
# def fibo(a,b):
#     for i in range(1,11):
#         print(a,end=' ')
#         c=a+b
#         a=b
#         b=c
# fibo(0,1)



"""
generate a list of all even numbers between 4 to 30
"""

# def even():
#     eve = []
#     for i in range(4,31):
#         if i%2==0:
#             eve.append(i)
#     print(eve)
# even()
#list comprihension method
# even=[i for i in range(4,31) if i%2==0]
# print(even)



# s=input("enter a string:")
# def palindrome(s):
#     str=""
#     for i in s:
#         str=i+str
#     if s==str:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome(s)


def reverse(str):
    str1=[str[i] for i in range(len(str)-1,-1,-1)]
    x=(''.join(str))
    if x==str:
        print("palindrome")
    else:
        print("not palindrome")
str=input("enter a string:")
reverse(str)


# def create_adder(x):
#     def adder(y,z):
#         return x+y+z
#     return adder
# print(create_adder(15)(10,50))
#
