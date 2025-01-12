
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
