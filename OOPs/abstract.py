#This code snippet talks about Abstract Base Classes (abc).
# The `abc` module provides features to create Abstract Base Classes.

# To create an Abstract Base Class, set the `__metaclass__` magic method
# to `abc.ABCMeta`. This will mark the respective class as an Abstract Base Class.

# Now, in order to specify the methods which are to be enforced on the
# child classes, ie.. to create Abstract Methods, we use the decorator 
# @abc.abstractmethod on the methods we need.

# The child class which inherits from an Abstract Base Class can implement
# methods of their own, but should always implement the methods defined in the parent ABC Class.

import abc

class MyABCclass:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def setData(self, val):
        return

    @abc.abstractmethod
    def getData(self):
        return

# Abstract Base Class defined above ^^^
# Custom class inheriting from the above Abstract Base Class, below

class MyClass(MyABCclass):
    def setData(self, input):
        self.val = input
    
    def getData(self):
        print("\nCalling the get_val() method")
        print("I'm part of the Abstract Methods defined in MyABCclass()")
        print(self.val)
    
    def hello(self):
        print("\nCalling the hello() method")
        print("not part of the Abstract Methods defined in MyABCclass()")

my_class = MyClass()
my_class.setData(100)
my_class.getData()
my_class.hello()