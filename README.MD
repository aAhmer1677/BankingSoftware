# Banking Software (Python CLI)

A command-line banking simulation built with Python. This project demonstrates basic account operations, lightweight verification, and file-based data persistence.

## Features

- Account registration with a 10-digit PIN
- Login and operation verification
- PIN digit-position challenge (3 random positions)
- Time-based OTP (6 digits, valid for 2 minutes)
- Deposit funds
- Withdraw funds with balance checks
- View account balance
- Transaction history logging

## Tech Stack

- Python 3.8+
- Standard library only (no external packages)

## Repository Structure

- `main.py` - Main application entry point and banking workflows
- `otp_gen.py` - Utility script to generate OTP for testing/demo
- `user_usernames.txt` - Username records (line-based)
- `user_pins.txt` - PIN records (line-based)
- `user_cash.txt` - Balance records (line-based)
- `transactions_history.txt` - Transaction and account activity logs

## Getting Started

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. Run the main application:

```bash
python main.py
```

## How OTP Works

The OTP is generated using:

- Account number
- Full PIN
- Current 2-minute time window

To generate a matching OTP during testing:

```bash
python otp_gen.py
```

Use the same account number and full PIN when prompted so the OTP matches what `main.py` expects.

## Usage Flow

1. Start the app with `python main.py`.
2. Enter account number.
3. Enter `-1` if you want to register a new account.
4. Complete the PIN-position check and OTP verification.
5. Choose an operation (`1` Deposit, `2` Withdraw, `3` Check Balance, `4` Terminate Session).

## Important Notes

- This project stores data in plain text files.
- Account numbers map directly to line numbers across data files.
- Missing data files are auto-created on startup.
- This is for learning/demo use, not production banking.


## License

This project is licensed under the MIT License. See `LICENSE` for details.
