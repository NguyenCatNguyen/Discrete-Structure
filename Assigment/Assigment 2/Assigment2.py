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
f) Prove De Morgan’s Law for the Universal Quantifier where P(x) is the
statement “x<5”
2. Find the following truth values for the domain of {0,1,2,3,4,5,6,7,8,9,10}
where P(x,y): x ∙ y = 0. Show the values in the domain that either make the assertions true or false. (See Example 1 and 2 for “Order of Quantifiers” in the 9-1 lecture on Nested Quantifiers).
a) ∀x∀yP(x,y) b) ∀x∃yP(x,y) c) ∃x∀yP(x,y) d) ∃x∃yP(x,y)
• Print out a line between each of the above indicating which number your program is answering, (e.g., 1b).
• Provide comments that explain what each line of code is doing. See rubric below.


"""

#Part 1.
Dlist = [0,1,2,3,4,5,6,7,8,9,10]


# a) ∃x P(x), where P(x) is the statement “x<2”
"""
Create a loop

"""
def a(L):
    print("a) ∃x P(x), where P(x) is the statement “x<2. ")
    x = 0
    while x != 9:
        if L[x] < 2:
            print(f"If x = {L[x]} then the statement ∃x P(x) is truth. ").





# b) ∀x P(x), where P(x) is the statement “x<2”.
def b(L):


# c) ∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”

# d) ∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7”

# e) Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement “x<5”

# f) Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement “x<5”






#Part 2.
