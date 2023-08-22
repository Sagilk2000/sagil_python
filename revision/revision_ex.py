import os

# with open('samp.txt','w')as file:
#     file.write('hii dears how are you ')
#     file.close()

# with open('samp.txt','r')as file:
#     x=file.readlines()
#     print(x)
#     file.close()

with open('samp.txt','r')as file:
    x=file.readlines()
    # print(x)
    # x.pop(0)
    # print(x)
n=int(input("enter the line number to delete:"))
for i in  x:
    y=x.pop(n)
    print(y)


