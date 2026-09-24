SIMPLE BANKING SYSTEM

First Semester Python Project

A console-based educational banking application.

Features:

\- Create account

\- Login with PIN

\- Check balance

\- Deposit money

\- Withdraw money

\- Transfer money

\- View transaction history

\- View account details

\- Save data in JSON format

"""

import json

from datetime import datetime

from pathlib import Path

DATA_FILE = Path("accounts.json")

class Account:

&nbsp; """Represents one bank account."""

&nbsp; def \__init_\_(self, account_number, name, phone, pin, balance=0.0, history=None):

&nbsp; self.account_number = account_number

&nbsp; self.name = name

&nbsp; self.phone = phone

&nbsp; self.pin = pin

&nbsp; self.balance = float(balance)

&nbsp; self.history = history or \[\]

&nbsp; def verify_pin(self, pin):

&nbsp; return self.pin == pin

&nbsp; def deposit(self, amount):

&nbsp; self.balance += amount

&nbsp; self.history.append({

&nbsp; "type": "Deposit",

&nbsp; "amount": amount,

&nbsp; "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

&nbsp; })

&nbsp; def withdraw(self, amount):

&nbsp; if amount > self.balance:

&nbsp; return False

&nbsp; self.balance -= amount

&nbsp; self.history.append({

&nbsp; "type": "Withdrawal",

&nbsp; "amount": amount,

&nbsp; "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

&nbsp; })

&nbsp; return True

&nbsp; def show_history(self):

&nbsp; print("\\n---------- TRANSACTION HISTORY ----------")

&nbsp; if not self.history:

&nbsp; print("No transactions found.")

&nbsp; return

&nbsp; for number, transaction in enumerate(self.history, start=1):

&nbsp; print(

&nbsp; f"{number}. {transaction\['date'\]} | "

&nbsp; f"{transaction\['type'\]} | "

&nbsp; f"₹{transaction\['amount'\]:.2f}"

&nbsp; )

&nbsp; def show_details(self):

&nbsp; print("\\n---------- ACCOUNT DETAILS ----------")

&nbsp; print(f"Account Number : {self.account_number}")

&nbsp; print(f"Name : {self.name}")

&nbsp; print(f"Phone : {self.phone}")

&nbsp; print(f"Balance : ₹{self.balance:.2f}")

class BankingSystem:

&nbsp; """Controls accounts and banking operations."""

&nbsp; def \__init_\_(self):

&nbsp; self.accounts = self.load_accounts()

&nbsp; def load_accounts(self):

&nbsp; """Load saved accounts from accounts.json."""

&nbsp; if not DATA_FILE.exists():

&nbsp; return {}

&nbsp; try:

&nbsp; with open(DATA_FILE, "r", encoding="utf-8") as file:

&nbsp; data = json.load(file)

&nbsp; except (json.JSONDecodeError, OSError):

&nbsp; print("Warning: Could not read saved data. Starting with empty data.")

&nbsp; return {}

&nbsp; accounts = {}

&nbsp; for account_number, details in data.items():

&nbsp; accounts\[account_number\] = Account(

&nbsp; details\["account_number"\],

&nbsp; details\["name"\],

&nbsp; details\["phone"\],

&nbsp; details\["pin"\],

&nbsp; details\["balance"\],

&nbsp; details.get("history", \[\])

&nbsp; )

&nbsp; return accounts

&nbsp; def save_accounts(self):

&nbsp; """Save all accounts to accounts.json."""

&nbsp; data = {}

&nbsp; for number, account in self.accounts.items():

&nbsp; data\[number\] = {

&nbsp; "account_number": account.account_number,

&nbsp; "name": account.name,

&nbsp; "phone": account.phone,

&nbsp; "pin": account.pin,

&nbsp; "balance": account.balance,

&nbsp; "history": account.history

&nbsp; }

&nbsp; with open(DATA_FILE, "w", encoding="utf-8") as file:

&nbsp; json.dump(data, file, indent=4)

&nbsp; @staticmethod

&nbsp; def valid_account_number(account_number):

&nbsp; return account_number.isdigit() and len(account_number) == 6

&nbsp; @staticmethod

&nbsp; def valid_pin(pin):

&nbsp; return pin.isdigit() and len(pin) == 4

&nbsp; @staticmethod

&nbsp; def get_positive_amount(message):

&nbsp; try:

&nbsp; amount = float(input(message))

&nbsp; if amount <= 0:

&nbsp; print("Amount must be greater than zero.")

&nbsp; return None

&nbsp; return amount

&nbsp; except ValueError:

&nbsp; print("Please enter a valid number.")

&nbsp; return None

&nbsp; def create_account(self):

&nbsp; print("\\n========== CREATE ACCOUNT ==========")

&nbsp; name = input("Enter account holder name: ").strip()

&nbsp; if not name:

&nbsp; print("Name cannot be empty.")

&nbsp; return

&nbsp; phone = input("Enter 10-digit phone number: ").strip()

&nbsp; if not phone.isdigit() or len(phone) != 10:

&nbsp; print("Phone number must contain exactly 10 digits.")

&nbsp; return

&nbsp; account_number = input("Create a 6-digit account number: ").strip()

&nbsp; if not self.valid_account_number(account_number):

&nbsp; print("Account number must contain exactly 6 digits.")

&nbsp; return

&nbsp; if account_number in self.accounts:

&nbsp; print("This account number already exists.")

&nbsp; return

&nbsp; pin = input("Create a 4-digit PIN: ").strip()

&nbsp; if not self.valid_pin(pin):

&nbsp; print("PIN must contain exactly 4 digits.")

&nbsp; return

&nbsp; opening_balance = self.get_positive_amount(

&nbsp; "Enter opening balance: ₹"

&nbsp; )

&nbsp; if opening_balance is None:

&nbsp; return

&nbsp; account = Account(

&nbsp; account_number,

&nbsp; name,

&nbsp; phone,

&nbsp; pin,

&nbsp; opening_balance

&nbsp; )

&nbsp; self.accounts\[account_number\] = account

&nbsp; self.save_accounts()

&nbsp; print("\\nAccount created successfully!")

&nbsp; print(f"Your account number is: {account_number}")

&nbsp; def login(self):

&nbsp; print("\\n========== LOGIN ==========")

&nbsp; account_number = input("Enter account number: ").strip()

&nbsp; if account_number not in self.accounts:

&nbsp; print("Account not found.")

&nbsp; return

&nbsp; pin = input("Enter PIN: ").strip()

&nbsp; account = self.accounts\[account_number\]

&nbsp; if not account.verify_pin(pin):

&nbsp; print("Incorrect PIN.")

&nbsp; return

&nbsp; print(f"\\nWelcome, {account.name}!")

&nbsp; self.account_menu(account)

&nbsp; def account_menu(self, account):

&nbsp; while True:

&nbsp; print("\\n========== ACCOUNT MENU ==========")

&nbsp; print("1. Check Balance")

&nbsp; print("2. Deposit Money")

&nbsp; print("3. Withdraw Money")

&nbsp; print("4. Transfer Money")

&nbsp; print("5. Transaction History")

&nbsp; print("6. Account Details")

&nbsp; print("7. Logout")

&nbsp; choice = input("Enter your choice: ").strip()

&nbsp; if choice == "1":

&nbsp; print(f"\\nCurrent Balance: ₹{account.balance:.2f}")

&nbsp; elif choice == "2":

&nbsp; self.deposit(account)

&nbsp; elif choice == "3":

&nbsp; self.withdraw(account)

&nbsp; elif choice == "4":

&nbsp; self.transfer(account)

&nbsp; elif choice == "5":

&nbsp; account.show_history()

&nbsp; elif choice == "6":

&nbsp; account.show_details()

&nbsp; elif choice == "7":

&nbsp; self.save_accounts()

&nbsp; print("Logged out successfully.")

&nbsp; break

&nbsp; else:

&nbsp; print("Invalid choice. Please select 1-7.")

&nbsp; input("\\nPress Enter to continue...")

&nbsp; def deposit(self, account):

&nbsp; amount = self.get_positive_amount("Enter amount to deposit: ₹")

&nbsp; if amount is None:

&nbsp; return

&nbsp; account.deposit(amount)

&nbsp; self.save_accounts()

&nbsp; print(f"₹{amount:.2f} deposited successfully.")

&nbsp; print(f"New Balance: ₹{account.balance:.2f}")

&nbsp; def withdraw(self, account):

&nbsp; amount = self.get_positive_amount("Enter amount to withdraw: ₹")

&nbsp; if amount is None:

&nbsp; return

&nbsp; if not account.withdraw(amount):

&nbsp; print("Insufficient balance.")

&nbsp; return

&nbsp; self.save_accounts()

&nbsp; print(f"₹{amount:.2f} withdrawn successfully.")

&nbsp; print(f"New Balance: ₹{account.balance:.2f}")

&nbsp; def transfer(self, sender):

&nbsp; receiver_number = input(

&nbsp; "Enter receiver's 6-digit account number: "

&nbsp; ).strip()

&nbsp; if receiver_number not in self.accounts:

&nbsp; print("Receiver account not found.")

&nbsp; return

&nbsp; if receiver_number == sender.account_number:

&nbsp; print("You cannot transfer money to your own account.")

&nbsp; return

&nbsp; amount = self.get_positive_amount(

&nbsp; "Enter amount to transfer: ₹"

&nbsp; )

&nbsp; if amount is None:

&nbsp; return

&nbsp; if not sender.withdraw(amount):

&nbsp; print("Insufficient balance.")

&nbsp; return

&nbsp; receiver = self.accounts\[receiver_number\]

&nbsp; receiver.deposit(amount)

&nbsp; self.save_accounts()

&nbsp; print(

&nbsp; f"₹{amount:.2f} transferred successfully "

&nbsp; f"to {receiver.name}."

&nbsp; )

def main():

&nbsp; """Start the banking system."""

&nbsp; banking_system = BankingSystem()

&nbsp; while True:

&nbsp; print("\\n========================================")

&nbsp; print(" SIMPLE BANKING SYSTEM")

&nbsp; print("========================================")

&nbsp; print("1. Create Account")

&nbsp; print("2. Login")

&nbsp; print("3. Exit")

&nbsp; choice = input("Enter your choice: ").strip()

&nbsp; if choice == "1":

&nbsp; banking_system.create_account()

&nbsp; elif choice == "2":

&nbsp; banking_system.login()

&nbsp; elif choice == "3":

&nbsp; banking_system.save_accounts()

&nbsp; print("\\nThank you for using the Simple Banking System!")

&nbsp; print("Goodbye!")

&nbsp; break

&nbsp; else:

&nbsp; print("Invalid choice. Please enter 1, 2, or 3.")

&nbsp; input("\\nPress Enter to continue...")

if \__name__ == "\__main_\_":

&nbsp; main()