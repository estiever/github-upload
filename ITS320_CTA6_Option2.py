#---------------------------------------------------------------------------------------------------------------------------------
# Program Name: Eric Stiever's Module 6, Option 2 Assignment
# Program Objective: Compute the Cartesian product, AxB of two lists. Each list has no more than 10 numbers.
# For example, given the two input lists: A = [1,2] B = [3,4] 
# then the Cartesian product output should be: AxB = [(1,3),(1,4),(2,3),(2,4)]
# 
# Logic used (Pseudocode or just plain English): Pseudocode
#---------------------------------------------------------------------------------------------------------------------------------
# Program Inputs

def CartesianProduct(A,B):
    # Create empty C (Cartesian) list.
    C = []
    # Index, i, is set to zero for the A list of user-inputted numbers.
    i = 0
    # Index, j, is set to zero for the B list of user-inputted numbers.
    j = 0
    # Loop 
    for i in range(len(A)):  
        # Index value, i, cannot be higher than 9 due to instructions stating there can be no more than 10 numbers per list.
        if i <= 9 and i <= len(A):
            for j in range(len(B)):
                # Index value, j, cannot be higher than 9 due to instructions tating there can be no more than 10 numbers per list.
                if j <= 9 and j <= len(B):
                    new_elem = (A[i],B[j])
                    C.append(new_elem)
                j += 1
        i += 1   
    # Return the Cartesian products of list A x list B.        
    return C
A = []
B = []
# Take in user input for the A list.
user_input_a = [int(i) for i in input("Please enter up to 10 numbers followed by a space: ").split()]
A = user_input_a
# Take in user input for B list.
user_input_b = [int(j) for j in input("Please enter up to 10 numbers followed by a space: ").split()]
B = user_input_b
# Print the Cartesian products, AxB, of the two user-inputted lists.
print('The Cartesian products of the numbers that you entered are: \n', CartesianProduct(A,B))
