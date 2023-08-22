"""
filter (function,iterable)
"""
# num = [-3,-7,5,6]
# lessthanzero=list(filter(lambda x:x<0,num))
# print(lessthanzero)
# greater=list(filter(lambda y:y>0,num))
# print(greater)


list3=[2,5,8,3]
even=list(filter(lambda x:x%2==0,list3))
print(even)
odd=list(filter(lambda x:x%2!=0,list3))
print(odd)

num = [-3,-7,5,6]
def even(num):
    even_num=[]
    for i in num:
        if i%2==0:
            even_num.append(i)
        return even_num
even(num)