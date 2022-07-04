
import pickle

from scratch.bank_account import BankAccount


def print_homepage():
    '''
    Function to print home page for courses app
    '''
    print("="*40)
    print("1. Open an account")
    print("2. Deposit")
    print("3. Wtihdraw")
    print("4. Show balance")
    print("5. Show transactions")
    print("6. Exit")
    print("="*40)
    user_choice = input("Enter a number choose your option: ")
    return user_choice




################# Main Program ####################

user_choice = 0
bank_info = {}
with open("my-bank.py", "wb") as my_bank:
        for line in bank_info:
            pickle.dump(line, bank_info)
            print(line)
while user_choice != '6':

    user_choice = print_homepage()
    

    if user_choice == '1':

        user_info = BankAccount(input("Enter your name: "), int(input("Enter your initial balance: ")))
        account_number = int(input("Enter a 4 digit account number: "))
        bank_info[account_number] = user_info
        
        print("Account number: ", account_number)#'\n', bank_info[account_number])
        print(bank_info[account_number])
    
    elif user_choice == '2':
        user_info.deposit(500) #this is a place holder, user enters amount
        
    elif user_choice == '3':
        user_info.withdraw(1) #placeholder, user enters amount

    elif user_choice == '4':
        print(bank_info[account_number])
        
    elif user_choice == '5':
        #user_info.show_transactions()
        print(user_info.transactions)
    elif user_choice != '6':
        print("Please enter a correct option ")

print("Thank you, have a nice day")


with open("my-bank.py", "wb") as my_bank:
    pickle.dump(bank_info, my_bank)
    print(user_info)




































































