import random
uppercase_letters = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.;:-/\\@#$%^&*?"

upper, lower, nums, syms = True, True, True, True

all = ""
x = list(map(int, input("Do you want to include alphabets(1), digits(2), symbols(3): ").split()))
if x[0] == 1:
    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
if x[1] == 2:
    if nums:
        all += digits
if x[2] == 3:
    if syms:
        all += symbols

length = int(input("Enter the length of the password: "))
password = "".join(random.sample(all, length))
print(password)