"""
1. to check weather a number is prime or not
"""
from setuptools.command.install import install

# num=10
#
# for i in range(2,num):
#     if num %i==0:
#         print(num,"the num is not prime")
#     else:
#         print(num,"the num is prime")



"""

"""
# num=int(input("enter the number:"))
# if num % 7==0 and num % 5==0:
#     print("the num is div by 7 and mul of 5")
# else:
#     print("the num is not div by 7 and mul of 5")

"""
to find a person can vote or not
"""
# age=int(input("enter your age:"))
# if age>=18:
#     print("you can vote")
# else:
#     print("you are a minor")

"""

"""
# sal=int(input("enter your sal:"))
# service=int(input("enter year of service:"))
# if service>5:
#     sal=sal+sal*(.050)
#     x=print("incrimented sal:",sal)
# else:
#     print("not eligible to get bonus")

"""

"""
# #
# colour= input("enter colour:")
#
# if colour=='green':
#     print("go")
# elif colour=='yellow':
#     print("wait")
# elif colour == 'red':
#     print("stop")
# else:
#     print("invalid")
#



# marks=int(input("enter your mark:"))
# if marks>=80:
#     print("A")
# elif marks>=70:
#     print("B")
# elif marks >= 60:
#     print("C")
# elif marks >= 50:
#     print("D")
# elif marks < 40:
#     print("F")
# else:
#     print("invalid")



"""
enter three values and find the greatest one
"""
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# if num1 >= num2 and num1 >= num3:
#     greatest = num1
# elif num2 >= num1 and num2 >= num3:
#     greatest = num2
# else:
#     greatest = num3
#
# print("The greatest number is:", greatest)

"""
check whether the number is palindrom or not
"""
# num=int(input("enter a number:"))
# reverse = int(str(num)[::-1])
# if num == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")


#fibonacci

# num=int(input("enter a number:"))
# n1,n2= 0,1
# for i in range(num):
#     print(n1, end=' ')
#     n3=n1+n2
#     n1=n2
#     n2=n3


#amstrong number

# num=int(input("enter a number:"))
# sum=0
# temp=num
# while temp>0:
#     n=temp%10
#     sum=sum+n*n*n
#     temp=temp//10
# if num==sum:
#     print(num,"amstrong")
# else:
#     print(num,"not amstrong")



#sum of odd and even numbers

# numbers=[3,6,7,5,11,8]
# x=0
# y=0
# for i in numbers:
#     if i%2==0:
#        x=x+i
#     else:
#         y=y+i
# print("sum of even numbers:",x)
# print("sum of odd numbers:",y)


"""
seperate odd and even numbers
"""
# n=int(input("enter a number:"))
# i=1
# x=[]
# y=[]
# while i<=n:
#     if i%2==0:
#         x.append(i)
#     else:
#         y.append(i)
#     i+=1
# print(x)
# print(y)

"""
WAP to check weather the two strings are anagram or not
"""
# str1 = input("enter first word")
# str2 = input("enter second word")
# x=len(str1)
# y=len(str2)
# if x==y:
#     str1=str1.lower()
#     str2=str2.lower()
#     str1==str2
#     print("the strings are anagram")
# else:
#     print("the strings are not anagram")

"""

"""
# year= int(input("enter a year:"))
#
# if year%400==0 or year % 4 and year//100 != 0:
#     print("not a leap year")
# else:
#     print("leap year")

"""
wap to  check wether a string is vowals ans consonants
"""
# chare = input("enter a string:")
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# if chare in vowels:
#     print(chare," is vowel")
# else:
#     print(chare,"is a consonants")
#

#it will print the numbers 1 to 10 in Ascending order
# i=1
# while i<=10:
#     print(i, end=' ')
#     i+=1
#
#it will print the numbers 10 to 1 in descending order
# i=10
# while i>1:
#     print(i,end=' ')
#     i-=1
#

# num = int(input("enter a number:"))
# sum=0
# i=1
# while i<=num:
#     sum+=i
#     i+=1
#     print(sum)


"""
diomond shape
"""
# n=int(input("enter a number:"))
# for i in range(n+1):
#     for j in range(n-i):
#         print("",end=' ')
#     for k in range(i):
#         print("*",end=' ')
#     print()
# for i in range(1,n):
#     for j in range(i):
#         print("",end=' ')
#     for k in range(n-i):
#         print("*",end=' ')
#     print()

#
# def print_diamond_pattern(n):
#     # Upper half of the diamond pattern
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "* " * i)
#
#     # Lower half of the diamond pattern
#     for i in range(n - 1, 0, -1):
#         print(" " * (n - i) + "* " * i)
#
#
# # Test the function
# num = int(input("Enter the number of rows for the diamond pattern: "))
#
# # Ensure the input is positive and odd
# if num > 0 and num % 2 != 0:
#     print_diamond_pattern(num)
# else:
#     print("Invalid input. Please enter a positive odd number.")


n=int(input("enter a number:"))
for i in range(n):
    for j in range(i):
        print("1",end=" ")
    for k in range(n-i):
        print("  *",end=" ")
    print()
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("  *",end=" ")
    print()