"""
Write a program that creates a min-max strategy for the game of Nim. Display the strategy in a 
manner that will be clear to the grader and includes all of the elements shown in the “Minmax Strategy 
for Nim (11.2.5)” slide in the “Application of Trees” lecture.

a) Debug your program with a version of Nim with the starting position where there are 3 piles 
of stones containing 2, 2, and 1 stone each, respectively (same as one in the “Minmax Strategy 
for Nim (11.2.5)” slide.
b) Test your program with a version of Nim with the starting position consists of three piles 
with one, two, and three stones, respectively. When drawing the tree represent by the same vertex 
symmetric positions that result from the same move.
c) Who wins the game if both players follow an optimal strategy?
"""
import random
def Nim(a,b,c):
    #Let a,b,c represent the amount of stones on each pile.
    N = [a,b,c]

    # D dummy list
    D = [0,1,2]
    while len(D) != 0:
        x = 1
        D[0] = D[0] - x 
    
    
    """
    Game rule:
    1. Player can remove as many stone as posible.
    2. Player can only pick one pile
    - Need to be a recurrsion function
    """
    return N

    """
    [1,2,3]
    p1 [0,2,3] [1,1,3] [1,0,3] [1,2,2] [1,2,1] [1,2,0]
    p2 [0,1,3] [0,0,3] [0,2,2] [0,2,1]
    
    """



print(Nim(1,2,3))