"""
Banking System

for admin the username is: admin
password is : 123456
"""

import random
class Role:
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

class User(Role):
    valid_account_numbers = []
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address)
        self.account_type = account_type
        self.balance = 0
        self.account_number = self.new_account_number()
        User.valid_account_numbers.append(self.account_number)
        self.transaction_history = []
        self.loan_count = 0

    def new_account_number(self):
        return random.randint(10000,99999)
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("You are out of money.")
        else:
            self.balance -= amount
            self.transaction_history.append(Transaction("Withdrawal", amount))
            print(f'{amount} is withdrawn from your account')

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(Transaction("Deposit", amount))
        print(f"{amount} deposited in your account")

    def balance_checking(self):
        print("----------Current Balance--------")
        print(f"Your Current is {self.balance}")
    
    def view_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(f"Type: {transaction.transaction_type}, Amount: {transaction.amount}")

    def loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.transaction_history.append(Transaction("Loan",amount))
            self.loan_count += 1
            print(f"Loan approved. Current balance {self.balance}")
        
        else:
            print("You have already taken loan for 2 times")

        
    def transfer_amount(self, recipient_account, amount):
        if recipient_account in User.valid_account_numbers:
            if self.balance >= amount:
                self.balance -= amount
                recipient_account.balance += amount
                self.transaction_history.append(Transaction("Transfer", -amount))
                recipient_account.transaction_history.append(Transaction("Transfer", amount))
                print(f"Amount {amount} transferred successfully to {recipient_account.name}.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Recipient account does not exist.")

    
class Admin(Role):
    user_accounts = []

    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    def new_account_number(self):
        return random.randint(10000, 99999)

    def create_account(self, name, email, address, account_type):
        account_number = self.new_account_number()
        new_user = User(name, email, address, account_type, account_number)
        Admin.user_accounts.append(new_user)
        print(f"User account created successfully. Account number: {new_user.account_number}")

    def delete_account(self, account_number):
        for user in Admin.user_accounts:
            if user.account_number == account_number:
                Admin.user_accounts.remove(user)
                print(f"User account with account number {account_number} deleted successfully.")
                return
        print("User account not found.")

    def view_all_accounts(self):
        print("List of all user accounts:")
        for user in Admin.user_accounts:
            print(f"Name: {user.name}, Email: {user.email}, Account Number: {user.account_number}")

    def total_available_balance(self):
        total_balance = sum(user.balance for user in Admin.user_accounts)
        print(f"Total available balance in the bank: {total_balance}")

    def total_loan_amount(self):
        total_loan = sum(user.balance for user in Admin.user_accounts if user.balance < 0)
        print(f"Total loan amount in the bank: {abs(total_loan)}")

    def toggle_loan_feature(self, status):
        if status == "on":
            User.loan_enabled = True
            print("Loan feature is now enabled.")
        elif status == "off":
            User.loan_enabled = False
            print("Loan feature is now disabled.")
        else:
            print("Invalid option. Please enter 'on' or 'off'.")

while True:
        print("\nOptions:")
        print("1. User")
        print("2. Admin")
        print("3. Exit")

        choice = input("Enter your choice: ")


        if choice == '1':
                    while True:
                        print("\nOptions:")
                        print("1. Create Account")
                        print("2. Deposit")
                        print("3. Withdraw")
                        print("4. Available Balance")
                        print("5. Transaction History")
                        print("6. Take Loan")
                        print("7. Transfer Money")
                        print("8. Exit")

                        user_choice = input("Enter your choice: ")

                        if user_choice == "1":
                            name = input("Enter your name: ")
                            email = input("Enter your email: ")
                            address = input("Enter your address: ")
                            account_type = input("Enter your account type: ")
                            user = User(name, email, address, account_type)
                            Admin.user_accounts.append(user)
                            print(f"Account created successfully. Your account number is {user.account_number}")

                        elif user_choice == "2":
                            account_number = int(input("Enter your account number: "))
                            amount = float(input("Enter the amount to deposit: "))
                            for user in Admin.user_accounts:
                                if user.account_number == account_number:
                                    user.deposit(amount)
                                    break
                                else:
                                    print("User account not found.")

                        elif user_choice == "3":
                            account_number = int(input("Enter your account number: "))
                            amount = float(input("Enter the amount to withdraw: "))
                            for user in Admin.user_accounts:
                                if user.account_number == account_number:
                                    user.withdraw(amount)
                                    break
                                else:
                                    print("User account not found.")

                        elif user_choice == "4":
                            account_number = int(input("Enter your account number: "))
                            for user in Admin.user_accounts:
                                if user.account_number == account_number:
                                    user.balance_checking()
                                    break
                                else:
                                    print("User account not found.")

                        elif user_choice == "5":
                            account_number = int(input("Enter your account number: "))
                            for user in Admin.user_accounts:
                                if user.account_number == account_number:
                                    user.view_transaction_history()
                                    break
                                else:
                                    print("User account not found.")

                        elif user_choice == "6":
                            account_number = int(input("Enter your account number: "))
                            amount = float(input("Enter the loan amount: "))
                            for user in Admin.user_accounts:
                                if user.account_number == account_number:
                                    user.loan(amount)
                                    break
                                else:
                                    print("User account not found.")

                        elif user_choice == "7":
                            sender_account_number = int(input("Enter your account number: "))
                            recipient_account_number = int(input("Enter the recipient's account number: "))
                            amount = float(input("Enter the amount to transfer: "))
                            for sender in Admin.user_accounts:
                                if sender.account_number == sender_account_number:
                                    for recipient in Admin.user_accounts:
                                        if recipient.account_number == recipient_account_number:
                                            sender.transfer_amount(recipient, amount)
                                            break
                                        else:
                                            print("Recipient account not found.")
                                            break
                                else:
                                    print("Sender account not found.")

                        elif user_choice == "8":
                            break

                        else:
                            print("Invalid choice. Please try again.")

        elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if username == "admin" and password == "123456":


            # username = input("Enter your username: ")
            # password = input("Enter your password: ")

            
            # if username == "admin" and password == "123456":
                    admin = Admin("Admin", "gewgsef@gm.com", "Advsdsvf")
                    while True:
                        print("\nOptions:")
                        print("1. Create Account")
                        print("2. Delete Account")
                        print("3. View All Accounts")
                        print("4. Total Available Balance")
                        print("5. Total Loan Amount")
                        print("6. On/Off loan feature")
                        print("7. Exit")

                        admin_choice = input("Enter your choice: ")

                        if admin_choice == "1":
                            name = input("Enter user's name: ")
                            email = input("Enter user's email: ")
                            address = input("Enter user's address: ")
                            account_type = input("Enter user's account type: ")
                            admin.create_account(name, email, address, account_type)

                        elif admin_choice == "2":
                            account_number = int(input("Enter account number to delete: "))
                            admin.delete_account(account_number)

                        elif admin_choice == "3":
                            admin.view_all_accounts()

                        elif admin_choice == "4":
                            admin.total_available_balance()

                        elif admin_choice == "5":
                            admin.total_loan_amount()

                        elif admin_choice == "6":
                            print("Feature is under construction")
                        elif admin_choice == "7":
                            break

                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("Wrong username or password")

        elif choice == '3':
            break

        else:
            print("Invalid choice! Please try again.")