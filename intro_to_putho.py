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

key = "age"
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