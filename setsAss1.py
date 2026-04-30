"""Q1. Write a Python program to create two sets, A and B, and find the elements
that are common to both sets. """
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A&B)#intersection

"""Q2. Write a Python program to create two sets, X and Y, and find the elements
that are unique to each set (not present in both)."""

X = {10, 20, 30, 40}
Y = {30, 40, 50, 60}

print((X|Y)-(X&Y))


# Q3. Write a Python program to check if all elements of one set are contained
# within another set. 
S1 = {1, 2, 3}
S2 = {1, 2, 3, 4, 5}
if(S1&S2==S1):
    print("True")
else:
    print("False")

# Q4. Write a Python program which create a new set from given two sets have
# only that elements which are not common. 
A = {2, 4, 3}
B = {1, 3, 5}
C= set((A|B)-(A&B))
print(C)

# Q5. Write a Python program to combine all elements from three different sets
# into one.
Set1 = {1, 2}
Set2 = {2, 3}
Set3 = {3, 4}
print((Set1|Set2)|Set3)

# Q6. Write a Python program to find all elements that are in one set but not in
# another.
A = {10, 20, 30}
B = {20, 30, 40}
print((A|B)-(A&B))


# Q7. Write a Python program to remove a specific element(n) from a set, but
# only if it exists in the set.
S = {1, 2, 3, 4, 5}
# Test case 1: n = 2
# Test case 2: n = 7 
S.discard(2) #discard do not throw error if element do not exist in the set and if it exist then it will delete it
#remove is not better for deeeletion and discard is better 
S.discard(7)
print(S)