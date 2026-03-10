from datetime import datetime
import random
import time
import hashlib
import os


FILES = [
    "user_usernames.txt",
    "user_pins.txt",
    "user_cash.txt",
    "transactions_history.txt"
]

def ensure_files():
    for f in FILES:
        if not os.path.exists(f):
            open(f, "w").close()

ensure_files()


def read_line(filename, line):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
    return lines[line - 1]

def read_all(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

def write_append(filename, content):
    with open(filename, "a") as file:
        file.write("\n" + content)

def change_line(filename, line, new_value):
    data = read_all(filename)
    data[line - 1] = str(new_value)
    with open(filename, "w") as file:
        file.write("\n".join(data))

# ---------- TIME ----------

def get_time_of_day():
    hour = datetime.now().hour
    if hour < 12:
        return "Morning"
    elif hour < 18:
        return "Afternoon"
    else:
        return "Evening"

# ---------- OTP ----------

def generate_expected_otp(account_number, pin):
    time_window = int(time.time() // 120)
    raw = f"{account_number}{pin}{time_window}"
    return hashlib.sha256(raw.encode()).hexdigest()[:6]

# ---------- SECURITY ----------

def credentials_check(accountN, user_name, action):
    user_pin = read_line("user_pins.txt", accountN)
    checks = []
    while True:
        r = random.randint(1, len(user_pin))
        if r not in checks:
            checks.append(r)
        if len(checks) == 3:
            break
    positions = sorted(checks)
    print(
        f"\nGood {get_time_of_day()}, {user_name}. "
        f"To confirm {action}, enter PIN digits at positions: {positions}"
    )

    for pos in positions:
        if input(f"Digit {pos}: ") != user_pin[pos - 1]:
            print("Access Denied")
            return False
    expected_otp = generate_expected_otp(accountN, user_pin)

    otp_input = input("Enter your 6-digit OTP: ")
    if otp_input != expected_otp:
        print("Invalid or expired OTP")
        return False

    print("Access Granted")
    return True


def deposit(user_name, account_number, amount):
    if not amount.isdigit():
        print("Invalid amount.")
        return options(user_name, account_number)

    if not credentials_check(account_number, user_name, f"depositing ${amount}"):
        return options(user_name, account_number)

    balances = read_all("user_cash.txt")
    new_balance = int(balances[account_number - 1]) + int(amount)
    change_line("user_cash.txt", account_number, new_balance)

    write_append(
        "transactions_history.txt",
        f"{user_name} deposited ${amount} on {datetime.now()}"
    )

    print(f"Transaction Completed.\nNew balance: ${new_balance}")
    options(user_name, account_number)

def withdrawl(user_name, account_number, amount):
    if not amount.isdigit():
        print("Invalid amount.")
        return options(user_name, account_number)

    balances = read_all("user_cash.txt")
    current_balance = int(balances[account_number - 1])

    if int(amount) > current_balance:
        print("Insufficient funds.")
        return options(user_name, account_number)

    if not credentials_check(account_number, user_name, f"withdrawing ${amount}"):
        return options(user_name, account_number)

    new_balance = current_balance - int(amount)
    change_line("user_cash.txt", account_number, new_balance)

    write_append(
        "transactions_history.txt",
        f"{user_name} withdrew ${amount} on {datetime.now()}"
    )

    print(f"Transaction Completed.\nNew balance: ${new_balance}")
    options(user_name, account_number)

def check_balance(user_name, account_number):
    if credentials_check(account_number, user_name, "checking balance"):
        balances = read_all("user_cash.txt")
        print(f"{user_name}, your balance is ${balances[account_number - 1]}")
    options(user_name, account_number)


def login(user_name, account_number):
    if credentials_check(account_number, user_name, "logging in"):
        options(user_name, account_number)

def registration():
    print("\n--- Registration ---")
    user_name = input("Enter your name: ")

    while True:
        pin = input("Create a 10-digit PIN: ")
        if pin.isdigit() and len(pin) == 10:
            break
        print("PIN must be exactly 10 digits.")

    account_number = len(read_all("user_pins.txt")) + 1

    write_append("user_usernames.txt", user_name)
    write_append("user_pins.txt", pin)
    write_append("user_cash.txt", "0")

    print("\nRegistration successful!")
    print(f"Your account number is: {account_number}\n")

    write_append(
        "transactions_history.txt",
        f"A new account has been made by {user_name} with Account Number with {account_number} on {datetime.now()}"
    )

    login(user_name, account_number)


def options(user_name, account_number):
    print(
        "\n1. Deposit Cash\n"
        "2. Withdraw Cash\n"
        "3. Check Balance\n"
        "4. Terminate Session"
    )

    choice = input("Choose option: ")
    if not choice.isdigit():
        print("Invalid choice.")
        return options(user_name, account_number)

    choice = int(choice)

    if choice == 1:
        deposit(user_name, account_number, input("Amount: "))
    elif choice == 2:
        withdrawl(user_name, account_number, input("Amount: "))
    elif choice == 3:
        check_balance(user_name, account_number)
    else:
        print("Session ended.")
        exit()


def landing():
    print("Welcome to Online Banking")
    acc = input("Enter account number (-1 to register): ")

    if not acc.lstrip("-").isdigit():
        print("Invalid input.")
        return landing()

    account_number = int(acc)

    if account_number == -1:
        registration()
        return

    users = read_all("user_usernames.txt")
    if account_number < 1 or account_number > len(users):
        print("Invalid account number.")
        return landing()

    user_name = users[account_number - 1]
    print(f"Welcome back, {user_name}")
    login(user_name, account_number)

landing()
