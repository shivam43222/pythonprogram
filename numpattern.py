# demonstrate number pattern

# take input from the user
size = int(input("Enter the range: "))

#initialize the su
k = 1

# outer loop to handle number of rows
for i in range(1, size + 1):
    # inner loop to handle number of columns values changing acc. to outer loop
    for j in range(1, i + 1):
        # printing number
        print(k, end=" ")
        # incrementing k after each loop
        k = k + 1
    print()
print("\n") 

"""
usage : To run this file please type command on terminal python3 vowelsalpha.py 
"""