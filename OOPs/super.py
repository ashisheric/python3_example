class Parent:
    def displayItem(self):
        print("this is parent display item")

class Child(Parent):
    def __init__(self, name):
        super(Child, self).displayItem()
        self.name = name

    def childName(self):
        return self.name

c = Child("ashish")
print(c.childName())
#print(c)