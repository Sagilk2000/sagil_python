"""7----------------------------------------------------------------------------------"""

# num=ord("B")-ord("A")
# for i in range(num,ord("e")):
#     print(i)
"""2----------------------------------------------------------------------------------"""

# s=input("enter somthing:")
# print(type(s))
# c=s.split()
# print(c)
# x=[]
# for i in c:
#     if i in x:
#         continue
#     else:
#         i=i[::-1]
#         x.append(i)
# print(" ".join(x))

"""4----------------------------------------------------------------------------------"""
# s = "1982376455"
# odd = []
# even=[]
# x=(list(s))
# for i in x:
#     if int(i) % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# # print(odd)
# # print(even)
# odd.sort()
# # print(odd)
# even.sort(reverse=True)
# # print(even)
# a=odd+even
# print(a)
# # b=(str(a))
# # print(b)
# b=''.join(a)
# print(b)

"""9----------------------------------------------------------------------------------"""
# n=[5,2,1,9]
# print(type(n))
# n.sort(reverse=True)
# print(n)
# b = "".join(n)
# print(b)

# n = [50, 2, 19, 9]
# sorted_n = sorted(map(str, n), reverse=True, key=lambda x: x*3)
# largest_number = int(''.join(sorted_n))
# print(largest_number)



# num = int(input("enter a number:"))
# rev = ""
# while num > 0:
#     rem = num % 10
#     rev =rev+str(rem)
#     num = num // 10
# print(rev)

# num = [25,45,6,58,90]
# g=[0]
# for i in num:
#     if num > 0:
#         g.append(i)
# print(g)

"""
string = "123" to 123
"""
# str1 = "586"
# result=0
# for i in str1:
#     x=ord(i)-ord('0')
#     result=result*10+x
# print(result)


#list comprhensive method

# list1=[2,5,4,8,9]
# even=[i for i in list1 if i%2==0]
# print(even)
# odd=[j for j in list1 if j%2!=0]
# print(odd)
#

# list_items = ["apple", "ornge", "grpe", "musambi", "stawberry"]
# list1 = [i for i in list_items if 'a' in i]
# print(list1)
# list2 = [i for i in list_items if 'a' not in i]
# print(list2)

# list = [i for i in range(10) if i<5 ]
# print(list)
# list1 = [i for i in range(10) if i>5 and i<=10]
# print(list1)






