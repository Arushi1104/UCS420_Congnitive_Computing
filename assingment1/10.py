
#10.1
import sys

if len(sys.argv) != 3:
    print("Usage: python 10.py <num1> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print(f"The sum of {num1} and {num2} is {num1 + num2}")

#10.2
import sys
if len(sys.argv) != 2:
    print("Usage: python intro_to_python.py <string>")
    sys.exit(1)

input_string = sys.argv[1]

print("The length of the string is:", len(input_string))
