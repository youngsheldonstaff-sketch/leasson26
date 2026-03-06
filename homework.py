import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(/.,!@#$%^&*"


length = 12
password_list = [random.choice(chars) for _ in range(length)]

password = "".join(password_list)

print(password)