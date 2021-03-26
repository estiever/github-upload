#------------------------------------------------------------------------
# Program Name: Eric Stiever's Module 3 Critical Thinking Assignment, Option 1 
# Program Objective: Program to output value of a Ferrari 250 GTO in year inputted.
# Logic used (Pseudocode or just plain English): Pseudocode
#------------------------------------------------------------------------
# Program Inputs:
year = int(input('Enter year of a Ferrari 250 GTO: '))
#------------------------------------------------------------------------
# Program Outputs:

if year < 1962:
    print('Car did not exist yet!')
elif year <= 1964:
    print('The value of this Ferrari is $',18500)
elif year <= 1968:
    print('The value of this Ferrari is $',6000)
elif year <= 1971:
    print ('The value of this Ferrari is $',12000)
elif year <= 1975:
    print ('The value of this Ferrari is $',48000)
elif year <= 1980:
    print('The value of this Ferrari is $',200000)
elif year <= 1985:
    print('The value of this Ferrari is $',650000)
elif year <= 2012:
    print('The value of this Ferrari is $',35000000)
elif year <= 2014:
    print('The value of this Ferrari is $',52000000)
else:
    print('This Ferrari is too new to value!')
#------------------------------------------------------------------------