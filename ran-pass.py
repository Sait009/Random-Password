import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]{\"}|/.,1234567890-=_+!@#$%^&*()<>?';:"
password = ""
i = int(input("Plase input range for password : "))
for x in range(i):
    password += random.choice(chars)
print("your password: " + password)
