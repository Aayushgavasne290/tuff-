def print_pattern(n):
    for i in range(n): #first here we have outer loop where * will be print
        for j in range(i+1):#here j check the column for the space , and i+1 will increment till n
            print("*",end=" ")

        print()
print_pattern(5)          