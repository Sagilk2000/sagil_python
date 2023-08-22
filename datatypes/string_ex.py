"""
sting
#immutable datatype
#ordered
#set of charecters
"""

#str1 = "hello world"
#string indexing
# print(str1[0])
# print(str1[10])
# print(str1[-1])

#strig slicing
# print(str1[0:5])
# print(str1[6:11])
# print(str1[::-1])
# print(str1[:-6:-1])
# print(str1[-7:-12:-1])


#string methods

# str1 = "hello world"
#
# print(str1.upper())
# print(str1.lower())
# print(str1.encode())
# print(str1.__str__())
# print(str1.capitalize())
#
# nam = "sagii sarang"
# b = nam.find("sarang")
# print(b)
# print(nam.split())
#
#
# nam =["sagil","sarang"]
# x = "#".join(nam)
# print(x)


# name='hello world'
# print(name.split())


# name=(2,'sagil',30,'sarang')
# print(name)

# str2='sagil kottapally'
# print(str2[0])
# print(str2[6])
# print(str2[:-1])
# print(str2[::-1])
# print(str2[5:16])
# print(str2[0:5])
# print(str2[:5:-1])
# print(str2[5::-1])

#
# s1='sarang'
# s2='sarath'

# print(len(s1))
# print(len(s2))

# x =(s1[:3]+s2+s1[3:])
# print(x)
#
# y=(s1[0]+s2[0]+s1[2]+s2[3]+s1[-1]+s2[-1])
# print(y)


# frst_char = s1[0]+s2[0]
# mid_char1= s1[int(len(s1)/2)]
# mid_char2= s2[int(len(s2)/2)]
# mid_char= mid_char1+mid_char2
# last_char= s1[-1]+s2[-1]
# op=frst_char+mid_char+last_char
# print(op)
#


str1 = "hi sagil"
x = (list(str1))
print(x)
print(type(x))
y = "".join(x)
print(y)
print(type(y))

