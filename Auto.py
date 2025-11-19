from Database import Database

#class definition
class Auto(Database):
    #constructor       class Eigenschaften
    def __init__(self, name="",brand="", sql_query=""):
        self.sql_query = sql_query
        super().__init__(self.sql_query)
        self.name = name
        self.brand = brand
        if not self.name.__len__():
            self.name = "name is not set"
        if not self.brand.__len__():
            self.brand = "brand is not set"
    
    def show(self):
        print (self.name)
        print (self.brand)