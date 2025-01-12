
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

#7.3
with open("example.txt", "r") as file:
    line_count = sum(1 for line in file)

print("The number of lines in the file is:", line_count)
