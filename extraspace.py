"""
program to Remove extra spaces from a string
"""

input_string = \
	' Hello Bunny . Welcome , Do you love Alcohol , traveller ? '
# Declare empty list
output_string = []

# Flag to check if spaces have occured
space_flag = False 

# using for loop 
for index in range(len(input_string)):
    if input_string[index] != ' ':
        if space_flag == True:
            if (input_string[index] == '.' or input_string[index] == '?' or input_string[index] == ','):
                pass
            else:
                output_string.append(' ')
            space_flag = False
        output_string.append(input_string[index])
	
    elif input_string[index - 1] != ' ':
        space_flag = True

print (''.join(output_string))

"""
usage : To run this file please type command on terminal python3 extraspace.py 
"""