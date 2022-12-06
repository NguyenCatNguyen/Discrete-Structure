"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Tuesday Nov 29, 2022
Assignment: Assignment 7
Topic: Distributing objects into boxes
"""
import math

# n choose k function
def C(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

# n permute k function
def P(n,k):
    return math.factorial(n)/math.factorial(n-k)

def S(n,j):
    i = 1
    total = 0
    while j != 0:
        total =((-1)**i)*C(j,i)*((j-i)**n) + total
        i += 1
        j -= 1
    total = (1/math.factorial(j))*total
    return total
    




#1. Function for distribute distinguishable objects into distinguishable boxes
def Ddist(n,k,t):
    #n = num of boxes
    #k = num of objects
    #t = num of object in bigbox
    #Check if the number of objects is less than the number of boxes
    if t/n >= k:
        ##Check if the number of objects is less than the number of boxes
        total = C(t,k)
        ## Use the formula to calculate the number of ways to distribute the objects into the boxes.
        while n != 1:
            #Use a loop to multiple the number of ways to distribute the objects into the boxes.
            t = t-k
            total = total * C(t,k)
            n = n - 1
        return total
    else:
        print("The input is invalid")

#2. Function for indisguishable objects in distinguishable boxes
def Idist(n,k):
    #Using the formula C(n+k-1,k) to calculate the number of ways to distribute indistinguishable objects into distinguishable boxes
    return C(n+k-1,k)


#3. Function for distribute distinguishable objects into indistinguishable boxes
def Dindist(n,k):
    return P(n+k-1,k)


#4. Function for distribute indistinguishable objects into indistinguishable boxes
def Iindist(n,k):
    return P(n,k)

def main():
    #Test case
    print("Part 1:")
    print("a. The number of ways to distribute 5 distinguishable cards for 4 distinguishable player is")
    print(f"=> {Ddist(4,5,52)}\n")
    print("b. The number of ways to distribute 40 distinguishable journal into 4 distinguishable boxes with 10 in each of them is")
    print(f"=> {Ddist(4,10,40)}\n")

    print("Part 2:")
    print("a. The number of ways to distribute 10 indistinguishable objects into 8 distinguishable boxes is")
    print(f"=> {Idist(8,10)}\n")
    print("b. The number of ways to distribute 12 indistinguishable balls into 6 distinguishable bins is")
    print(f"=> {Idist(6,12)}\n")

    print("Part 3:")
    print("a. The number of ways to distribute 4 distinguishable employees into 3 indistinguishable offices is")
    print(f"=> {Dindist(3,4)}\n")
    print("b. The number of ways to distribute 5 distinguishable employes into 4 indistinguishable offices is")
    print(f"=> {Dindist(4,5)}\n")


    print("Part 4:")
    print("a. The number of ways to distribute 6 indistinguishable book into 4 indistinguishable boxes is")
    print(f"=> {Iindist(4,6)}\n")
    print("b. The number of ways to distribute 5 indistinguishable objects into 3 indistinguishable boxes is")
    print(f"=> {Iindist(3,5)}\n")

    
main()
print(f"Test case: {S(6,1)}")
