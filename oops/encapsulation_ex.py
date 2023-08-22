"""
wrappig the  data in a single unit

these three are the acess modifier
1.public
2.protect(_)
3.private(__)


"""
# class Bank:
#     def __init__(self,b_name,b_transaction):
#         self._name=b_name
#         self.__trans=b_transaction
#
#     def bank_info(self):
#         print("bank name:",self._name)
#         print("bank name:",self.__trans)
#
#
# class Customer(Bank):
#     def bank_tran(self):
#         print(self._name)
#         print(self.__trans)
#
# bank=Bank('SBI',123456789)
# bank.bank_info()
# obj1=Customer("SBI",123456789)
# obj1.bank_tran()

class Employee:
    def __init__(self,name,salary):
        self._name=name
        self.__salary=salary

    def get_info(self):
        print("employee name:",self._name)
        print("employee salary:",self.__salary)

class person(Employee):
    def emp(self):
        print(self._name)
        # print(self.__salary)

obj=person("sagil",45000)
obj.emp()
obj1=Employee("sarang",45000)
obj1.get_info()