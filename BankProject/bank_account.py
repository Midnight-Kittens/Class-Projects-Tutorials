 

'''
Class that defines a bank account object
'''
class BankAccount:

    '''
    Function to initialize the objects attributes
    '''
    def __init__(self, name,balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
        
    '''
    Function to represent the class's object as a human readable string
    '''
    def __str__(self) -> str:
         return f"Account Name: {self.name}\n \tInitial Balance: {self.balance}\n"
    
    '''
    Function to deposit a new amount to the balance variable 
    Appends the deposit to the transactions list to keep a running log
    '''
    def deposit(self, amount):
        amount = int(input("Enter an amount to deposit: "))
        if amount > 0:
            self.balance += amount
            self.transactions.append(self.balance)
            self.show_balance()
        else:
            print("Error: must pick an amount to deposit")

    '''
    Function to withdraw an amount from the balance
    Appends the withdrawal to the transaction list to keep a running log
    '''
    def withdraw(self, amount):
        amount = int(input("Enter an amount to withdraw: "))
        
        if amount > self.balance:
            print("Error: Insufficient funds")
        else:
            self.balance -= amount
            self.transactions.append(self.balance)
            self.show_balance()            


    '''
    Prints the balance of the objects attribute 'balance'
    '''    
    def show_balance(self):
        print(f"Balance = {self.balance}")

    '''
    Prints a running log of the withdrawals and deposits associated with the account
    '''
    def show_transactions(self,):
        print(self.transactions)

















































































