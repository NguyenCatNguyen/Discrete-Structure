"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Monday October 10, 2022
Assignment: Assignment 4
"""

#Main function space (need more comment on function)
"""
1. Write code that determines if a relation (R) of ordered pairs is reflexive or not & then if it is not, 
finds the reflexive closure of R (R*). The output should be:
a) R={...}
b) R is or is not reflexive
c) R* if it is not reflexive
d) Show the code works for the relation {(1,1), (4,4), (2,2), (3,3)} on the
set {1,2,3,4}.
e) Show the code works for the relation {(a,a), (c,c)} on the set {a,b,c,d}.

"""

#Functions for all the part of the assignment.
#  
def order_pair(M):
    #Create an empty list to hold the value of ordered pairs.
    OP = []
    for (x,y) in M:
        OP.extend([(x,x),(y,y),(x,y),(y,x)])
    #Using extend method to add the value of ordered pairs to the empty list.
    OP = list(set(OP))
    #Using set method to remove duplicates and convert back to list.
    return OP

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



#Part 1
set1 = {1,2,3,4}
relation1 = {(1,1), (4,4), (2,2), (3,3)}

print(f"For relationship R={relation1} on the set {set1}")
print("a) R = ", order_pair(relation1))
print("b) R is reflexive: ",reflexive(relation1,set1))

set2 = {a,b,c,d}
relation2 = {(a,a), (c,c)}
print(f"For relationship R={relation2} on the set {set2}")
print("a) R = ", order_pair(relation2))
print("b) R is reflexive: ",reflexive(relation2,set2))



    