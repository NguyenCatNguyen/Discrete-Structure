

def Nim(a, b, c):
    I = [a,b,c]
    #Case 1: If the number of stone in each pile is 0, ask the user to input the number of stone in each pile again
    if a == 0 and b == 0 and c == 0:
        print("Invalid input. Please input again.")
        a = int(input("Please input the number of stone in pile 1: "))
        b = int(input("Please input the number of stone in pile 2: "))
        c = int(input("Please input the number of stone in pile 3: "))
        Nim(a, b, c)
    #If the number of stone in each pile is 0, declare the winner
    if :
        print("You win!")
    case1 = I(a-1, b, c)
    case2 = I(a, b-1, c)
    case3 = I(a, b, c-1)

