#
# """
# Write a code to reverse a number
# """
# num=int(input("enter the number to reverse"))
# rev=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)
#
#
# """
# write  code of greatest common divisor
# """
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# a=num1
# b=num2
# while b!=0:
#     temp=b
#     b=a%b
#     a=temp
#     gcd=a
# print("GCD of",num1,"and",num2,"is",gcd)
#
# """
# WAP to check weather the two strings are anagram or not
# """
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



#
# row=int(input("enter a number:"))
# for i in range(row+1,0,-1):
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()



"""
hollow diamomd pattern
"""
# n=int(input("enter a number:"))
# for i in range(n+1):
#     for j in range(n-1):
#         print(' ',end=' ')
#     print(i)
