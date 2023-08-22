"""Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line"""
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i)

"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""
# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

"""With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
# num=int(input("enter a number :"))
# dict1={}
# for i in range(1,num+1):
#     dict1.setdefault(i,i*i)
# print(dict1)

"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""
# num=(list(input("enter numbers:").split()))
# print(num)
# print(tuple(num))

'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods'''


# class StringManipulator:
#     def __init__(self):
#         self.string = ""
#
#     def getString(self):
#         self.string = input("Enter a string: ")
#
#     def printString(self):
#         print(self.string.upper())
#
#
# def testStringManipulator():
#     # Create an instance of StringManipulator
#     sm = StringManipulator()
#
#     # Test getString() and printString() methods
#     sm.getString()
#     sm.printString()
#
#     # Testing the class methods
#
#
# testStringManipulator()

# stri=input("enter something:")
# x=stri.upper()
# print(x)

'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''
# from math import sqrt
# n=list(map(int,(input("enter numbers:")).split()))
# c=50
# h=30
# a=[]
# for i in n:
#     q=sqrt((2*c*i)/h)
#     a.append(int(q))
# print(tuple(a))

'''Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'''
# x=int(input("enter no of rows:"))
# y=int(input("enter no of coloums:"))
# a=[[i*j for j in range(y)]for i in range(x)]
# print(a)
a=[]
def up(x):
    def lp(y):
        for i in range(y+1):
            for j in range(x+1):
                a=i*j
            print(a)
up(5)(5)
