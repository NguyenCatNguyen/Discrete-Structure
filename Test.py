def FiveD():
	A = {1,2,3,4}
	R = [(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)]
	def transitive(R,A):
		for a in A:
			for b in A:
				if (a, b) in R:
					for c in A:
						if (b, c) in R and (a, c) not in R:
							return False
		return True
	def antisymmetric(R,A):
		for ele1, ele2 in R:# for loop that iterates over the ordered pairs in the relation above
			if (ele2, ele1) not in R:#if statement with the condition that the ordered pairs in R must be antisymmetric to excute further code
				return True 
		return False
	def reflexive(R,a):
		for ele in a:
			if (ele, ele) not in R:
				return False
		return True
	print(f"5d)")
	print(f"\ta) S = {A}")
	print(f"\tb) R = {R}")
	if transitive(R,A) == True and antisymmetric(R,A) == True and reflexive(R,A) == True:
		print (f'\tc) (S,R) is a poset')
	else:
		print(f'\tc) (S,R) is not a poset')
		print(f'\td) Reasons (S,R) is not a poset: ')
	if transitive(R,A) == False:
		print('\t\tIt is not transitive')
	if reflexive(R,A) == False:
		print('\t\tIt is not reflexive')
	if antisymmetric(R,A) == False:
		print('\t\tIt is not antisymmetric')
	print('-------------------------------------------------------')# prints a line to help seperate each problem
FiveD()

def FiveE():
	A = {0,1,2,3}
	R = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)]
	def transitive(R,A):
		for a in A:
			for b in A:
				if (a, b) in R:
					for c in A:
						if (b, c) in R and (a, c) not in R:
							return False
		return True
	def antisymmetric(R,A):
		for ele1, ele2 in R:# for loop that iterates over the ordered pairs in the relation above
			if (ele2, ele1) not in R:#if statement with the condition that the ordered pairs in R must be antisymmetric to excute further code
				return True 
		return False
	def reflexive(R,a):
		for ele in a:
			if (ele, ele) not in R:
				return False
		return True
	print(f"5e)")
	print(f"\ta) S = {A}")
	print(f"\tb) R = {R}")
	if transitive(R,A) == True and antisymmetric(R,A) == True and reflexive(R,A) == True:
		print (f'\tc) (S,R) is a poset')
	else:
		print(f'\tc) (S,R) is not a poset')
		print(f'\td) Reasons (S,R) is not a poset: ')
	if transitive(R,A) == False:
		print('\t\tR is not transitive')
	if reflexive(R,A) == False:
		print('\t\tR is not reflexive')
	if antisymmetric(R,A) == False:
		print('\t\tR is not symmetric')
	print('-------------------------------------------------------')# prints a line to help seperate each problem
FiveE()



"""
1. Write code that determines if a relation (R) of ordered pairs is reflexive or not & then if it is not, 
finds the reflexive closure of R (R*). The output should be:
a) R={...}
b) R is or is not reflexive
c) R* if it is not reflexive
d) Show the code works for the relation {(1,1), (4,4), (2,2), (3,3)} on the
set {1,2,3,4}.
e) Show the code works for the relation {(a,a), (c,c)} on the set {a,b,c,d}.

2. Write code that determines if a relation (R) of ordered pairs is symmetric or 
not & then if it is not, finds the symmetric closure of R (R*). The output should be:
a) R={...}
b) R is or is not symmetric
c) R* if it is not symmetric
d) Show the code works for the relation {(1,2), (4,4), (2,1), (3,3)} on the
set {1,2,3,4}.
e) Show the code works for the relation {(1,2), (3,3)} on the set
{1,2,3,4}.

3. Write code that determines if a relation (R) of ordered pairs is transitive or not
& then if it is not, finds the transitive closure of R (R*) using Warshalls Algorithm. The output should be:
a) R={...}
b) R is or is not transitive 
c) R* if it is not transitive
d) Show the code works for the relation {(a,b), (d,d), (b,c), (a,c)} on the set {a,b,c,d}.
e) Show the code works for the relation {(1,1),(1,3),(2,2),(3,1),(3,2)} on the set {1,2,3}.

4. Write code that determines if a relation (R) of ordered pairs is an equivalence 
relation or not and the reason why. The output should be:
a) R={...}
b) R is or is not an equivalence relation
c) The reasons why, if it is not an equivalence relation (i.e., it is not
reflexive, and/or it is not symmetric, and/or it is not transitive).
d) Show the code works for the relation {(1,1),(2,2),(2,3)} on the set
{1,2,3}.
e) Show the code works for the relation {(a,a),(b,b),(c,c),(b,c),(c,b)} on
the set {a,b,c}.

5. Write code that determines if a relation (R) of ordered pairs is a poset of the
set (S) or not and the reason why. The output should be: a) S={...}
b) R={...}
c) (S,R) is or is not a poset
d) The reason why, if it is not poset (i.e., it is not reflexive, and/or it is
not antisymmetric, and/or it is not transitive.
e) Show the code works for the relation {(1,1), (1,2), (2,2), (3,3), (4,1),
(4,2), (4,4)} on the set {1, 2, 3, 4}.
f) Show the code works for the relation {(0, 0), (0, 1), (0, 2), (0, 3), (1,
0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} on the set {0, 1, 2, 3}.

"""
