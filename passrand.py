#Password Generator Project
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Gettig user input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

generated_password = ''

# For loop to generate letters, symbols and numbers used in standard password.

for letter in range(0, nr_letters):
  generated_password += random.choice(letters)

for symbol in range(0, nr_symbols):
  generated_password += random.choice(symbols)

for number in range(0, nr_numbers):
  generated_password += random.choice(numbers)



hard_pass_list = []
hard_pass_str = ''

# For loop to generate letters, symbols and numbers used in hard password.
for letter in range(0, nr_letters):
  hard_pass_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
  hard_pass_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
  hard_pass_list.append(random.choice(numbers))


# Checking lenth of hard password
pass_len = len(hard_pass_list)

for item in range(0, pass_len):
  hard_pass_list = random.sample(hard_pass_list, pass_len)

# Change orders of the letters, numbers and symbols.
random.shuffle(hard_pass_list)

hard_pass = hard_pass_str.join(hard_pass_list)


print(f'Your random password is: {hard_pass}')



