#Range
#for i in range(1,10)
# print(i)
#print("Hello");print("Hii")
#print("Home work",end=" ");print("done!")

# reversed star pattern
n=int(input("Enter the number of rows you want!\n"))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(" ",end="*")
    print()

#star pattern
n=int(input("Enter the number of rows you want!\n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()