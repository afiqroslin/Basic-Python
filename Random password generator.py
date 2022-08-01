import random

lower = "qwertyuiopasdfghjklzxcvbnm"

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"

numbers = "0123456789"

symbols = "@#-_"


alphabet = "".join(random.sample(lower + upper, 5))
number = "".join(random.sample(numbers + symbols, 5))

all = alphabet + number
print(all)