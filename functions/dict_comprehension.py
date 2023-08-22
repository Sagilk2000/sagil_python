"""
dictionary comprehension

expression,loop,condition

"""

# s={}
# for num in range(1,11):
#     s[num]=num*num
# print(s)
#
#
# #using dictionary comprehension
#
# s={num:num*num for num in range(1,11)}
# print(s)
#
# su={num:num*num for num in range(1,11) if num%2==0}
# print(su)
#
# old={"milk":1.02,"coffee":25,"bread":2.5}
# add=0.76
# new={key:value*add for (key,value)in old.items()}
# print(new)
#
# # name={'sagil':22,'sarang':23,'karthik':25,'ajveed':21}
# # s={k:(''v for (k,v)}
#
# keys=['a','b','c','d','e']
# values=[1,2,3,4,5]
# name={key:value for(key,value)in zip(keys,values)}
# print(name)
#
# x={k: ('even' if k % 2 == 0 else 'odd') for k in range(1,11)}
# print(x)
# #
# s={}
# k=['a','b','c','d','e','f','g','h']
# x={k[i]:k[i+1] for i in range(0,len(k),2)}
# print(x)
#
#
# n=[]
# m=[]
# k=['a','b','c','d','e','f']
# for i in range(0,len(k),2):
#     n.append(k[i])
# for j in range(1,len(k),2):
#     m.append(k[j])
# print(dict(zip(n,m)))
#
# #using list comprehension
# a=[]
# b=[]
# k=['a','b','c','d','e','f']
# for i in range(0,len(k),2):
#     a.append(k[i])
# for j in range(1,len(k),2):
#     b.append(k[j])
# print(dict(zip(a,b)))
#
#
#
