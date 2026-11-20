# # hello
# def printrevpattern(n):
#     for i in range(1,n):
#         for j in range(i):
#             print(j, end=" ")
#         print()
# printrevpattern(5)        

def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
print(square(4))        