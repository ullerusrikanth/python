def smart_div(func):
    def inner(a,b):
        if b == 0:
            print("cant divibe by zero")
            
        else:
            return func(a,b)
    return inner


def calc(a,b):
    return a/b
    
    
d = smart_div(calc)


print(d(10,5))
print(d(10,0))