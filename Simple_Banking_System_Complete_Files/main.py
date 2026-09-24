"""
SIMPLE BANKING SYSTEM
First Semester Python Project

A console-based educational banking application.
Features:
- Create account
- Login with PIN
- Check balance
- Deposit money
- Withdraw money
- Transfer money
- View transaction history
- View account details
- Save data in JSON format
"""

import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("accounts.json")


class Account:
    """Represents one bank account."""

    def __init__(self, account_number, name, phone, pin, balance=0.0, history=None):
        self.account_number = account_number
        self.name = name
        self.phone = phone
        self.pin = pin
        self.balance = float(balance)
        self.history = history or []

    def verify_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.history.append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def withdraw(self, amount):
        if amount > self.balance:
            return False

        self.balance -= amount
        self.history.append({
            "type": "Withdrawal",
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        return True

    def show_history(self):
        print("\n---------- TRANSACTION HISTORY ----------")

        if not self.history:
            print("No transactions found.")
            return

        for number, transaction in enumerate(self.history, start=1):
            print(
                f"{number}. {transaction['date']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']:.2f}"
            )

    def show_details(self):
        print("\n---------- ACCOUNT DETAILS ----------")
        print(f"Account Number : {self.account_number}")
        print(f"Name           : {self.name}")
        print(f"Phone          : {self.phone}")
        print(f"Balance        : ₹{self.balance:.2f}")


class BankingSystem:
    """Controls accounts and banking operations."""

    def __init__(self):
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Load saved accounts from accounts.json."""
        if not DATA_FILE.exists():
            return {}

        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read saved data. Starting with empty data.")
            return {}

        accounts = {}

        for account_number, details in data.items():
            accounts[account_number] = Account(
                details["account_number"],
                details["name"],
                details["phone"],
                details["pin"],
                details["balance"],
                details.get("history", [])
            )

        return accounts

    def save_accounts(self):
        """Save all accounts to accounts.json."""
        data = {}

        for number, account in self.accounts.items():
            data[number] = {
                "account_number": account.account_number,
                "name": account.name,
                "phone": account.phone,
                "pin": account.pin,
                "balance": account.balance,
                "history": account.history
            }

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def valid_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 6

    @staticmethod
    def valid_pin(pin):
        return pin.isdigit() and len(pin) == 4

    @staticmethod
    def get_positive_amount(message):
        try:
            amount = float(input(message))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return None
            return amount
        except ValueError:
            print("Please enter a valid number.")
            return None

    def create_account(self):
        print("\n========== CREATE ACCOUNT ==========")

        name = input("Enter account holder name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        phone = input("Enter 10-digit phone number: ").strip()
        if not phone.isdigit() or len(phone) != 10:
            print("Phone number must contain exactly 10 digits.")
            return

        account_number = input("Create a 6-digit account number: ").strip()

        if not self.valid_account_number(account_number):
            print("Account number must contain exactly 6 digits.")
            return

        if account_number in self.accounts:
            print("This account number already exists.")
            return

        pin = input("Create a 4-digit PIN: ").strip()

        if not self.valid_pin(pin):
            print("PIN must contain exactly 4 digits.")
            return

        opening_balance = self.get_positive_amount(
            "Enter opening balance: ₹"
        )

        if opening_balance is None:
            return

        account = Account(
            account_number,
            name,
            phone,
            pin,
            opening_balance
        )

        self.accounts[account_number] = account
        self.save_accounts()

        print("\nAccount created successfully!")
        print(f"Your account number is: {account_number}")

    def login(self):
        print("\n========== LOGIN ==========")

        account_number = input("Enter account number: ").strip()

        if account_number not in self.accounts:
            print("Account not found.")
            return

        pin = input("Enter PIN: ").strip()
        account = self.accounts[account_number]

        if not account.verify_pin(pin):
            print("Incorrect PIN.")
            return

        print(f"\nWelcome, {account.name}!")
        self.account_menu(account)

    def account_menu(self, account):
        while True:
            print("\n========== ACCOUNT MENU ==========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Transaction History")
            print("6. Account Details")
            print("7. Logout")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                print(f"\nCurrent Balance: ₹{account.balance:.2f}")

            elif choice == "2":
                self.deposit(account)

            elif choice == "3":
                self.withdraw(account)

            elif choice == "4":
                self.transfer(account)

            elif choice == "5":
                account.show_history()

            elif choice == "6":
                account.show_details()

            elif choice == "7":
                self.save_accounts()
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please select 1-7.")

            input("\nPress Enter to continue...")

    def deposit(self, account):
        amount = self.get_positive_amount("Enter amount to deposit: ₹")

        if amount is None:
            return

        account.deposit(amount)
        self.save_accounts()

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"New Balance: ₹{account.balance:.2f}")

    def withdraw(self, account):
        amount = self.get_positive_amount("Enter amount to withdraw: ₹")

        if amount is None:
            return

        if not account.withdraw(amount):
            print("Insufficient balance.")
            return

        self.save_accounts()

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"New Balance: ₹{account.balance:.2f}")

    def transfer(self, sender):
        receiver_number = input(
            "Enter receiver's 6-digit account number: "
        ).strip()

        if receiver_number not in self.accounts:
            print("Receiver account not found.")
            return

        if receiver_number == sender.account_number:
            print("You cannot transfer money to your own account.")
            return

        amount = self.get_positive_amount(
            "Enter amount to transfer: ₹"
        )

        if amount is None:
            return

        if not sender.withdraw(amount):
            print("Insufficient balance.")
            return

        receiver = self.accounts[receiver_number]
        receiver.deposit(amount)

        self.save_accounts()

        print(
            f"₹{amount:.2f} transferred successfully "
            f"to {receiver.name}."
        )


def main():
    """Start the banking system."""
    banking_system = BankingSystem()

    while True:
        print("\n========================================")
        print("        SIMPLE BANKING SYSTEM")
        print("========================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            banking_system.create_account()

        elif choice == "2":
            banking_system.login()

        elif choice == "3":
            banking_system.save_accounts()
            print("\nThank you for using the Simple Banking System!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
