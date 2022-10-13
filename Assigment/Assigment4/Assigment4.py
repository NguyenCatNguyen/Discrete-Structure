"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Monday October 10, 2022
Assignment: Assignment 4
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

def transitive(M,S):
    #For x,y,z in set s, check if (x,y) in M and (y,z) in M then (x,z) in M.
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

#Function to check if the relation is symmetric or not.
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

#Function to check if the relation is antisymmetric or not.
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



#Function to find Reflexive Closure. 
def CR(M,s):
    if reflexive(M,s) == True:
        print("b) R is reflexive\n")
    else:
        print("b) R is not reflexive")
        for x in s:
            #Adding the missing pair of (y,x) if it is missing
            if (x,x) not in M:
                M = list(M)
                M.append((x,x))
        print(f"c) R* = {M}\n")

#Function to find Symmetric Closure.
def CS(M):
    if symmetric(M) == True:
        print("b) R is symmetric\n")
    else:
        print("b) R is not symmetric")
        for (x,y) in M:
            if (y,x) not in M:
                #Adding the missing pair of (y,x) if it is missing
                M = list(M)
                M.append((y,x))
        print(f"c) R* = {M}\n")

#Function to find Transitive Closure.
def CT(M,s):
    if transitive(M,s) == True:
        print("b) R is transitive\n")
    else:
        print("b) R is not transitive")
        #Using Warshall Algorithm to find R*.
        for x in s:
            for y in s:
                for z in s:
                    if (x,y) in M and (y,z) in M:
                        M = list(M)
                        M.append((x,z))
        M = list(set(M))
        print(f"c) R* = {M}\n")

#Function to find Equivalence Relation.
def CE(M,s):
    #Check if R is reflexive
    if reflexive(M,s) == True:
        if symmetric(M) == True:
            if transitive(M,s) == True:
                print("b) R is an equivalence relation\n")
            else:
                print("b) R is not an equivalence relation, because it is not transitive\n")
        else:
            print("b) R is not an equivalence relation, because it is not symmetric\n")
    else:
        print("b) R is not an equivalence relation, because it is not reflexive\n")

#Function to find Poset.
def CP(M,s):
    if reflexive(M,s) == True:
        if antisymmetric(M) == True:
            if transitive(M,s) == True:
                print("b) R is a poset\n")
            else:
                print("b) R is not a poset, because it is not transitive\n")
        else:
            print("b) R is not a poset, because it is not antisymmetric\n")
    else:
        print("b) R is not a poset, because it is not reflexive\n")



#Functiont to execute each part of the assignment.
def Part1(R,s):
    print(f"For relationship R= {R} on the set {s}")
    print("a) R order pair = ", order_pair(R))
    CR(R,s)
   

def Part2(R,s):
    print(f"For relationship R= {R} on the set {s}")
    print("a) R order pair = ", order_pair(R))
    CS(R)
 

def Part3(R,se):
    print(f"For relationship R= {R} on the set {se}")
    print("a) R order pair = ", order_pair(R))
    CT(R,se)

def Part4(R,s):
    print(f"For relationship R= {R} on the set {s}")
    print("a) R order pair = ", order_pair(R))
    CE(R,s)

def Part5(R,s):
    print(f"For relationship R= {R} on the set {s}")
    print(f"a) S = {s}")
    print(f"b) R = {R}")
    CP(R,s)



#Assigment excercute.
#Part 1
set1 = {1,2,3,4}
relation1 = {(1,1), (4,4), (2,2), (3,3)}
set2 = {"a","b","c","d"}
relation2 = {("a","a"), ("c","c")}
print("\nPart 1 - Reflexive")
print("1.d")
Part1(relation1,set1)
print("1.e")
Part1(relation2,set2)
print("-"*70)


#Part 2
relation3 = {(1,2), (4,4), (2,1), (3,3)}
relation4 = {(1,2),(3,3)}
print("\nPart 2 - Symmetric")
print("2.d")
Part2(relation3,set1)
print("2.e")
Part2(relation4,set1)
print("-"*70)

#Part 3
relation5 = {("a","b"),("d","d"),("b","c"),("a","c")}
set6 = {1,2,3}
relation6 = {(1,1),(1,3),(2,2),(3,1),(3,2)}
print("\nPart 3 - Transitive")
print("3.d")
Part3(relation5,set2)
print("3.e")
Part3(relation6,set6)
print("-"*70)


#Part 4
relation7 = {(1,1),(2,2),(2,3)}
set7 = {1,2,3}
relation8 = {("a","a"),("b","b"),("c","c"),("b","c"),("c","b")}
set8 = {"a","b","c"}
print("\nPart 4 - Equivalence")
print("4.d")
Part4(relation7,set7)
print("4.e")
Part4(relation8,set8)
print("-"*70)

#Part 5[ ]
relation9 = {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)}
set9 = {1,2,3,4}
relation10 = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)}
set10 = {0, 1, 2, 3}
print("\nPart 5 - Poset")
print("5.d")
Part5(relation9,set9)
print("5.e")
Part5(relation10,set10)
print("-"*70)

    