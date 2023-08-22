"""
diamond shape pattern
"""
n = int(input("enter a value:"))#5
for i in range(n+1):#no of rows
    for j in range(n-i):
        print("1",end=" ")
    for k in range(i):
        print(" * ",end=" ")
    print()
# for i in range(1,n+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(" * ",end=" ")
#
#     print()


"""
reverse number pattern
"""
# n = int(input("enter a value:"))
# for i in range(n+1,0,-1):
#     for j in range(i-1,0,-1):
#         print(j,end=" ")
#     print()

"""
number pattern
"""
# n = int(input("enter a value:"))
# for i in range(n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i):
#         print(k,end="   ")
#     print()
#reverse
# n = int(input("enter a value:"))
# for i in range(n+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(1,n-i):
#         print(k,end="   ")
#     print()

"""
number pattern model2
"""
# n = int(input("enter a value:"))
# for i in range(n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print(i,end="   ")
#     print()



# #reverse
# n = int(input("enter a value:"))
# for i in range(n+1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(n-i,end="   ")
#     print()

"""
*filled x pattern
"""

# n=int(input("enter the value:"))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print(" * ",end=" ")
#     print()
# for i in range(2,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print(" * ",end=" ")
#     print()
#

"""
To create a hollow diamond pattern
"""

# n=int(input("Enter the number of rows for the hollow diamond pattern: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print("1", end="")
#     for j in range(1, (2 * i)):
#         if j == 1 or j == (2 * i - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, (2 * i)):
#         if j == 1 or j == (2 * i - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

"""
hollow diamond diagram
"""
#not completed
# for row in range(9):
#     for col in range(9):
#         if (row+col==4 and row-col==4) or (row+col==12 and col-row==4):
#             print(" * ",end=" ")
#         else:
#             print(" ", end=" ")
#     print()
"""
WAP to find the largest element in a list.
WAP to remove duplicates from a list.
WAP to find the index of an element in a list.
WAP to find the intersection of two lists.
WAP to  
5   5   5   5   5   
  4   4   4   4   
    3   3   3   
      2   2   
        1 

"""

"""
heart shape pattern
"""
# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")
#     print()




# n=int(input("enter the range:"))
# k=1
# for i in range(n+1):
#     for j in range(i):
#         print(j,end=" ")
#     print()

"""
charecter pattern
"""
# for i in range(65,91):
#     print(chr(i),end=" ")


# n=int(input("enter the range:"))
# k=1
# for i in range(n+1):
#     for j in range(i):
#         x=chr(64 + k)
#         print(x, end=" ")
#         k+= 1
#     print()
#
#
# n=int(input("enter the range:"))
# for i in range(65,65+n):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

