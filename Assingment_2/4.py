A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

# i. 
union_scores = A.union(B)
print(f"Unique scores achieved by both teams are: {union_scores}")

# ii. 
common_scores = A.intersection(B)
print(f"Scores that are common to both teams are: {common_scores}")

# iii. 
# symmetric diff==elements that are in either of the sets, but not in their intersection
exclusive_scores = A.symmetric_difference(B)
print(f"Scores that are exclusive to each team are: {exclusive_scores}")

# iv.
is_A_subset_of_B = A.issubset(B)
is_B_superset_of_A = B.issuperset(A)
print(f"Are the scores of team A a subset of team B? {is_A_subset_of_B}")
print(f"Are the scores of team B a superset of team A? {is_B_superset_of_A}")

# v. 
X = int(input("Enter the specific score to to remove from set A:"))
if X in A:
    A.remove(X)
    print(f"The score {X} has been removed from set A. The updated set A is: {A}")
else:
    print(f"The score {X} is not present in set A.")
