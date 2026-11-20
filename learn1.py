# hello
def printrevpattern(n):
    for i in range(1,n):
        for j in range(i):
            print(j, end=" ")
        print()
printrevpattern(5)        