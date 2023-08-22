import csv
import os

class HR:
    def __init__(self,name,age,role,salary):
        self.name=name
        self.age=age
        self.role=role
        self.__salary=salary
        self.password="password"

    def insert(self):
        exist_file=os.path.exists('empdata.csv')
        with open('empdata.csv','a')as file:
            headers=['name','age','role','salary']
            emp=csv.DictWriter(file,fieldnames=headers)
            if not exist_file:
                emp.writeheader()
            emp = csv.writer(file)
            emp.writerow([self.name,self.age,self.role,self.__salary])
            file.close()
            print("insertion succussfully")

    # def update(self):


    # def emp_details(self):
    #     print("employee name :",self.name)
    #     print("employee age :",self.age)
    #     print("employee role :",self.role)
    #     print("employee salary :",self.__salary)

# class Employee(HR):
#     def login(self):
#         username=input("enter username :")
#         password=input("enter username :")
#         if username==self.name and password==self.password:
#             print("login succussfully")
#             print("name :", self.name)
#             print("age :", self.age)
#             print("role :", self.role)
#             print("salary :", self.__salary)
#         else:
#             print("incorrect username or password")

obj=HR('sarang',23,'devp',20000)
obj.insert()