class Test:
    @classmethod
    def m2(cls):
        cls.c = 200
        Test.d = 400
        
t1 = Test()
t2 = Test()
Test.m2()
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)



"""class Test:
    @classmethod
    def m1(cls):
        cls.a =100
        Test.b=200
        
        @classmethod
        def m2(cls):
            cls.a=111
            Test.b=222

        
t1 =Test()
t2 =Test()
Test.m1
Test.m2
print(Test.__dict__)
print(t1.__dict__)
print(t2.__dict__)"""


