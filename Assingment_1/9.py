
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
random.shuffle(nums)
print("The shuffled list of numbers is: ", nums)

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
