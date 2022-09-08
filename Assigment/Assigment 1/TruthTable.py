

#Create and function for 2 input.
def AND(x,y):
    if x == "T" and y == "T":
        return "T"
    else:
        return "F"
#Create or function for 2 input.
def OR(x,y):
    if x == "T" or y == "T":
         return "T"
    else:
        return "F"
#Create not function for 2 input.
def NOT(x):
    if x == "T":
        return "F"
    else:
        return "T"

#Create and function for 3 input.
def AND1(x,y,z):
    if x == "T" and y == "T" and z == "T":
        return "T"
    else:
        return "F"


#Code main function.
def main():
    num = ""
    while num != "7":
        # preset value for 2 input
        p = ["T", "T", "F", "F"]
        q = ["T", "F", "T", "F"]
        # preset value for 3 input
        P = ["F","F","F","F","T","T","T","T"]
        Q = ["F","F","T","T","F","F","T","T"]
        R = ["F","T","F","T","F","T","F","T"]
        #Print the option that user could view.
        print(
            "1. De Morgan's First Law\n2. De Morgan's Second Law\n3. First Associative Law\n4. Second Associative Law\n5. [(p+q)(p->r)(q->r)] -> r = T\n6. p<->q = (p->q)(q->p)\n7. Exit the program.")
        num = input("\nPick a truth table you want to view: ")
        if num == "1":
            print("\n--- De Morgan's First Law ---\n")
            i = 0
            # Loop through all the output for p and q
            while i != 4:
                # the condition for the loop. Since there are 4 input and the first input start at 0
                print(
                    f"p: {p[i]} | q: {q[i]} | !p: {NOT(p[i])} | !q: {NOT(q[i])} | p+q: {AND(p[i], q[i])} | !(p+q): {NOT(AND(p[i], q[i]))} | !p*!q: {OR(NOT(p[i]), NOT(q[i]))}")
                i += 1
            print("\n==> !(p*q)=!p+!q")

        if num == "2":
            print("\n--- De Morgan's Second Law ---\n")
            i = 0
            # Loop through all the output for p and q
            while i != 4:
                # the condition for the loop. Since there are 4 input and the first input start at 0
                print(
                    f"p: {p[i]} | q: {q[i]} | !p: {NOT(p[i])} | !q: {NOT(q[i])} | p+q: {OR(p[i], q[i])} | !(p+q): {NOT(OR(p[i], q[i]))} | !p*!q: {AND(NOT(p[i]), NOT(q[i]))}")
                i += 1
            print("\n==> !(p+q)=!p*!q")

        if num == "3":
            print("\n--- First Associative Law ---\n")
            i = 0
            # Loop through all the output for p,q and r
            while i != 8:
                # the condition for the loop. Since there are 8 input and the first input start at 0
                print(f"p: {P[i]} | q: {Q[i]} | r: {R[i]} | p*q: {AND(P[i],Q[i])} | q*r: {AND(Q[i],R[i])} | (p*q)*(r):{AND(AND(P[i],Q[i]),R[i])} | p*(q*r): {AND(P[i],AND(Q[i],R[i]))}")
                i +=1
            print("\n==> (p*q)*r = p*(q*r)")

        if num == "4":
            print("\n--- Second Associative Law ---\n")
            i = 0
            # Loop through all the output for p,q and r
            while i != 8:
                # the condition for the loop. Since there are 8 input and the first input start at 0
                print(f"p: {P[i]} | q: {Q[i]} | r: {R[i]} | p+q: {OR(P[i],Q[i])} | q+r: {OR(Q[i],R[i])} | (p+q)+(r):{OR(OR(P[i],Q[i]),R[i])} | p+(q+r): {OR(P[i],OR(Q[i],R[i]))}")
                i +=1
            print("\n==> (p*q)*r = p*(q*r)")

        if num == "5":
            print("\n--- [(p+q)(p->r)(q->r)] -> r = T ---\n")
            i = 0
            # Loop through all the output for p,q and r
            while i != 8:
                # the condition for the loop. Since there are 8 input and the first input start at 0
                print(f"p: {P[i]} | q: {Q[i]} | r: {R[i]} | p+q: {OR(P[i],Q[i])} | p->r: {OR(NOT(P[i]),R[i])} | q->r: {OR(NOT(Q[i]),R[i])} | (p+q)(p->r)(q->r): {AND1(OR(P[i],Q[i]),OR(NOT(P[i]),R[i]),OR(NOT(Q[i]),R[i]))} | (p+q)(p->r)(q->r)] -> r: {OR(NOT(AND1(OR(P[i],Q[i]),OR(NOT(P[i]),R[i]),OR(NOT(Q[i]),R[i]))),R[i])}  ")
                i +=1
            print("\n==> [(p+q)(p->r)(q->r)] -> r = T")



        if num == "6":
            print("\n--- (p<->q = (p->q)*(q->p)\n")
            # p->q = !p+q and q->p = !q+p
            i = 0
            # Loop through all the output for p and q
            while i != 4:
                print(f"p: {p[i]} | q: {q[i]} | !p: {NOT(p[i])} | !q: {NOT(q[i])} | p->q: {OR(NOT(p[i]),q[i])} | q->p: {OR(NOT(q[i]),p[i])} ")
                i += 1
        #Incase the user input an unvalid input.
        else:
            print("\nYou enter an invalid choices. Please pick one of these options.")
    print("\nProgram end.")




#code excercute.
main()
