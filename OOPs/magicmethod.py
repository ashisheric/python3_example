class Magicmethod:

    def __init__(self, data):
        self.data = data
        
    
    def __repr__(self):
        return str(self.data)

m = Magicmethod(["a", "b", "c"])
print(m.data)