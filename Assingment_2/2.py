scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

# i.
highest_score = max(scores)
highest_index = scores.index(highest_score)
print(f"The highest score : {highest_score}, index: {highest_index}.")

# ii. 
lowest_score = min(scores)
lowest_count = scores.count(lowest_score)
print(f"The lowest score: {lowest_score}, appears: {lowest_count} times.")

# iii.
reversed_list = list(scores[::-1])
print(f"The reversed tuple as a list: {reversed_list}.")

# iv. 
x = int(input("Enter the number to check:  "))
if x in scores:
    index_first = scores.index(x)
    print(f"The score {x} is present, first occurrence index: {index_first}.")
else:
    print(f"The score {x} is not present in the tuple.")
