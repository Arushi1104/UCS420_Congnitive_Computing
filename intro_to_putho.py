# 1
print("Anything You find cool.")

# 2.1
num1 = 5
num2 = 3
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

#2.2
string1 = "Los"
string2 = "Angeles"
result = string1 + " " + string2
print(result)

#2.3
string = "number of pineapples"
number = 42
print(string + " " + str(number))

#3.1
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#3.2
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#4.1
for i in range(1, 11):
    print(i)

#4.2
i = 1
while i <= 10:
    print(i)
    i += 1

#4.3
sum = 0
for i in range(1, 101):
    sum += i

print("The sum from 1 to 100: ", sum)

#5.1
numbers = [13, 25, 58, 47, 19]
largest = max(numbers)
smallest = min(numbers) 

print("The largest number is:", largest)
print("The smallest number is:", smallest)

#5.2
my_dict = {"name": "Anjali", "age": 30, "city": "Jodhpur"}

key = "city"
value = my_dict.get(key)

print("The value of the key", key, "is:", value)

#5.3
numbers = [10, 25, 3, 47, 19]
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("The list in ascending order is:", ascending)
print("The list in descending order is:", descending)

#5.4
dict1 = {"name": "Anjali", "age": 30}
dict2 = {"city": "Jodhpur", "country": "India"}

merged_dict = {**dict1, **dict2}

print("The merged dictionary is:", merged_dict)

#6.1
string = "eutopia"
vowel_count = 0
vowels = "aeiouAEIOU"

for char in string:
    if char in vowels:
        vowel_count +=1

print("The number of vowels: ", vowel_count)

#6.2
string = "The quick brown fox jumps over the lazy dog"
reversed_string = string[::-1]
print("The reversed string is:", reversed_string)

#6.3
string = "kayak"
string1=string[::-1]
if string == string1:
    print("A palindrome.")
else:
    print("Not a palindrome.")

#7.1
with open("example.txt", "w") as file:
    file.write("Hi everyone, this is the first line.\nThis is the second line.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#7.2
with open("example.txt", "a") as file:
    file.write("\nThis is a new line.")

with open("example.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)

# #7.3
# with open("example.txt", "r") as file:
#     line_count = sum(1 for line in file)

# print("The number of lines in the file is:", line_count)

#8.1
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

num1 = 10
num2 = 0
print("Result: ", divide(num1, num2))

#8.2
def get_number():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        return "Error: Invalid input. Please enter a valid number."
    return number

print("Number is:", get_number())

#8.3
def demonstrate_finally():
    try:
        file = open("example.txt", "r")
        content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        print("This block will always execute.")
        if 'file' in locals():
            file.close()

demonstrate_finally()

#9.1
import random
random_nums = [random.randint(1, 100) for _ in range(5)]
print("The random numbers are:", random_nums)

# 9.2
import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

random_num = random.randint(1, 100)

if is_prime(random_num):
    print(f"The random number {random_num} is a prime number.")
else:
    print(f"The random number {random_num}  is not a prime number.")

# 9.3
import random
die_roll = random.randint(1, 6)
print("The result of rolling the die is:", die_roll)

# 9.4
import random
nums = [55, 23, 12, 125, 2345, 2, 346, 358,979]
print("The unshuffled list of number is: ", nums)

print("The shuffled list of numbers is: ", random.shuffle(numbers))

# 9.5
import random
items = ["apple", "banana", "cherry", "date", "blackberry"]
selected_item = random.choice(items)
print("The randomly selected item is:", selected_item)

# 9.6
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 8

random_password = generate_password(password_length)
print("The random password is:", random_password)

# 9.7
import random
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [rank + " of " + suit for suit in suits for rank in ranks]
selected_card = random.choice(deck)

print("The randomly selected card is:", selected_card)

#10.1
import sys
if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("The sum of", num1, "and", num2, "is", num1+num2)

#10.2
import sys
if len(sys.argv) != 2:
    print("Usage: python script.py <string>")
    sys.exit(1)

input_string = sys.argv[1]

print("The length of the string is:", len(input_string))

#11.1
import math

num = 16
sqrt = math.sqrt(num)
print("The square root of", num, "is", sqrt)

#11.2
from datetime import datetime
current_datetime = datetime.now()
print("The current date and time is:", current_datetime)

#11.3
import os

files = os.listdir()

print("The files in the current directory are:")

for file in files:
    print(file)
