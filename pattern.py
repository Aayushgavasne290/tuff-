def print_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        # Indent this print() so it lines up with the inner 'for' loop
        print() 

# You must call the function and pass it a number to see the output
print_pattern(5)