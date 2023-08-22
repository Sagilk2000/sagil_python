class HR:
    def __init__(self,name,age,role,salary):
        self.name=name
        self.age=age
        self.role=role
        self.__salary=salary
        self.password="password"

    def emp_details(self):
        print("employee name :",self.name)
        print("employee age :",self.age)
        print("employee role :",self.role)
        print("employee salary :",self.__salary)

class Employee(HR):
    def login(self):
        username=input("enter username :")
        password=input("enter username :")
        if username==self.name and password==self.password:
            print("login succussfully")
            print("name :", self.name)
            print("age :", self.age)
            print("role :", self.role)
            print("salary :", self.__salary)
        else:
            print("incorrect username or password")

#
# obj=HR("sagil",23,"junior developer",2000)
# obj.emp_details()
obj1=Employee("sagil",23,"junior developer",2000)
obj1.login()


