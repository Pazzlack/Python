#class definition
class Auto():
    #constructor       class Eigenschaften
    def __init__(self, name="",brand=""):
        self.name = name
        self.brand = brand
        if not self.name.__len__():
            self.name = "name is not set"
        if self.brand.__len__() ==0:
            self.brand = "brand is not set"
    
    def show(self):
        print (self.name)
        print (self.brand)