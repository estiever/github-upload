#------------------------------------------------------------------------
# Program Name: Eric Stiever's Module 2, Option 2 Assignment
# Program Objective: Input various data elements related to a car and store it all as a dictionary. 
# Then, output the result.

# Logic used (Pseudocode or just plain English): Pseudocode
#------------------------------------------------------------------------
# Program Inputs: Prompt user to enter a car brand, model, year, starting odometer reading,
# an ending odometer reading, and the estimated miles per gallon consumed by the vehicle.

dict = {}
    car brand = input('Please enter a car brand: ')
    car model = input('Please enter a car model: ')
    car year = int(input('Please enter the model year of the car: '))
    start odometer = int(input('Please enter the starting odometer reading of the car: '))
    end odometer = int(input('Please enter the ending odometer reading of the car: '))
    est mpg = int(input('Please enter the estimated miles per gallon consumed by the vehicle: '))

#------------------------------------------------------------------------
# Program Outputs: (Python will print the dictionary contents in an unordered fashion.)
print('The contents of the dictionary are', dict)
#------------------------------------------------------------------------
