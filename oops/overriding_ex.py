class Animal:
    def __init__(self,name):
        self.name=name

    def breath(self):
        print("i breath oxygen")

    def food(self):
        print("1 eat food")

class Dog(Animal):
    def food(self):
        print("2 eat  food")


obj=Dog("maika")
obj.food()
obj.breath()