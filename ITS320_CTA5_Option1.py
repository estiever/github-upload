#--------------------------------------------------------------------------------------------------
# Program Name: Eric Stiever's Module 5 Critical Thinking Assignment, Option 1
# Program Objective: Write a Python function that will accept as input three strings from the user.
# The method will return to the user a concatenation of the three strings and will print the
# strings in reverse order.
# Logic used (Pseudocode or just plain English): Pseudocode
#--------------------------------------------------------------------------------------------------
# Program Inputs:

def user_str(str1, str2, str3):
    # return concatenation of the three strings printed in reverse
    return str1[::-1] + str2[::-1] + str3[::-1]

# Create the main method to process three strings from the user. 
def main():
    # User input for the three strings
    user_string1 = input('Please enter a text string: ')
    user_string2 = input('Please enter text string 2: ')
    user_string3 = input('Please enter text string 3: ')
#---------------------------------------------------------------------------------------------------
# Program Output:
    # Call the user_str function
    print('The three strings concatenated AND printed in reverse:'
        , user_str(user_string1, user_string2, user_string3))

main()
#--------------------------------------------------------------------------------------------------