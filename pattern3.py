def printrevpattern(n):
    for i in range(n,0,-1):#outer loop for rows
        for j in range(i):#inner loop for columns
            print("*", end=" ")
        print()
printrevpattern(5)