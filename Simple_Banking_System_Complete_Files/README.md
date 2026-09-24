# Simple Banking System

## Project Overview

The **Simple Banking System** is a beginner-friendly, console-based Python project developed as a first-semester programming project.

The system simulates basic banking operations such as creating an account, logging in, checking balance, depositing money, withdrawing money, transferring money, and viewing transaction history.

The project uses **Python, Object-Oriented Programming, JSON file handling, functions, loops, conditional statements, dictionaries, and input validation**.

> **Note:** This is an educational project and is not intended for real banking or financial use.

---

## Problem Statement

Students learning programming need practical projects through which they can apply programming concepts to a real-world problem.

The objective of this project is to develop a simple banking application that can manage basic customer accounts and perform common banking operations through a menu-driven Python program.

---

## Objectives

1. Create and manage bank accounts.
2. Provide PIN-based account login.
3. Allow users to check their balance.
4. Allow users to deposit money.
5. Allow users to withdraw money.
6. Allow users to transfer money between accounts.
7. Maintain transaction history.
8. Store account information permanently using a JSON file.
9. Validate user input and handle common errors.
10. Demonstrate modular and object-oriented Python programming.

---

## Main Features

### 1. Create Account
The user enters:
- Name
- 10-digit phone number
- 6-digit account number
- 4-digit PIN
- Opening balance

The program checks the input before creating the account.

### 2. Login
The user logs in using:
- Account number
- PIN

### 3. Check Balance
The current account balance is displayed.

### 4. Deposit Money
The user can add money to their account.

### 5. Withdraw Money
The user can withdraw money if enough balance is available.

### 6. Transfer Money
The user can transfer money to another existing account.

### 7. Transaction History
The system displays previous deposits and withdrawals with date and time.

### 8. Account Details
The system displays basic account information and current balance.

### 9. Data Persistence
Account information is saved in `accounts.json`, so the data remains available after restarting the program.

### 10. Error Handling
The program handles:
- Invalid account numbers
- Invalid PINs
- Invalid phone numbers
- Empty names
- Invalid amounts
- Duplicate account numbers
- Non-existing receiver accounts
- Insufficient balance

---

## Technologies Used

- **Python 3**
- JSON
- File Handling
- Object-Oriented Programming
- Functions
- Lists
- Dictionaries
- Conditional Statements
- Loops
- Exception Handling

No external Python libraries are required.

---

## Project Structure

```text
Simple_Banking_System/
│
├── main.py
├── README.md
├── statement.md
└── accounts.json
```

### File Description

| File | Purpose |
|---|---|
| `main.py` | Complete Python source code |
| `accounts.json` | Stores account data |
| `README.md` | Project documentation |
| `statement.md` | Project statement and requirements |

---

## How to Run

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Open the Project Folder

Open Command Prompt, PowerShell, or VS Code terminal inside the project folder.

### Step 3: Run the Program

```bash
python main.py
```

If your computer uses `python3`, run:

```bash
python3 main.py
```

---

## Example Workflow

```text
START
  |
  v
Main Menu
  |
  +---- Create Account
  |         |
  |         v
  |    Validate Details
  |         |
  |         v
  |     Save Account
  |
  +---- Login
            |
            v
       Verify PIN
            |
            v
       Account Menu
            |
     +------+-------+---------+---------+
     |      |       |         |         |
 Balance Deposit Withdraw Transfer History
     |      |       |         |         |
     +------+-------+---------+---------+
                    |
                    v
                Save Data
                    |
                    v
                  Logout
```

---

## Functional Modules

The project provides the following major functional modules:

1. **Account Management**
   - Create account
   - Store account information
   - Login

2. **Banking Operations**
   - Check balance
   - Deposit
   - Withdraw
   - Transfer

3. **Transaction Management**
   - Record transactions
   - Display transaction history

4. **Data Management**
   - Load data from JSON
   - Save data to JSON

---

## Non-Functional Requirements

### Usability
The system uses a simple menu-driven interface suitable for beginners.

### Reliability
The program validates input and handles common errors without crashing.

### Maintainability
The program uses classes and separate functions so that features can be modified easily.

### Resource Efficiency
JSON is used as lightweight local storage, so no external database is required.

### Security
A PIN is required to access an account.

### Error Handling
Invalid inputs such as incorrect account numbers, invalid amounts, and insufficient balances are handled.

---

## Testing

| Test Case | Expected Result |
|---|---|
| Create valid account | Account is created |
| Create duplicate account | Error message displayed |
| Enter invalid phone number | Account creation rejected |
| Enter invalid PIN | Account creation rejected |
| Login with correct PIN | Login successful |
| Login with wrong PIN | Login rejected |
| Deposit valid amount | Balance increases |
| Deposit invalid amount | Error displayed |
| Withdraw within balance | Balance decreases |
| Withdraw above balance | Transaction rejected |
| Transfer to existing account | Transfer successful |
| Transfer to non-existing account | Error displayed |
| View transaction history | Transactions displayed |
| Restart program | Saved accounts are loaded |

---

## Future Enhancements

The project can be improved in the future by adding:

- Graphical User Interface using Tkinter
- SQLite or MySQL database
- Password/PIN hashing
- Admin login
- Account deletion
- Change PIN option
- Monthly bank statements
- Interest calculation
- Transaction IDs
- Search and filtering
- Better transfer records

---

## Conclusion

The Simple Banking System demonstrates how basic Python programming concepts can be combined to solve a practical problem.

The project provides experience with **classes, functions, dictionaries, lists, loops, conditions, JSON, file handling, validation, and exception handling**.

It also provides a foundation that can be expanded into a more advanced banking application in future semesters.

---

## Author

**Name:** Pratha Jain

**Roll Number:** 26BSA10046

**Course:** CSE_1021

**Semester:** First Semester

**College:** VIT BHOPAL

**Academic Year:** 2026-27
