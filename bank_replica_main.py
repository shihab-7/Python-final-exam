class User:
    users = []
    account_number = 20000

    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.took_loans = 0
        self.transactions = [] 
        User.account_number += 5 # generating acc_no.
        self.account_number = User.account_number

        User.users.append(self) # storing users

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f'Deposited : {amount} Taka')
            print(f'You have just Diposited : {amount} Taka in your account')
        else:
            print('Invalid Amount, Try again')


    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f'Withdraw : {amount} Taka')
            print(f'You just Withdraw : {amount} Taka from your account')
        else:
            print('Withdrawl amount exceeded.')

    def check_current_balance(self):
        print(f'Your current Balance is : {self.balance} Taka')

    def check_transactions(self):
        print('Your transaction history :')
        for transaction in self.transactions:
            print(transaction)

    def take_loan(self, loan_amount):
        if self.took_loans < 2 :
            self.balance += loan_amount
            self.took_loans += 1
            self.transactions.append(f'Loan : {loan_amount} Taka')
            print(f'You have get a loan of {loan_amount} Taka')
        elif self.took_loans >= 2 :
            print('Your loan taking limit is over')

    def balance_transfer(self, other_account, send_amount):
        if other_account in User.users:
            if send_amount > 0 and send_amount <= self.balance:
                other_account.deposit(send_amount)
                self.balance -= send_amount
                self.transactions.append(f'Send money : {send_amount}')
                print(f'You just transfer {send_amount} Taka to account {other_account.name}')
            else :
                print('Invalid amount')
        else:
            print('Account does not exist')

    def is_a_valid_account(account_number):
        v = False
        for user in User.users:
            if user.account_number == account_number:
                v = True
        return v


    def account_details(self):
        print(f'Account Number : {self.account_number}\nName : {self.name}\nEmail : {self.email}\nAddress : {self.address}\nAccount Type : {self.account_type}\n')


class Admin:
    id = 'admin'
    password = '123'
    def creat_account_for_user(self, name, email, address, account_type):
        User(name, email, address, account_type)
        acc_no = User.account_number
        print(f'A new user is created Account number {acc_no}')


    def delete_user_account(self, account_number):
        for user in User.users:
            if user.account_number == account_number:
                User.users.remove(user)
                print(f'Acoount : {account_number} has been deleted')

    def user_list(self):
        if len(User.users) == 0:
            print(' (-_-) Empty user list')
        else:
            for user in User.users:
                print()
                print(f'Owner : {user.name}')
                print(f'Email : {user.email}')
                print(f'Account number : {user.account_number}')
                print(f'Account Type : {user.account_type}')
                print(f'Address : {user.address}')

    def total_bank_balance(self):
        total = 0
        for user in User.users:
            total += user.balance
        print(f'Total available balance in the bank is : {total} Taka')

    def total_loan_amount(self):
        total_loan = 0
        for user in User.users:
            if user.took_loans > 0:
                total_loan += user.balance
        print(f'Total loan amount of the bank is : {total_loan}')

    def on_off_loan(self, option):
        option = True
        if option == True:
            User.took_loans = 0
            print('loan is enabled')
        else:
            User.took_loans = 2
            print('loan is disabled')

 

    
while True:
    print()
    print('---------------Welcome to the Bank----------------')
    print()
    print('1 . Press 1 for User')
    print('2 . Press 2 for Admin')
    print('3 . Press 3 for Exit')
    print()
    
    option = input('Enter your option : ')
    print()

    if option == '1':
        print()
        print('User ====>')
        print('1 . Creat Account')
        print('2 . Account log in')
        print('3 . Back')
        print()

        user_option = input('Enter your option : ')
        print()

        if user_option == '1':
            print()
            name = input('Enter name : ')
            email = input('Enter email : ')
            address = input('Enter address : ')
            account_type = input('Enter Account Type : ')
            admin = Admin()
            admin.creat_account_for_user(name, email, address, account_type)
        elif user_option == '2' :
            print()
            account_num = int(input('Enter your account number to log in : '))
            if User.is_a_valid_account(account_num):
                user = None
                for owner in User.users:
                    if owner.account_number == account_num:
                        user = owner
                        break
                if user is not None:
                    while True:
                        print()
                        print('====Menu====')
                        print('1 . Deposit')
                        print('2 . Withdraw')
                        print('3 . Check Balance')
                        print('4 . Check Transaction History')
                        print('5 . Take a loan ')
                        print('6 . Transfer Money')
                        print('7 . Log out')
                        print()
                        user_choice = input('Enter your option : ')
                        print()

                        if user_choice == '1':
                            deposit_amount = int(input('Enter your Deposit amount : '))
                            user.deposit(deposit_amount)
                        elif user_choice == '2' :
                            withdraw_amount = int(input('Enter your withdrawl amount : '))
                            user.withdraw(withdraw_amount)
                        elif user_choice == '3' :
                            user.check_current_balance()
                        elif user_choice == '4' :
                            user.check_transactions()
                        elif user_choice == '5' :
                            loan_amount = int(input('Enter your amount you want as loan : '))
                            user.take_loan(loan_amount)
                        elif user_choice == '6' :
                            other_user_accNo = int(input('Enter the account number of the user : '))
                            if User.is_a_valid_account(other_user_accNo):
                                other_user = None
                                for other_owner in User.users:
                                    if other_owner.account_number == other_user_accNo:
                                        other_user = other_owner
                                        break
                            
                                if other_user is not None:
                                    transfer_amount = int(input('Enter transfer amount : '))
                                    user.balance_transfer(other_user, transfer_amount)
                            else:
                                    print('Account does not exist')   
                        elif user_choice == '7':
                            break
                        else:
                            print('Invalid option , try again')
            else :
                    print('Invalid account number')   
        elif user_option == '3' :
            continue
        else:
            print('Invalid option , try again')
    elif option == '2' :
        admin_password = input('Enter password to log in as Admin: ')
        if Admin.password == '123':
            print()
            print('=====Admin Menu======')
            print('1 . Creat user Account')
            print('2 . Delete user Account')
            print('3 . See User Accounts list')
            print('4 . Check Total Balance available in Bank')
            print('5 . Check Total loan amount')
            print('6 . On / Off loan feature of the Bank')
            print('7 . Back')
            print()
            admin_option = input('Enter your option : ')
            print()

            admin = Admin()
            if admin_option == '1' :
                name = input('Enter name : ')
                email = input('Enter email : ')
                address = input('Enter address : ')
                account_type = input('Enter Account Type : ')
                admin.creat_account_for_user(name, email, address, account_type)
            elif admin_option == '2' :
                account_number = int(input('Enter account number to delete user : '))
                admin.delete_user_account(account_number)
            elif admin_option == '3' :
                admin.user_list()
            elif admin_option == '4' :
                admin.total_bank_balance()
            elif admin_option == '5' :
                admin.total_loan_amount()
            elif admin_option == '6' :
                switch = input('Enable load ? (on/off) : ')
                if switch == 'on':
                    admin.on_off_loan(True)
                else:
                    admin.on_off_loan(False)
            elif admin_option == '7' :
                continue
            else :
                print('Invalid option , try again')
        else:
            print('Wrong password , try again')
    elif option == '3' :
        print()
        print('<<<<<<< Exited >>>>>>>>')
        print()
        break
    else:
        print('Invalid option , try again')