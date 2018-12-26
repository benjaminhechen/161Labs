"""
Benjamin Chen
CSC161 Lab12 TR 1230-145
"""

class client:
    def __init__(self, id, pin, balance):
        self.id = id
        self.pin = int(pin)
        self.balance = int(balance)
    def get_id(self):
        return self.id
    def get_pin(self):
        return self.pin
    def set_pin(self, pin):
        self.pin = pin
    def get_balance(self):
        return self.balance
    def set_balance(self, bal):
        self.balance = bal

class bank:
    def __init__(self, accounts):
        self.accounts = accounts
    def get_accts(self):
        return self.accounts

def main():
    client1 = client('msklar', 1234, 100)
    client2 = client('lpacific', 4321, 100)
    client3 = client('sfischer', 5252, 100)
    client4 = client('bchen', 2525, 100)
    clients = [client1, client2, client3, client4]
    bank203 = bank(clients)
     
    userID = input("user ID? ")
    userPIN = eval(input("pin? "))
    
    for i in bank203.get_accts():
        if i.get_id() == userID:
            if i.get_pin() == userPIN:
                userAcct = i
                break
        userAcct = None
        
    if userAcct == None:
        print('incorrect login, exiting, error incoming')        
        
    print(userAcct.get_id())
    
    on = True
    while on:
        inpt2 = input("what would you like to do? type in: checkbalance, withdraw, deposit, done: ")
        if inpt2 == 'checkbalance':
            print('Balance: ', userAcct.get_balance())
        elif inpt2 == 'withdraw':
            inpt3 = eval(input('how much: '))
            userAcct.set_balance(userAcct.get_balance() - inpt3)
            print('New Balance: ', userAcct.get_balance())
        elif inpt2 == 'deposit':
            inpt3 = eval(input('how much: '))
            userAcct.set_balance(userAcct.get_balance() + inpt3)
            print('New Balance: ', userAcct.get_balance())
        elif inpt2 == 'done':
            print('have a nice day, exiting')
            on = False
        else:
            print('unrecognized input, exiting. have a nice day')
            on = False

main()


























