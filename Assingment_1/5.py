
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
