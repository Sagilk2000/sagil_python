class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def get_details(self):
        print("book title:",self.title)
        print("author name:",self.author)
        print("book price:",self.price)

class Fiction(Book):
    def __init__(self,title,author,price,genre):
        super().__init__(title,author,price)
        self.genre=genre

    def get_details(self):
        fdeatail=super().get_details()
        print(fdeatail,"genre:",self.genre)


class NonFiction(Book):
    def __init__(self,title,author,price,topic):
        super().__init__(title,author,price)
        self.topic=topic

    def get_details(self):
        nfdetail=super().get_details()
        print(nfdetail,"topic:",self.topic)



class Poetry(Book):
    def __init__(self,title,author,price,style):
        super().__init__(title,author,price)
        self.style=style

    def get_details(self):
        pbook=super().get_details()
        print(pbook,"style:",self.style)

obj=Book("alchimist","jhon",2005.5)
obj.get_details()
obj1=Fiction("scorpion","alex",105.5,"poem")
obj1.get_details()
obj2=NonFiction("death","david",555.5,"thriller")
obj2.get_details()
obj3=Poetry("charanmar","joseph",570.,"fantasy")
obj3.get_details()


