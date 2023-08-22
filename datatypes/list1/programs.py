# """
# *sum all the items in a list
# my_list =[1,2,3,4,5]
#
# """
# my_list =[1,2,3,4,5]
# sum=0
# for i in my_list:
#     sum=sum+i
#     print(sum)

# my_list =[1,2,3,4,5]
# sum=1
# for i in my_list:
#     sum*=i
#     print(sum)
#
# my_list =[1,2,3,4,5]
# sum=1
# for i in my_list:
#     sum=sum-i
#     print(sum)
#
# my_list =[1,2,3,4,5]
# sum=1
# for i in my_list:
#     sum=sum/i
#     print(sum)
#
#
# """
# write a program to convert a list of charecter into a string
# s = ['p','y','t','h','o','n']
# """
# s = ['p','y','t','h','o','n']
# x=''
# for i in s:
#    x=x+i
# print(x)
# s = ['D','j','a','n','g','o']
# x=''
# for i in s:
#     x=x+i
# print(x)

#
#
# name="sarun"
# x=name[1:]
# for i in x:
#     print(i)


# num=[1,5,6,-5,-2,-1,9,0]
# x=[]
# y=[]
# z=[]
# for i in num:
#     if i>0:
#         x.append(i)
#         print(x)
#     elif i==0:
#         z.append(i)
#         print(z)
#     else:
#         y.append(i)
#         print(y)
#
#
# my_list =[9,1,23,54,5]
# print(max(my_list))
# my_list.sort(reverse=True)
# print(my_list)
# max=my_list[0]
# for i in my_list:
#     if max<=i:
#         max=i
# print(max)

# def fibonacci(n):
#     fib_seq = [0, 1]  # Initialize the sequence with the first two numbers
#
#     for i in range(2, n):
#         next_num = fib_seq[i - 1] + fib_seq[i - 2]
#         fib_seq.append(next_num)
#
#     return fib_seq
#
# # Example usage
# n = 10  # Generate the first 10 Fibonacci numbers
# sequence = fibonacci(n)
# print(sequence)

"""
write a to find common number from two lists
list1= [1,6,8,7,9]
list2= [2,6,7,1,9]
"""
# list1= [1,6,8,7,9]
# list2= [2,6,7,1]
# newlist=[]
# list3=[]
# for i in list1:
#     for j in list2:
#         if i==j and i not in newlist:
#             newlist.append(i)
#         else:
#             list3.append(i)
# print(list3)
# print(newlist)

#take even numbers
#
# list1= [1,6,8,7,9]
# list2= [2,6,7,1]
# x=[]
# for i in list1:
#     if(i%2==0):
#         x.append(i)
#         print(x)

"""
write a program to remove same items in a list
list=["apple","mango","mango","grape","pineapplle","grape"]
"""
# list = ["apple","mango","mango","grape","pineapplle","grape"]
# x = []
# for i in list:
#     if i not in x:
#         x.append(i)
# print(x)

# a=["www.zframes.com","www.wikipedia.com","www.asp.net"]
# x=[]
# for i in a:
#     print(i)
#     suffix = i.split(".")[-1]
#     x.append(suffix)
# print(x)



