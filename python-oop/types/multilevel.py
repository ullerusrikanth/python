class grandparent:
    def m1(self):
        print("grandparent class -m1() method")
        
class parent(grandparent):
    def m2(self):
        print("parent class -m2() method")
        
        
        
class child(parent):
    def m3(self):
        print("child class -m3() method")
        
obj=child()
obj.m1()
obj.m2()
obj.m3()