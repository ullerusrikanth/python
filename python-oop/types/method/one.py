class Test:
    def m1(self):
        self.a = 100
        self.b = 200
        
t1 = Test()
t2 = Test()
t1.m1()
t2.m1()

print(t1.__dict__)
print(t2.__dict__)



"""class Test:
    
    def m1(self):
        self.a =100
        self.b =200
        
    def m2(self):
        self.A = 444
        self.B =555
        
        
t1 = Test()
t2 = Test()
t1.m1()
t2.m2()


print(t1.__dict__)
print(t2.__dict__)"""



"""class Test:
    def m1(self):
        self.a=100
        self.b=200
        self.c=300
        self.d=400
        
    def m2(self):
        self.A = 111
        self.B = 222
        self.C = 333
        self.D = 444
        
t1 = Test()
t2 = Test()

t1.m1()
t2.m2()"""

print(t1.__dict__)
print(t2.__dict__)