#!/usr/bin/env python3.6
from account import Account
from records import details

def create_account(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name,user_name,password,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()    

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()    


def find_account(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Account.find_by_name(name)    

def check_existing_accounts(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Account.account_exist(name)    

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()  
 #_________________________________________details____________________________________________________________________


def create_details(details_name,usr_name,password,email):
    '''
    Function to create a new account
    '''
    new_details = details(details_name,usr_name,password,email)
    return new_details

def save_details(details):
    '''
    Function to save account
    '''
    details.save_details()    

def del_details(details):
    '''
    Function to delete a account
    '''
    details.delete_details()    


def find_details(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return details.find_by_name(name)    

def check_existing_details(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return details.details_exist(name)    

def display_details():  
    '''
    Function that returns all the saved accounts
    '''
    return details.display_details() 




def main():
    print("Hello! Welcome to Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n SU -> SIGN UP.\n DA -> Display account.\n LN ->LOGIN.\n ex ->exit Password Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create an Account")
            print("_"*100)
            account_name = input('Account name:')
            print ('\n')
            u_name = input('Username:')
            print ('\n')
            pwd = input('Password: ')
            print ('\n')
            e_address = input('Email address:')
            save_accounts(create_account(account_name,u_name,pwd,e_address)) 
            print ('\n')
            print(f"A New {account_name} Account with the username  {u_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')
        elif short_code == 'da':
             if display_accounts():
                 print("Here are your account details:")
                 print('\n')
                 for account in display_accounts():
                     print(f"Account name:{account.account_name}  Username: {account.user_name} Password:{account.password}")
                     print('\n')
             else:
                 print('\n')
                 print("Account not found! Sign up to create a new account.")
                 print('\n')
        elif short_code == 'ln':
            print("Enter your password to log in:")
            search_account = input()
            if check_existing_accounts(search_account):
                search_cred = find_account(search_account)
                print("\033[1;32;1m   \n")
                print(f"You are now logged in to your {account_name} account :)")
                print("\033[1;37;1m   \n")
                
                while True:
                    print('''
                    Use these short codes:
                    CA -> Create new credential.
                    DC -> Display your details.
                    ex ->Log out your details account.''')
                    short_code = input().lower()
                    if short_code == "ca":
                        print("Create new credential")
                        print('_' * 20)
                        details_name = input('Credential name:')
                        print('\n')
                        usr_name = input(f"{details_name} user name:")
                        print('\n')
                        print('*' * 20)
                        pwd = input(f"{details_name} password:")
                        save_details(create_details(details_name,u_name,pwd,e_address))
                        print('\n')
                        print(f"A New {details_name} Account with the username  {usr_name} has been created.")
                        print ('\n')
                    elif short_code == 'dc':
                         if display_details():
                             print("Here are your details:")
                             print('\n')
                             for details in display_details():
                                 print(f"Credential name:{details.details_name}  Username: {details.usr_name} Password:{details.password}")
                                 print('\n')
                         else:
                              print('\n')
                              print("You don't seem to have created any account yet")
                              print('\n')
                    elif short_code == "ex":
                        print('\n')
                        print(f"You have logged out of your {account_name} account")
                        print('\n')
                        break
                        
            else:
                print('\n')
                print("INCORRECT PASSWORD!! PLEASE ENTER CORRECT PASSWORD:")
                print('\n')
                print('\n')
                    
        elif short_code == "ex":
                    print(f"Thank you {user_name} for your time!")
                    break
        else:
                    print("I did not understand. Please use the short codes provided")

if __name__ == '__main__':
    main()
    