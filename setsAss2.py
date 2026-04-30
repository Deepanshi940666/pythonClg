# Q1. Write a program to multiply all the float element in the set. set should be
# taken as input such that a set should contain integer float and string element.
# Input:- Enter a set:-{5, 'abc', 7, 8.0, 'def', '10.0', 11, 12.0, '123', 14.0}
# Output:- 1344.0

A=eval(input("Enter a set: "))
print(A)
result=1
for i in A:
    if isinstance(i, (float)):
        result *= i

print(result)

# Q2. Write a program to add all the integer element in a set and set should be
# taken as input such that a set should contain integer float and string element.
# Input:- Enter a set:-{5, 'abc', 7, 8.0, 'def', '10.0', 11, 12.0, '123', 14.0}
# Output:- 23

A=eval(input("Enter a set: "))
print(A)
result=0
for i in A:
    if isinstance(i, (int)):
        result += i

print(result)

# Q3. Write a Python program to convert all the even number of a set into a
# string and set should be user defined.
# Input:- Enter a set:-{5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# Output:- {'10', 5, 7, 9, 11, 13, '14', '6', '8', '12'}

A=eval(input("Enter a set: "))
B=set()
print(A)
result=0
for i in A:
    if(type(i)==(int)):
        if(i%2==0):
           B.add(str(i))
        else:
            B.add(i)

print(B)

# Q4. Write a Python program to convert all the odd number of a set into a float
# and set should be user defined.
# Input:- Enter a set:-{5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
# Output:-{5.0, 6, 7.0, 8, 9.0, 10, 11.0, 12, 13.0, 14}

A=eval(input("Enter a set: "))
B=set()
print(A)
result=0
for i in A:
    if(type(i)==(int)):
        if(i%2!=0):
           B.add(float(i))
        else:
            B.add(i)

print(B)

# Q5. Write a program to convert all the integer element of a set into float and
# the float element of a set into integer and set should be user defined
# Input:- {5.0, 6, 7.0, 8, 9.0, 10, 11.0, 12, 13.0, 14}
# Output:- {5, 6.0, 7, 8.0, 9, 10.0, 11, 12.0, 13, 14.0}


A=eval(input("Enter a set: "))
B=set()
print(A)
result=0
for i in A:
    if(type(i)==(int)):
           B.add(float(i))
    else:
            B.add(int(i))
print(B)