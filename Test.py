k = [(1,2),(2,1)]
for (x,y) in k:
    if (y,x) in k:
        if x != y:
            print("True")
        else:
            print("False")