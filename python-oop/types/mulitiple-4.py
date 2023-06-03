class parent1:
    def m1(self):
        print("parent1 class -m1() method")
        
    def m2(self):
        print("parent1 class -m2()meythod")
        
        
    def m3(self):
        print("parent1 class -m3()method")
        
        
class parent2:
    def m1(self):
        print("parent2 class -m1()method")
        
    def m2(self):
        print("parent2 class -m2()method")
                
class child(parent1,parent2):
    def m4(self):
        print("child class -m4()method")
        
        
obj=child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()