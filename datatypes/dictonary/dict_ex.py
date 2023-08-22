"""
#dictionary

.indexed
.mutable
.ordered
.not allow duplicates
. key value pairs

"""
# dict1={"name":"priya","age":"24","place":"kannur"}
# print(dict1["age"])
# print(dict1["name"])
# print(dict1.get("place"))
# dict1.update({"qualification":"bsc","course":"python"})
# print(dict1)
# print(dict1.keys())
# print(dict1.values())


#zip function

# dict_keys=(['name', 'age', 'place', 'qualification', 'course'])
# print(type(dict_keys))
# dict_values=(['priya', '24', 'kannur', 'bsc', 'python'])
# print(type(dict_keys))
# print(dict(zip(dict_keys,dict_values)))


# dict1={'name': 'priya', 'age': '24', 'place': 'kannur', 'qualification': 'bsc', 'course': 'python'}
# dict1.pop("age")
# dict1.pop("course")
# print(dict1)

#fromkeys
# x=('key1','key2','key3')
# y=1
# z= dict.fromkeys(x,y)
# print(z)

#setdefault
# car={"name":"alto","model":"800","year":"2018"}
# x= car.setdefault("model","new")
# y= car.setdefault("colour","grey")
# car["name"]="new"
# print(car)

# num=int(input("enter a number:"))
# a = {}
# for i in range(1,num+1):
#     a.setdefault(i,i*1)
# print(a)

# num=int(input("enter a number:"))
# a =dict()
# for i in range(1,num+1):
#     a[i]=i*i
# print(a)

# sampledict={"class":{
#     "student":{
#         "name":"sagil",
#         "course":{
#             "python":2023,
#             "angular":2028,
#         "marks":{
#             "physics":70,
#             "english":80
#         }
#         }
#     }
# }
# }
# print(sampledict['class']['student']['course']['angular'])
#

# sample_dict = {
#     'dict1':{"name": "priya", "age":24, "place": "kannur"},
#     'dict2':{"nam": "sagil", "ag":25, "plce":"kozhikode"},
#     'dict3':{"per": "sarang", "ae":22, "plac":"wayanad"}
# }
# print(sample_dict)
# x=sample_dict['dict2']['plce']="palakkad"
# print(sample_dict)


#
# dict1={"name": "priya", "age":24, "place": "kannur"}
# dict2={"nam": "sagil", "ag":25, "plce":"kozhikode"}
# print(list(dict1))
# print(list(dict2))

#
# dict_1={"name": "priya", "age":24, "place": "python"}
# print(dict_1)
# dict_1["sthalam"]=dict_1.pop('place')
# print(dict_1)
#
#
#
# dictt ={"name":"sarand","age":25,"qualification":"degree"}
# print(dictt)
# dictt["education"]=dictt.pop("qualification")
# print(dictt)
"""
writw a program which accept a sequence of comma-seperated numbers from a console and generate a list and tuple
"""
# Accept comma-separated numbers from the console
# numbers = input("Enter a sequence of comma-separated numbers: ")
#
# # Split the input by commas and convert each element to an integer
# number_list = [int(num) for num in numbers.split(",")]
#
# # Create a tuple from the list
# number_tuple = tuple(number_list)
#
# # Display the list and tuple
# print("List:", number_list)
# print("Tuple:", number_tuple)


from math import sqrt
# c=50
# h=30
# x=[]
# a=list(map(int,(input("enter the num:").split())))
# for i in a:
#     q=sqrt((2*c*i)/h)
#     x.append(int(q))
# print(tuple(x))

#
# a=list(map(str,(input("enter the words:").split())))
# a.sort()
# b=print(','.join(a))

# a=input("enter the words:").split()
# b=sorted(list(set(a)))
# print(b)


# x = int(input("Enter the number of rows :"))
# y = int(input("Enter the number of columns :"))
# a=[[i*j for j in range(y)] for i in range(x)]
# print(a)

# x =input("Enter somthing:")
# a=x.upper()
# print(a)
x=[]
for i in range(2000,3001):
    a=i
    print(a,end=",")


