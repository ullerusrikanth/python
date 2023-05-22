a = 10   #a is global scope

def m1():
    b = 20 # local varible
    print(a)
    print(b)
    
def m2():
    print(a)
    #print(b)
    
def m3():
    print(a)
    

m1()
m2()
m3()
    
    