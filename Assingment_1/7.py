#7.1
with open('example.txt', 'w') as file:
    file.write('Hi, welcome to this file.\n')
    file.write('This is the second line.\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

#7.2
with open('example.txt', 'a') as file:
    file.write('This is the thrid line.\n')

with open('example.txt', 'r') as file:
    updated_content = file.read()
    print(updated_content)

#7.3
with open('example.txt', 'r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print(f'The number of lines in the file is: {line_count}')


