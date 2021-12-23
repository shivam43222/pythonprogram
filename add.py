"""
accept two numbers from users for addition 
& ask user if he wants to repeat the addition with other numbers.
"""
# create function 
def add():
    # taking input from user
    add_1=int(input("Enter first Number :"))
    add_2=int(input("Enter second Number :"))
    # performing addition
    ans=add_1+add_2
    print("Addition of 2 No ",ans)

# main programm
add() # calling the function
while True:
    user = input("Do You Want to repeat the addition with other numbers Tpe Y/N").upper()
    if user == 'Y': 
        add() # calling function if user chose to perform other number addition.
    else:
        # if user dont want to perform other number addition
        print("Thank you")
        break # loop will be break and come outside the loop

"""
usage : To run this file please type command on terminal python3 add.py 
"""

        
        