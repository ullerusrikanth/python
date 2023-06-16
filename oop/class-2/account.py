class Account:
    min_Bal =500
    
    
    def open_Account(self):
        print("Account opened successfully")
        
    def deposit_Account(self):
        print("amount deposited")
        
        
a1=Account()
a2=Account()
print(id(a1))
print(id(a2))
print(a1)