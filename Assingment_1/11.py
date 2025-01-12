
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
