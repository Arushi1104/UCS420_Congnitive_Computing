import random
l = []
for num in range(100):
    l.append(random.randint(100,901))

# i.
odd = [number for number in l if number % 2 != 0]
print('No.of odd elemnts:', len(odd))
print(odd)

# ii. 
print('\n')
even = [number for number in l if number % 2 == 0]
print('No.of even elemnts:', len(even))
print(even)

# iii. 
print('\n')
prime = [num for num in l if num >1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
print('No.of prime elemnts:', len(prime))
print(prime)