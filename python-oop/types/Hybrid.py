class grandparent1:
    def m1(self):
        print("grandparent1 class -m1() method")
        
class grandparent2:
    def m2(self):
        print("grantparent2 class -m2() method")
        
class parent(grandparent1,grandparent2):
    def m3(self):
        print("parent class -m3() method")
        
class child1(parent):
    def m4(self):
        print("child1 class -m4() method")
        
class child2(parent):
    def m5(self):
        print("child2 class -m5()method")
        
obj1=child1()
obj1.m1()
obj1.m2()
obj1.m3()
obj1.m4()
obj2 = child2()
obj2.m1()
obj2.m2()
obj2.m3()
obj2.m5()
        
        