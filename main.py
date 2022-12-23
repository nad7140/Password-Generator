import random
import string

print("Hello, Welcome to Password Generator :)")

length = int(input("Enter the lenght of the Password: "))

lower = string.ascii_lowercase
upper = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

mix_str = lower+upper+numbers+symbols

rand = random.sample(mix_str,length)

password = "".join(rand)

print("Password: "+ password)
