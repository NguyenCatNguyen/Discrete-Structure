"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Tuesday October 25, 2022
Assignment: Assignment 5
"""

#Function to check if the relation is a function or not.
def check_function(A,B,f):
    count = 0
    for x in A:
        for y in B:
            if (x,y) in f:
                count += 1
    if count == len(A):
        return True
    else:
        return False
    
#Function to check if the relation is an injective or not.
def check_injective(A,B,f):
    List = []
    for (x,y) in f:
        for x in (x,y):
            List.append(x)
    #Check if value in List is unique
    if len(List) == len(set(List)):
        return True
    else:
        return False

#Function to check if the relation is surjective or not.
def check_surjective(B,f):
    count = 0
    for (x,y) in f:
        for y in (x,y):
            #Check if y is in B
            if y in B:
                count += 1
    if count == len(B):
        #Check if all y values in f are in B.
        return True
    else:
        return False

#Function to check if the relation is bijective or not.
def check_bijective(A,B,f):
    #A function is bijective if and only if it is both injective and surjective.
    if check_function(A,B,f) == True and check_injective(A,B,f) == True and check_surjective(B,f) == True:
        return True
    else:
        return False

def check_inverse(A,B,f):
    L = []
    for (x,y) in f:
        L.append((y,x))
    print(f"c) The inverse of f is: {L}")


#Main function to printout all the require outcome. 
def main(A,B,f,num):
    print(f"{num}. A = {A}, B = {B}, f = {f}")
    if check_function(A,B,f) == True:
        print("a) The relation is a function.")
        print("b) The relation is:")
        print(f"- The relation is injective: {check_injective(A,B,f)}")
        print(f"- The relation is surjective: {check_surjective(B,f)}")
        if check_bijective(A,B,f) == True:
            print("The relation is bijective.")
            check_inverse(A,B,f)
    else:
        print("a) The relation is not a function.")
    print()

#Test case
#1
A = ["a","b","c","d"] 
B = ["v","w","x","y","z"]
f = [("a","z"),("b","y"),("c","x"),("d","w")]
#2
B2 = ["x","y","z"]
f2 = [("a","z"),("b","y"),("c","x"),("d","z")]
#3
B3 = ["w","x","y","z"]
#4
B4 = {1,2,3,4,5}
f4 = {("a",4),("b",5),("c",1),("d",3)} 
#5
A5 = ["a","b","c"]
B5 = {1,2,3,4}
f5 = {("a",3),("b",4),("c",1)}
#6
f6 = {("a",2),("b",1),("c",3),("d",2)}
B6 = {1,2,3,4}
#7
f7 = {("a",4),("b",1),("c",3),("d",2)}
B7 = {1,2,3,4}
#8
f8 = {("a",2),("b",1),("c",2),("d",3)}
#9
A9 = ["a","b","c"]
B9 = {1,2,3,4}
f9 = {("a",2),("b",1),("a",4),("c",3)}
#Question 1
main(A,B,f,1)

#Question 2
main(A,B2,f2,2)

#Question 3
main(A,B3,f,3)

#Question 4
main(A,B4,f4,4)

#Question 5
main(A5,B5,f5,5)

#Question 6
main(A,B6,f6,6)

#Question 7
main(A,B5,f7,7)

#Question 8
main(A5,B6,f8,8)

#Question 9
main(A9,B9,f9,9)




