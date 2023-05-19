# creating decorator
def login_required(func):
    def inner(name, is_login):
        if is_login == False:
            print("boys please login")
        
        else:
            return func(name, is_login)
        
        
        
    return inner


@login_required
def home_page(name, is_login):
    print("home page")
    
    
home_page("srikanth", True)
home_page("kanna", False)