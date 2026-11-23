def hollow_triangle(n):
    for row in range(n):
        for col in range(n):
            if col == n - row - 1 or col == n - 1 or row == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()