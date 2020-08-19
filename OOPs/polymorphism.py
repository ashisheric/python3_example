#Polymorphism means having the same interface/attributes in different classes.
    
class Persons:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print(self.name)

class Male(Persons):
    def showDetails(self):
        print("this is male")


class Female(Persons):
    def showDetails(self):
        print("this is female")
    
for a in (Male("testMale"), Female("testFemale"), Male("testMale2"), Female("testFemale2")):
    a.getName()