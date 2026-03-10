import time
import hashlib

def generate_otp(account_number, pin):
    time_window = int(time.time() // 120)
    raw = f"{account_number}{pin}{time_window}"
    return hashlib.sha256(raw.encode()).hexdigest()[:6]

print("OTP Generator")
account_number = input("Account number: ")
pin = input("Full PIN: ")

otp = generate_otp(account_number, pin)
print("\nYour OTP (valid for 2 minutes):", otp)
