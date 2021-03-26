#------------------------------------------------------------------------
# Program Name: Eric Stiever's Module 4 Critical Thinking Assignment, Option 1
# Program Objective: Utilize a while loop to read a set of five floating-point
# values from user input and print the total, average, max, min, and interest 
# at 20% for each value.
#
# Logic used (Pseudocode or just plain English): Pseudocode
#------------------------------------------------------------------------
# Program Inputs:
# Created an empty list where the values are stored to be accessed later.
values = []

# loop 5 times to collect the five user inputted values.
for i in range(0, 5):
    n = float(input("Please enter a numerical value, then press Enter: ")) 
    values.append(n)

# Set the starting sum to zero.
sum = 0
# Calculate the total of the five user inputted numbers.
for n in values:
    sum = sum + n
# Calculate the average
    avg = sum/len(values)

# Calculate the interest at 20% for each original value, n, entered by the user.
# Float specified to two decimal places after the whole number.
for Original_Value in values:
    Interest_Value = Original_Value + (Original_Value * 0.2)
    print('Interest at 20 percent of original value, %.2f, is %.2f' % (Original_Value, Interest_Value))
#------------------------------------------------------------------------
# Program Outputs
print('\nTotal:', sum)

print('Average:', avg)

print('Maximum:', max(values))

print('Minimum:', min(values), '\n')