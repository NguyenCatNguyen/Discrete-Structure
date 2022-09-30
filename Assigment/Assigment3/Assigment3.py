"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Tuesday September 27, 2022
Assignment: Assignment 3
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


#Function to show M as a set of ordered pairs.(Part4.a).
def order_pair(M):
    #Create an empty list to hold the value of ordered pairs.
    OP = []
    for (x,y) in M:
        OP.extend([(x,x),(y,y),(x,y),(y,x)])
    #Using extend method to add the value of ordered pairs to the empty list.
    OP = list(set(OP))
    #Using set method to remove duplicates and convert back to list.
    return OP


#Function that check to see if list is reflexive or not.(Part4.b)
def reflexive(M,set):
    count = 0
    for x in set:
        if (x,x) in M:
            #Check if (x,x) in M then count + 1.
            count += 1
    if count == len(set):
        #Check if all the value in set satisfy the condition above are in M.
        return True
    else:
        return False
          

#Function that check to see if list is symmetric or not.(Part4.c)
def symmetric(M):
    #going through list M and check if (x,y) in M and (y,x) in M then return True.
    #Check all the value in M that satisfy the condition above.
    count = 0
    for (x,y) in M:
        if (y,x) in M:
            count += 1
    if count == len(M):
        return True
    else:
        return False

    

#Function that check to see if list is antisymmetric or not.(Part4.d)
def antisymmetric(M):
    count = 0
    for (x,y) in M:
        if (y,x) in M:
            #check if (y,x) in M, if yes then check if x = y.
            if x == y:
                count += 1
    if count == 0:
        return True
    else:
        return False
    


#Function that check to see if list is transitive or not.(Part4.e)
def transitive(M,S):
    #For x,y,z in set S, check if (x,y) in M and (y,z) in M then (x,z) in M.
    #Check all the value in M that satisfy the condition above.
    count = 0
    for x in S:
        for y in S:
            for z in S:
                if (x,y) in M and (y,z) in M:
                    if (x,z) in M:
                        count += 1
    if count == len(S)**3:
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

#Declare set A that hold all the value from -10 to 10.
A = set(range(-10,11))


#Create a list of tuples M that hold all the value of x and y that satisfy the condition x + y = 0.
M = [(x,y) for x in A for y in A if x + y == 0]


print("4. For the relation R = {(x, y) | x + y = 0} on the set {-10, ..., -1, 0, 1, ..., 10}:\n")
print(f"Set A = {A}\n")
print(f"List of tuples R = {M}\n")



#a) Show R as a set of ordered pairs.
print("a) Show R as a set of ordered pairs.")
print(f"=> R = {order_pair(M)}\n")
#b) Show whether R is reflexive or not.
print("b) Show whether R is reflexive or not.")
print(f"=> R is reflexive: {reflexive(M,A)}\n")
#c) Show whether R is symmetric or not.
print("c) Show whether R is symmetric or not.")
print(f"=> R is symmetric: {symmetric(M)}\n")
#d) Show whether R is antisymmetric or not.
print("d) Show whether R is antisymmetric or not.")
print(f"=> R is antisymmetric: {antisymmetric(M)}\n")
#e) Show whether R is transitive or not.
print("e) Show whether R is transitive or not.")
print(f"=> R is transitive: {transitive(M,A)}\n")
