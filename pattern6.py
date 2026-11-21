def right_tiangle(n):
    for i in range(1, n + 1):  # outer loop for rows
        for j in range(1, i + 1):  # inner loop for columns
            print(j, end=" ")
        print()  # move to the next line after each row     
        
print(right_tiangle(5))   