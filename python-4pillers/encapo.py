class Test:
    __a = 100
    _b=200
    c=300
    d=500
    
    
    def __init_(self):
        print(self.__a)
        print(self._b)
        print(self.c)
        print(self.d)
        
    def get_data(self):
        return self.__a
        
        
t =Test()
print(t.d)
print(t.c)
print(t._b)
print(t.get_data())