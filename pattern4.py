def print_number_pattern(n):
    for i in range(1, n + 1):#outer loop for rows 
        for j in range(1, i + 1):#inner loop for columns will be incremented for each row
            print(j, end=" ")
        print()
print_number_pattern(5)        