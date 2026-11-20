def repeated_pattern(n):
    for i in range(1, n + 1):  # outer loop for rows
        for j in range(n, 0, -1):  # inner loop for columns
            print(j, end=" ")
        print()  # move to the next line after each row
repeated_pattern(5)     