class Database():
    def __init__(self, sql_query=""):
        self.sql_query = sql_query
        if not self.sql_query.__len__():
            print ("sql_query is not set")
    
    def __connect(self):
        print ("I am private function and i try to connect to db")
    
    def insert(self):
        self.__connect()
        print(f"i will give { self.sql_query } to db")

    def delete(self):
        self.__connect()
        print(f"i will give { self.sql_query } to db")

    def update(self):
        self.__connect()
        print(f"i will give { self.sql_query } to db")
    
    def select(self):
        self.__connect()
        print(f"i will give { self.sql_query } to db")