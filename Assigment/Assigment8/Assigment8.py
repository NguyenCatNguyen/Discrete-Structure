"""
Authour: Nguyen Cat Nguyen
KUID: 3077463
Date: Thursday Dec 8, 2022
Assignment: Assignment 8
Topic: Intro to graph 
"""
"""
Plan:
- Write the graph out
- Write the function to check if the graph is connected
- Write the function to find an Euler circuit in a graph
- Write the function to find an Euler path in a graph
- Write the function to check if the graph is Euler
- Write the function to find the degree of a vertex
- Write the function to check if the graph is Hamiltonian using Dirac's theorem
- Write the function to check if the graph is Hamiltonian using Ore's theorem

"""
import random
#Function to check if the graph is connected
def isConnect(G):
    #Check if the graph is connected
    V = []
    Q = []
    for i in G:
        Q.append(i)
        #Add all the vertices to the queue
        break
    while Q:
        node = Q.pop(0)
        #Pop the first element in the queue
        if node not in V:
            #Check if the node has been passed through
            V.append(node)
            #If not, add it to the list of visited vertices
            for i in G[node]:
                #Add all the vertices that are connected to the node to the queue
                Q.append(i)
                #Check if the graph is connected
    if len(V) == len(G):
        #If the number of visited vertices is equal to the number of vertices in the graph, the graph is connected
        return True
    else:
        return False
        
#Function to check if the graph is Euler path
def isEuler_path(G):
    #Check if the graph path through every edge exactly once
    if isConnect(G) == True:
        odd = 0
        for i in G:
            if len(G[i]) % 2 == 1:
                #Check if there are any odd degree
                odd += 1
        if odd <= 2:
            #Check if there are more than 2 odd degree
            return True
            #If there are 2 odd degree, the graph is Euler path
        else:
            return False
            #If there are more than 2 odd degree, the graph is not Euler
    else:
        return False

#Function to check if the graph is Euler circuit
def isEuler_circuit(G):
    #Check if the graph path through every edge exactly once
    if isConnect(G) == True:
        for i in G:
            if len(G[i]) % 2 == 1:
                return False
            else:
                return True
    else:
        return False

#Function to print the vertices that has odd degree
def notEuler(G, num):
    #Empty list to store the vertices that has odd degree
    L = []
    for i in G:
        if len(G[i]) % 2 == 1:
            #Make the list of vertices that has odd degree
            L.append(i)
    print(f"Graph {num} is not Euler because vertices: {L} has odd degree.")

#Function to check if the graph is Euler and print the result
def Euler(G, num):
    #Check if the graph is Euler path or Euler circuit
    if isEuler_circuit(G) == True:
        print(f"Graph {num} is an Euler circuit\n")
    elif isEuler_path(G) == True:
        print(f"Graph {num} is an Euler path\n")
    else:
        notEuler(G, num)

#Function to find the degree of a vertex
def degree(G, v):
    #Check if the vertex is in the graph
    if v in G:
        return len(G[v])
    else:
        return 0

#Function that represent Dirac's theorem about Hamiltonian circuit
def Dirac(G, num):
    #number of vertices over 2
    n = 0
    #Check if the degree of every vertex is greater or equall to n
    for i in G:
        if degree(G, i) >= (len(G)/2):
            n += 1
    if n == len(G):
        print(f"Graph {num} is Hamiltonian\n")
    else:
        print(f"Graph {num} is not Hamiltonian\n")

"""
- Ore's theorem:
    - Create a non-adjacent function to find non-adjacent vertices
    - Check to see if the degree of the non-adjacent vertices pair is greater than n (number of vertices)
    - If it is, the graph is Hamiltonian
    - If it is not, the graph is not Hamiltonian

"""




def non_adj(G):
    #Empty list to store the vertices that has odd degree
    # Check if two vertices are adjacent
    # If they are not, add them to the list
    # Loop through the list to find the pair of non-adjacent vertices
    L = []
    for i in G:
        for j in G:
            if j not in G[i]:
                L.append((i,j))
                #Add the pair of non-adjacent vertices to the list
    #Remove the pair of same vertices
    for (x,y) in L:
        if (x,x) in L:
            L.remove((x,x))
        if (y,y) in L:
            L.remove((y,y))
    #Remove the pair of non-adjacent vertices that are the same but in reverse order
    for (x,y) in L:
        if (y,x) in L:
            L.remove((y,x))
    return L


#Function that represent Ore's theorem about Hamiltonian path
def Ore(G, num):
    n = 0
    Non = non_adj(G)
    for x,y in Non:
        if degree(G,x) + degree(G,y) >= len(G):
            n += 1
    if n == len(Non):
        print(f"Graph {num} is Hamiltonian\n")
    else:
        print(f"Graph {num} is not Hamiltonian\n")

#Maxmin function to find the maximum minimum path
def Minmax(I):
    for value in I:
        if value == 0:
            continue

#Player take turn to take stones from the pile.
def switch(player):
    if player == 1:
        return 2
    else:
        return 1


#Function to create a strategy for the game of nim, game tree of nim
def nim(row, pile1 , pile2, pile3):
    #Pile represent number of stones in each pile
    #Row represent the number of rows
    I= [pile1, pile2, pile3]
    #Create a list of the initial number of stones in each pile
    print(f"Initial number of stones in each pile: {I}")
    #Posible move for each pile
    #If the number of stones in the pile is greater than 0, the player can take 1 or 2 stones
    #If the number of stones in the pile is 1, the player can only take 1 stone
    #If the number of stone in each pile is 0, declare the winner


















#Part 1: Graph
G11 = { "a" : ["b", "e"],
          "b" : ["a", "e"],
          "c" : ["d", "e"],
          "d" : ["c","e"],
          "e" : ["a", "b", "c", "d"]
        } 

G12 = { "a" : ["b", "e","d"],
          "b" : ["a", "e","c"],
          "c" : ["b", "e","d"],
          "d" : ["a", "c","e"],
          "e" : ["a", "b", "c", "d"]}

G13 = { "a" : ["b","d","c"],
            "b" : ["a", "d","e"],
            "c" : ["d", "a"],
            "d" : ["a", "b", "c","e"],
            "e" : ["b","d"]
            }


Gb1 = { "a" : ["b", "d"],
        "b" : ["a", "c","d","e"],
        "c" : ["b", "e","f"],
        "d" : ["a", "b", "e"],
        "e" : ["b", "c", "d","f"],
        "f" : ["c", "e","i"],
        "g" : ["d","e","h"],
        "h" : ["g","i","d","e","f"],
        "i" : ["h","f"],
    }

#Part 2: Graph
G21 = { "a" : ["b", "e","c"],
        "b" : ["a", "e","c"],
        "c" : ["a", "b", "d","e"],
        "d" : ["c","e"],
        "e" : ["a", "b", "c", "d"]
    }

G22 = { "a" : ["b"],
        "b" : ["a", "c","d"],
        "c" : ["b", "d"],
        "d" : ["b", "c"]
    }

G23 = { "a" : ["b"],
        "b" : ["a", "c","g"],
        "c" : ["b", "d","e"],
        "d" : ["c"],
        "e" : ["c", "f","g"],
        "f" : ["e"],
        "g" : ["b", "e"]
    }

Gb2 = { "a" : ["b", "c"],
        "b" : ["a", "c"],
        "c" : ["a", "b", "f"],
        "d" : ["e","f"],
        "e" : ["d", "f"],
        "f" : ["c", "d", "e"]
    }






#Main run
#Part1
print("PART 1: GRAPH")
print("a. ")
Euler(G11,"G1")
Euler(G12,"G2")
Euler(G13,"G3")
print("b. ")
Euler(Gb1,"Test1")
print("="*70)
#Part2
print("PART 2: GRAPH")
print("Using Dirac's theorem")
print("a. ")
Dirac(G21,"G1")
Dirac(G22,"G2")
Dirac(G23,"G3")
print("b. ")
Dirac(Gb2,"Test2")
print("="*70)

#Part3
print("PART 3: GRAPH")
print("Using Ore's theorem")
print("a. ")
Ore(G21,"G1")
Ore(G22,"G2")
Ore(G23,"G3")
print("b. ")
Ore(Gb2,"Test2")
print("="*70)

#Part4
