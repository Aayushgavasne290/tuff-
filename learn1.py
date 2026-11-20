# # hello
# def printrevpattern(n):
#     for i in range(1,n):
#         for j in range(i):
#             print(j, end=" ")
#         print()
# printrevpattern(5)        

def square(n):
    for i in range(n):    #outer loop here will print the rows
        for j in range(n):  #inner loop here will print the columns
            print("*", end=" ") # here the star is present that will be printed in over square figure
        print()
print(square(4))        