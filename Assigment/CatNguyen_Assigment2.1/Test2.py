"""
Author: Cat Nguyen
Date: 9/9/2022
Assigment: 2
"""

# Make and, or, not function
def AND(x,y):
    if x is True and y is True:
    # If x and y is true, return true.
        return True
    else:
        return False

def OR(x,y):
    if x is True or y is True:
    # If x or y is true, return true.
        return True
    else:
        return False

def NOT(x):
    if x:
    # If x is true, return false.
        return False
    else:
        return True

# Make and, or, not function for list.
def ANDF(A,B):
     #Set initial value for x and count.
    x = 0
    count = 0
    #Make an empty list to hold value.
    L = []
    while x!= len(A):
        if A[x] == True and B[x] == True:
            #If A[x] and B[x] is true, add 1 to count.
            count+=1
        x += 1
    if count == len(A):
        #If count is equal to length of A, return true.
        L = [True]
    else:
        L = [False]
    return L

def ORF(A,B):
    #Set initial value for x and count.
    x = 0
    count = 0
    L = []
    while x != len(A):
        if A[x] == True or B[x] == True:
            #If A[x] or B[x] is true, add 1 to count.
            count += 1
        x += 1
    if count == len(A):
        #If count is equal to length of A, return true.
        L= [True]
    else:
        L = [False]
    return L

def NOTF(A):
    L = []
    # Empty list to hold not value.
    for x in A:
        if x is True:
            L.append(False)
        else:
            L.append(True)
    return L


"""
Part1: Prove (true) or disprove (false) the following assertions for the domain 
of {0,1,2,3,4,5,6,7,8,9,10}. For the universal quantifier, show at least 
one of the numbers in the domain that disproves the assertion.For the existential 
quantifier, show at least one number in the domain that proves the assertion:

"""

#list of domain
Domain = [0,1,2,3,4,5,6,7,8,9,10]

# Function that part 1 provide.
def P(x):
    return x < 2

def Q(x):
    return x > 7

def Z(x):
    return x < 5

# A method that return a list of true and false value.
def LTF(domain,num):
    S = []
    if num == 1:
        # If x > 2, add the outcome to list S.
        for x in domain:
            S.append(P(x))

    if num == 2:
        # If x > 7, add the outcome to list S.
        for x in domain:
            S.append(Q(x))

    if num == 3:
        # If x < 5, add the outcome to list S.
        for x in domain:
            S.append(Z(x))
    return S

# Define for all value in domain equal to true, return true.
def ForAll(domain,num):
    return all(LTF(domain,num))

# Define for some value in domain equal to true, return true.

def ForSome(domain,num):
    return any(LTF(domain,num))

# Print a single example of ForALl or Forsome.
def Print(domain,num):
    if num == 1:
        print(f"P(x) is {domain} when x = 1")
    if num == 2:
        print(f"Q(x) is {domain} when x = 8")
        print(f"Z(x) is {domain} when x = 9")



# a) ∃x P(x), where P(x) is the statement “x<2”
print("a) ∃x P(x), where P(x) is the statement “x<2”")
print(f"=> Answer: This statement is {FS(P)}.\n")
#print("")
