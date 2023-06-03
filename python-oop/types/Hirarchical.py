class parent:
    def m1(self):
        print("parent class -m1()method ")
        
    def m2(self):
        print("parent class -m2() method")
        
        
class child1(parent):
    def m3(self):
        print("child1 class -m3() method")
        
class child2(parent):
    def m4(self):
        print("child2 class -m4() method")
        
obj1=child1()
obj1.m1()
obj1.m2()
obj1.m3()
#obj1.m4() -child1 -object has no attribut m4
obj2=child2()
obj2.m1()
obj2.m2()
#obj2.m3() -child2 object has no attribute m3
obj2.m4()
        

        
        
