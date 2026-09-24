# Project Statement

## Project Title

**Simple Banking System**

---

## 1. Problem Statement

Develop a simple Python-based banking system that allows users to create and manage bank accounts and perform common banking operations through a menu-driven console application.

The system should provide account creation, login, balance checking, deposits, withdrawals, money transfers, account details, and transaction history.

The application should validate user inputs and store account information so that the data can be used again when the program is restarted.

---

## 2. Project Scope

The project focuses on basic banking operations for educational purposes.

The system will:

- Create new customer accounts.
- Assign a unique six-digit account number.
- Create a four-digit PIN.
- Allow customers to log in.
- Display the current balance.
- Deposit money.
- Withdraw money.
- Transfer money to another account.
- Display transaction history.
- Display account details.
- Store account data in a JSON file.
- Validate user input.
- Handle common errors.

### Out of Scope

The system is not designed for real banking use.

It does not include:

- Real bank servers
- Real payment gateways
- ATM integration
- Internet banking
- Real financial transactions
- Government or bank identity verification

---

## 3. Target Users

The main target users are:

- First-semester students learning Python.
- Teachers evaluating Python programming projects.
- Beginners learning Object-Oriented Programming.
- Students learning file handling and JSON.

---

## 4. Project Objectives

The major objectives are:

1. Apply Python programming concepts to a practical problem.
2. Understand Object-Oriented Programming.
3. Implement account management.
4. Implement basic banking operations.
5. Use JSON for data storage.
6. Learn input validation.
7. Learn exception handling.
8. Develop a menu-driven application.
9. Organize a complete academic project.
10. Understand how a simple software system is designed and tested.

---

## 5. Functional Requirements

### FR1: Account Creation

The system shall allow a user to create a new account by entering:

- Account holder name
- Phone number
- Account number
- PIN
- Opening balance

The system shall reject invalid input.

### FR2: Login

The system shall allow an account holder to log in using:

- Account number
- PIN

The system shall reject an incorrect PIN.

### FR3: Check Balance

The logged-in user shall be able to view the current account balance.

### FR4: Deposit

The logged-in user shall be able to deposit a positive amount into their account.

### FR5: Withdrawal

The logged-in user shall be able to withdraw money if sufficient balance is available.

### FR6: Transfer

The logged-in user shall be able to transfer money to another existing account.

The transfer shall be rejected if:

- The receiver does not exist.
- The sender has insufficient balance.
- The sender attempts to transfer to the same account.
- The entered amount is invalid.

### FR7: Transaction History

The system shall maintain and display transaction history.

### FR8: Account Details

The system shall display the user's account number, name, phone number, and current balance.

### FR9: Data Storage

The system shall save account information and transaction history in a JSON file.

---

## 6. Non-Functional Requirements

### NFR1: Usability

The application should be simple and easy to understand.

### NFR2: Reliability

The application should continue running after normal input errors.

### NFR3: Maintainability

The code should use classes and functions so that it can be updated easily.

### NFR4: Resource Efficiency

The application should use lightweight local JSON storage.

### NFR5: Security

The account should require a PIN for login.

### NFR6: Error Handling

The program should handle invalid input and display meaningful error messages.

---

## 7. Input and Output

### Inputs

The system accepts:

- Name
- Phone number
- Account number
- PIN
- Amount
- Receiver account number
- Menu choices

### Outputs

The system displays:

- Account creation status
- Login status
- Current balance
- Transaction results
- Transaction history
- Account details
- Error messages

---

## 8. System Workflow

```text
                  START
                    |
                    v
             +-------------+
             |  Main Menu  |
             +-------------+
                /       \
               /         \
              v           v
     Create Account      Login
           |               |
           v               v
     Validate Data    Verify PIN
           |               |
           v               v
       Save Data      Account Menu
                           |
          +----------------+----------------+
          |        |        |       |       |
       Balance  Deposit  Withdraw Transfer History
          |        |        |       |       |
          +--------+--------+-------+-------+
                           |
                           v
                       Save Data
                           |
                           v
                         Logout
                           |
                           v
                          END
```

---

## 9. System Architecture

```text
+----------------------+
|       User           |
+----------+-----------+
           |
           v
+----------------------+
|    Main Program      |
|       main.py        |
+----------+-----------+
           |
           v
+----------------------+
|   Banking System     |
| Account Operations   |
+----------+-----------+
           |
           v
+----------------------+
|      Account         |
| Balance & History    |
+----------+-----------+
           |
           v
+----------------------+
|     JSON Storage     |
|    accounts.json     |
+----------------------+
```

---

## 10. Use Cases

### Actor

**User**

### Use Cases

- Create Account
- Login
- Check Balance
- Deposit Money
- Withdraw Money
- Transfer Money
- View Transaction History
- View Account Details
- Logout

---

## 11. Data Design

Each account contains:

```text
Account
-------------------------
account_number
name
phone
pin
balance
history
```

Each transaction contains:

```text
Transaction
-------------------------
type
amount
date
```

---

## 12. Technologies

The project uses:

- Python 3
- Object-Oriented Programming
- JSON
- File Handling
- Functions
- Dictionaries
- Lists
- Loops
- Conditional Statements
- Exception Handling

No external packages are required.

---

## 13. Expected Outcome

After completing the project, the user should be able to:

1. Create a bank account.
2. Log into the account.
3. Check the account balance.
4. Deposit money.
5. Withdraw money.
6. Transfer money.
7. View transaction history.
8. View account details.
9. Close and reopen the program without losing saved account data.

---

## 14. Limitations

This is a basic educational banking system.

The system does not provide the security, database infrastructure, encryption, authentication systems, or regulatory controls required by real financial institutions.

---

## 15. Future Enhancements

Possible future improvements include:

- Graphical User Interface
- SQLite/MySQL database
- PIN hashing
- Admin panel
- Change PIN
- Account deletion
- Monthly statements
- Interest calculation
- Transaction IDs
- Advanced reporting

---

## 16. Conclusion

The Simple Banking System is designed to demonstrate how Python can be used to create a practical application.

It combines programming fundamentals with Object-Oriented Programming, file handling, JSON storage, validation, and error handling.

The project is suitable for a first-semester Python course and can be expanded with additional features as programming knowledge increases.
