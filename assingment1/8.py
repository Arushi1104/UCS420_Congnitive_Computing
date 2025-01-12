
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
