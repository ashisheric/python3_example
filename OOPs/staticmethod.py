"""
# 1) Static methods are functions methods which doesn’t need a binding to a class or an instance.
# 2) Static methods, as well as Class methods, don’t require an instance to be called.
# 3) Static methods doesn’t need  self or cls as the first argument since it’s not bound to an instance 
# or class.
# 4) Static methods are normal functions, but within a class.
# 5) Static methods are defined with the keyword @staticmethod above the function/method.
# 6) Static methods are usually used to work on Class Attributes.
"""
class Static():

    def __init__(self, data):
        print("Instance is created for Static class")
        self.data = data
        print(f"Without Static method name {self.data}")

    @staticmethod
    def static(data):
        print(f"the name of static fucntion is {data}")

    @classmethod
    def classMethod(cls, data):
        print(f"inside classmethos and value is {data}")

s = Static("NO staticMethod")
Static.static("Staticmethod")
Static.classMethod("classMethod")