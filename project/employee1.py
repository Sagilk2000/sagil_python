import csv

class HR:
    def __init__(self):
        self.username="username"
        self.password = "password"
        self.employees = []
        self.headers = ['Employee Name', 'Department', 'Place', 'Salary']

    def add_employee(self, name, department, place,__salary):
        self.employees.append([name, department, place,__salary])

    def savecsv(self):
        with open('empdata.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)
            writer.writerows(self.employees)

    def update(self):
        with open('empdata.csv',mode='r')as file:
            reader= csv.reader(file)
            print(reader)


    



obj=HR()
# obj.add_employee("sagil","cs","pallor",25000)
# obj.savecsv('empdata.csv')
obj.update()