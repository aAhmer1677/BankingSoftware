# Banking Software (Python CLI)

A simple command-line banking simulation written in Python. The app supports account registration, login verification, deposits, withdrawals, and balance checks using text files for storage.

## Features

- User registration with a 10-digit PIN
- Account-based login
- Two-step verification for sensitive actions:
- Random 3-digit position check from the PIN
- Time-based OTP (valid for 2 minutes)
- Deposit cash
- Withdraw cash (with insufficient balance protection)
- Check account balance
- Transaction history logging

## Project Structure

- `main.py`: Main banking application flow
- `otp_gen.py`: Helper script to generate a valid OTP for testing
- `user_usernames.txt`: Stores usernames (1 line per account)
- `user_pins.txt`: Stores PINs (1 line per account)
- `user_cash.txt`: Stores balances (1 line per account)
- `transactions_history.txt`: Stores activity logs

## Requirements

- Python 3.8+
- No external dependencies (standard library only)

## How To Run

1. Open a terminal in the project folder:
```powershell
cd "c:\Bulu Ahmer\Banking Software"
```
2. Start the main app:
```powershell
python main.py
```

## OTP Flow (Important)

The application asks for a 6-digit OTP during login and before sensitive actions. OTP is generated from:

- Account number
- Full PIN
- Current 2-minute time window

To generate a matching OTP for testing:

```powershell
python otp_gen.py
```

Then enter the same account number and full PIN to get the OTP and paste it into `main.py` when prompted.

## Usage Overview

1. Run `main.py`
2. Enter account number
- Enter `-1` to register a new account
3. Complete PIN-position verification and OTP check
4. Choose an option:
- `1` Deposit cash
- `2` Withdraw cash
- `3` Check balance
- `4` Terminate session

## Notes

- Data is stored in plain text files for learning/demo purposes.
- Account number maps to line number in the data files.
- `main.py` auto-creates required `.txt` files if missing.
- This project is not production-ready security-wise.

## Future Improvements

- Hash and salt PINs instead of storing plain text
- Add input validation for usernames and account fields
- Add unit tests
- Use a real database (SQLite/PostgreSQL)
- Add transfer between accounts

