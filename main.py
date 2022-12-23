import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~!@#$%^&*()_-+=`./<>]["

mix_str = lower+upper+numbers+symbols

password = "".join(random.sample
                (mix_str,18)) #here if you need increase of length of a password u can increase
print("Password: "+ password)
