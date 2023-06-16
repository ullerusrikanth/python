class account:
    def __init__(self,id,name,amount):
        self.id =id
        self.name = name
        self.amount =amount
    def get_account_info(self):
        self.email = "srikanth@mp.com"
        
        
a1 = account(101,"rahul",60000)
a1.get_account_info()
a1.loc = "wayanad"

print(a1.__dict__)