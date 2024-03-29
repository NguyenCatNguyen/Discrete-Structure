"""
You may use any language you want, but if you want help from me or one of the 
SIs, you should probably use C++ or Python. 
• Recall that a function f from A to B, is a relation f ⊆ A x B such that each element 
of A is assigned to exactly one element of B. 
• Thus, we can represent a function as a relation of order pairs, (a,b), where a ∊ A, b ∊ B, and b = f(a). 
• Write a program that takes inputs of A, B, and a relation f and 
a) determines if the relation is a function or not, 
b) and if it is a function, determines if it is injective, surjective, or bijective, 
c) and if it is bijective, determines the inverse function. 
• Your program should print out the inputs using the notation you learned in class, 
i.e., A = {...}, B = {...}, f = {(a,b), ...}, whether the relation is a function or not, 
b) and if it is a function, whether it is injective, surjective, or bijective, c) and if it 
is bijective, what is the inverse function. Test your program with the following 
inputs: 
1. A = {a,b,c,d}, B = {v,w,x,y,z}, f = {(a,z),(b,y),(c,x),(d,w)} 
2. A = {a,b,c,d}, B = {x,y,z}, f = {(a,z),(b,y),(c,x),(d,z)} 
3. A = {a,b,c,d}, B = {w,x,y,z}, f = {(a,z),(b,y),(c,x),(d,w)} 
4. A = {a,b,c,d}, B = {1,2,3,4,5}, f = {(a,4),(b,5),(c,1),(d,3)} 

5. A = {a,b,c}, B = {1,2,3,4}, f = {(a,3),(b,4),(c,1)} 

6. A = {a,b,c,d}, B = {1,2,3}, f = {(a,2),(b,1),(c,3),(d,2)} 

7. A = {a,b,c,d}, B = {1,2,3,4}, f = {(a,4),(b,1),(c,3),(d,2)} 

8. A = {a,b,c,d}, B = {1,2,3,4}, f = {(a,2),(b,1),(c,2),(d,3)} 

9. A = {a,b,c}, B = {1,2,3,4}, f = {(a,2),(b,1),(a,4),(c,3)} 
• Provide comments that explain what each line of code is doing. See rubric below. 

"""