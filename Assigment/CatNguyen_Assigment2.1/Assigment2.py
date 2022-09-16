"""
Author: Nguyen Cat Nguyen
Date: 9/9/2022
Assigment: 2


Copy of Rubric2.docx with your name and ID filled out (do not submit a PDF)
2. Source code.
3. Screen print showing the successful execution of your code or copy and paste the
output from a console screen to a Word document and PDF it.
Assignment:
• You may use any language you want, but if you want help from me or one of the
SIs, you should probably use C++ or Python.
• Create a program for the following:
1. Prove (true) or disprove (false) the following assertions for the domain of {0,1,2,3,4,5,6,7,8,9,10}.
For the universal quantifier, show at least one of the numbers in the domain that disproves the assertion.
For the existential quantifier, show at least one number in the domain that proves the assertion:
a) ∃x P(x), where P(x) is the statement “x<2”
b) ∀x P(x), where P(x) is the statement “x<2”
c) ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is
the statement “x>7”
d) ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is
the statement “x>7”
e) Prove De Morgan’s Law for the Existential Quantifier where P(x) is
the statement “x<5”
f) Prove De Morgan’s Law for the Universal urceQuantifier where P(x) is the
statement “x<5”
2. Find the following truth values for the domain of {0,1,2,3,4,5,6,7,8,9,10}
where P(x,y): x ∙ y = 0. Show the values in the domain that either make the assertions true or false.
(See Example 1 and 2 for “Order of Quantifiers” in the 9-1 lecture on Nested Quantifiers).
a) ∀x∀yP(x,y) b) ∀x∃yP(x,y) c) ∃x∀yP(x,y) d) ∃x∃yP(x,y)
• Print out a line between each of the above indicating which number your program is answering, (e.g., 1b).
• Provide comments that explain what each line of code is doing. See rubric below.
"""


# Create and function for 2 input.
def AND(x,y):
    if x is True and y is True:
        return True
    else:
        return False
# Create or function for 2 input.
def OR(x,y):
    if x is True or y is True:
        return True
    else:
        return False
# Create not function for 2 input.
def NOT(x):
    if x:
        return False
    else:
        return True

# Create and form for list
def ANDF(A,B):
    x = 0
    count = 0
    while x!= len(A):
        if A[x] == True and B[x] == True:
            count+=1
        x += 1
    if count == len(A):
        L = [True]
    else:
        L = [False]
    return L

# Create or form for list
def ORF(A,B):
    x = 0
    count = 0
    L = []
    while x != len(A):
        if A[x] == True or B[x] == True:
            count += 1
        x += 1
    if count == len(A):
        L= [True]
    else:
        L = [False]
    return L

# Create not form for list.
def NOTF(A):
    L = []
    # Empty list to hold not value.
    for x in A:
        if x is True:
            L.append(False)
        else:
            L.append(True)
    # Return value after list have been change
    return L

#Part 1.
Domain = [0,1,2,3,4,5,6,7,8,9,10]

def P(x):
    #Function Declare
    return x<2
def Q(x):
    # Function Declare
    return x>7
def Z(x):
    # Function Declare
    return x<5


def Form(list,num):
    S = []
    if num == 1:
        # If x > 2, add the outcome to list S.
        for x in list:
            S.append(P(x))

    if num == 2:
        # If x > 7, add the outcome to list S.
        for x in list:
            S.append(Q(x))

    if num == 3:
        # If x < 5, add the outcome to list S.
        for x in list:
            S.append(Z(x))
    #Return the list of true or false
    return S



# Define for all.
def FA(list):
    return all(list)
# Define for some.
def FS(list):
    return any(list)

#Let the truth table for P(x) as P.
P = Form(Domain,1)
# a) ∃x P(x), where P(x) is the statement “x<2”
print("a) ∃x P(x), where P(x) is the statement “x<2”")
print(f"=> Answer: This statement is {FS(P)}.\n")
#print("")

# b) ∀x P(x), where P(x) is the statement “x<2”.
print("b) ∀x P(x), where P(x) is the statement “x<2”")
print(f"=> Answer: This statement is {FA(P)}.\n")


# c) ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”
print("c) ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7” ")
#Let the truth table for Q(x): x > 7
Q = Form(Domain,2)
print(f"=> Answer: This statement is {OR(FS(P),FA(Q))}.\n")

# d) ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”
print("d) ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7” ")
print(f"=> Answer: This statement is {FA(ORF(P,Q))}.\n")

"""
e) Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement “x<5”
De Morgan’s Law: !∃x (P(x)) => ∀x !(P(x))
"""
#Let the truth table for Q(x): x < 5
Z = Form(Domain,3)
print("e) De Morgan’s Law: !∃x (P(x)) => ∀x !(P(x))")
print(f"We have the value for !∃x (P(x)) is {NOT(FS(Z))} and ∀x !(P(x)) is {FA(NOTF(Z))}")
print(f"=> Answer: This statement is {AND(NOT(FS(Z)),FA(NOTF(Z)))}.\n")
"""
f) Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement “x<5”
De Morgan’s Law: !∀x (P(x)) => ∃x (!P(x))
"""
print("f) De Morgan’s Law: !∀x (!P(x)) => ∃x (P(x))")
print(f"We have the value for !∀x (P(x)) is {NOT(FA(Z))} and the statement for ∃x (P(x)) is {FS(NOTF(Z))}")
print(f"=> Answer: This statement is {AND(NOT(FA(Z)),FS(NOTF(Z)))}\n")


#Part2: P(x,y): x ∙ y = 0.
#Declare function x*y = 0

def T(A,B):
    #
#a) ∀x∀yP(x,y)

# b) ∀x∃yP(x,y)
# c) ∃x∀yP(x,y)
# d) ∃x∃yP(x,y)
