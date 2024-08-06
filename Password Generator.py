import random

print('Welcome to Password Generator')
chars = 'abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ!@#$%^&*:;1234567890'
numbers = input("Amount of Password  want: ")
numbers = int(numbers)
length = input("Length of Password You Want: ")
length = int(length)

print("\n Here Your password:")

for i in range(numbers):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    print(password)