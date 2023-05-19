def verifysecondvalue(func):
    def inner(a,b):
        if b == 0:
            print("cant divide by zero")
        else:
            return func(a,b)
    return inner




@verifysecondvalue
def calc(a,b):
    return a/b



print(calc(10,5))
print(calc(10,0))
