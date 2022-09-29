"""

You may use any language you want, but if you want help from me or one of the
SIs, you should probably use C++ or Python.
• Label each output with a description, e.g., “1a. Union of R1 and R2”
• Use the methods or functions inherent in the language and/or using methods or
functions you create. Like previous assignments, don’t “hard code” a solution you
did on paper as the output.
• Create a program for the following:
1. For the relations:
R1 = {(1,1), (2,2), (3,3)} and R2 = {(1,1), (1,2), (1,3), (1,4)} perform the following set operations and display the results:
a) R1∪R2 b) R1∩R2 c) R1−R2 d) R2−R1
2. Display S ◦ R, where:
R is the relation from A = {1, 2, 3} to B = {1, 2, 3, 4} with R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}
S is the relation from B = {1, 2, 3, 4} to C = {0, 1, 2} with S = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)} 2
.
4. For the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}:
3. For R = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)}, show R
a) Show R as a set of ordered pairs.
b) Show whether R is reflexive or not.
c) Show whether R is symmetric or not.
d) Show whether R is antisymmetric or not. e) Show whether R is transitive or not.
• Provide comments that explain what each line of code is doing. See rubric below.
"""

"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Tuesday September 27, 2022
"""



#Main function space (need more comment on function)

#Function to find the union of two list of tuples (Part1)
def union(R1, R2):
    #Put all value of R1 and R2 into list U.
    U = R1 + R2
    #Using set function to remove duplicates and convert back to list.
    U = list(set(U))
    return U


#Function to find the intersection of two list of tuples (Part1)
def intersection(R1, R2):
    I = [x for x in R1 if x in R2]
    #Create I list that hold x value if x value in both R1 and R2.
    return I

#Function to find the difference of two list of tuples (Part1)
def difference(R1, R2):
    D = [x for x in R1 if x not in R2]
    #Create D list that hold x value for x value in R1 but not in R2.
    return D

#Function to find the composition of two list of tuples (Part3 and Part 2)
def composition(S, R):
    C = []
    #Create an empty list to hold the composition of two list.
    for x in R:
        for y in S:
            #Loop throught all the value in S.
            if x[1] == y[0]:
                #if x[1] = y[0] then add the value of (x[0],y[1]) to empty list C
                C.append((x[0], y[1]))
    return C


#Function to show M as a set of ordered pairs.(Part4).
def order_pair(M):
    #Create an empty list to hold the value of ordered pairs.
    OP = []
    for (x,y) in M:
        OP.extend([(x,x), (y,y) , (x,y), (y,x)])
    OP = list(set(OP))
    return OP

#Function that check to see if list is reflexive or not.(Part4)
def reflexive(M,A):
    for x in A:
        if (x,x) in M:
            return True
        else:
            return False
            




#Part 1 of the assigment.
#Let create two list of tuples R1 and R2.
R1 = [(1,1), (2,2), (3,3)]
R2 = [(1,1), (1,2), (1,3), (1,4)]

print("1. Perform the following set operations and display the results: \n")
#Print out the result for R1 and R2.
print(f"a) R1 U R2 : {union(R1, R2)}\n")
print(f"b) R1 ∩ R2 : {intersection(R1, R2)}\n")
print(f"c) R1 - R2 : {difference(R1, R2)}\n")
print(f"d) R2 - R1 : {difference(R2, R1)}\n")




#Part 2 of the assigment.
#Let create two list of tuples R and S
R = [(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)]
S = [(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)]
print(f"2. Display S ◦ R:\n")
print(f"=> S ◦ R = {composition(S, R)}\n")


#Part 3 of the assigment.
# For R = [(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)], show R ◦ R
print("3. Display R ◦ R\n")
print(f"=> R ◦ R = {composition(R,R)}\n")

#Part 4 of the assigmnet.
# For the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}:

#Create a list of tuples M that hold all the value of x and y that satisfy the condition x + y = 0.
M = [(x,y) for x in range(-10,11) for y in range(-10,11) if x + y == 0]
#Declare set A that hold all the value from -10 to 10.
A = set(range(-10,11))
#a) Show R as a set of ordered pairs.
print("a) Show R as a set of ordered pairs.\n")
print(f"=> R = {order_pair(M)}\n")
#b) Show whether R is reflexive or not.
print("b) Show whether R is reflexive or not.\n")

    
print(f"=> R is reflexive: {reflexive(M,A)}\n")