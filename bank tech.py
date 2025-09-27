# bank
# cust object
class customer:
    def __init__(self, name, account_num=int, balence=int):
        self.name = name
        self.account = account_num
        self.balence=balence
        self.bank_name= 'SBI'
    def details(self):
        return f'Name: {self.name}, Account type: {self.account}, Balence: {self.balence}'
    def amount_withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount<=99:
            print("the Amount Withdraw should be atlest 100")
        else:
            print("Your Transaction is proceed")
            self.Availabel_amount = self.balence - self.withdraw_amount
            print(f'Hello {self.name} a/c:{self.account} the Amount Credited Rs:{self.withdraw_amount}')
            print(f'the available balance: {self.Availabel_amount}')
        
    def amount_deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        if self.deposit_amount<=99:
            print("the Amount Deposit should be atlest 100")
        else:
            print("Your Transaction is proceed")
            self.Availabel_amount = self.balence + self.deposit_amount
            print(f'Hello {self.name} a/c:{self.account} the Amount Credited Rs:{self.deposit_amount}')
            print(f'the available balance: {self.Availabel_amount}')
            
        

c1 = customer('sai', 1245 , 1000)
print(c1.amount_withdraw(20))

        
