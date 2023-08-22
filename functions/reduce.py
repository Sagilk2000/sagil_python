"""
reduce(function,iterable)
"""

from functools import reduce
# list1=[1,3,5,6]
# product=1
# for i in list1:
#     product=product*i
# print(product)


# list2=[1,3,5,6]
# product= reduce((lambda x,y:x*y ),list2)
# print(product)
#
# num=int(input("enter a number"))
# sum=reduce(lambda x,y:x+y,range(num+1))
# print(sum)

num=int(input("enter a number:"))
sum=reduce(lambda x,y:x*y,range(1,num+1))
print(sum)

