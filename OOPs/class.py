class Dummy:
    # __new__ call at class level i.e at the time of object creation 
    def __new__(cls, data):
        print(f"new is call {data}")

    # __init__ call once instance is create
    def __init__(self, data):
        self.data = data
        print(f"init is call {self.data}")
        print("I'm call") # it call when create a constructor

print(Dummy("ash")) # At the time of object create
d = Dummy("hi") # Instance of class is created and self is reference of current object
print(type(d)) # d is object of class type Dummy
print(type(Dummy)) # class type object 