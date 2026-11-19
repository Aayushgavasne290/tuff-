# def print_pattern(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end=" ")
#         # Indent this print() so it lines up with the inner 'for' loop
#         print() 

# # You must call the function and pass it a number to see the output
# print_pattern(5)

# now new type of pattern

# def printrevpattern(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*", end=" ")
#         print()
# printrevpattern(5)
#         


#   pyramid pattern
  def printpyarmaid(n):
      for i in range(n):
          for j in range(n-1-i):
              print(" ", end="")
            for k in range(2*i+1):
                print("*", end="")
            print()
    printpyarmaid(5)        