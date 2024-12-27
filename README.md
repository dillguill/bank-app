# Class Based Python Banking App

## Overview
This project is a simple Bank Account management program written in Python. It allows users to perform basic banking operations such as depositing and withdrawing funds, while keeping a record of all transactions in a log file. It is designed to demonstrate foundational Python programming concepts such as object-oriented programming, input handling, and file operations.

## Features
- Allows users to:
  - **Deposit** funds into their account.
  - **Withdraw** funds from their account.
  - **View account balance**.
  - Quit the program at any time.
- Includes input validation to handle invalid entries and ensure valid transactions.
- Logs all transactions (deposits and withdrawals) into a file named `transactions.txt`.
- Demonstrates key Python concepts:
  - **Object-Oriented Programming**: Encapsulation and methods in the `BankAccount` class.
  - **File handling**: Writing transaction logs to a text file.
  - **Error handling**: Ensures only valid amounts can be deposited or withdrawn.
  - **User interaction**: Interactive input prompts for a smooth user experience.

## What I Learned
- How to implement object-oriented programming in Python by creating and managing a `BankAccount` class.
- Using methods to encapsulate behavior like deposits, withdrawals, and transaction logging.
- Handling files in Python to log data persistently.
- Enhancing input validation for a better user experience.
- Using Python's `__str__` method to create user-friendly string representations of objects.

## Example Usage
```text
Enter 'd' to deposit, 'w' to withdraw, or 'q' to quit: d
Enter amount: 100
Deposited $100. New balance: $100.0

Enter 'd' to deposit, 'w' to withdraw, or 'q' to quit: w
Enter amount: 50
Withdrew $50. New balance: $50.0

Enter 'd' to deposit, 'w' to withdraw, or 'q' to quit: q
```

## How to Run
1. Ensure you have **Python 3.9+** installed on your system. You can download it from [python.org](https://python.org).
2. Save the `bank_account.py` file on your computer.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Run the program using the command:
   ```bash
   python bank_account.py
   ```

## Credits
This project was based on the instructions from the Python section of the [Ultimate 2024 Fullstack Web Development Bootcamp](https://www.udemy.com/course/the-ultimate-fullstack-web-development-bootcamp/) on Udemy. Special thanks to the instructor **Kalob Taulien** for his guidance.
