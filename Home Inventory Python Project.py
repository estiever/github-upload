#----------------------------------------------------------------------------------------------------
# Program Name: Eric Stiever's Module 8, Option 2 Assignment
# Program Objective: Create a home inventory class that will be used by a national builder to maintain
# inventory of available houses in the country.  Allow user to output all the home inventory to a 
# text file.
#
# Logic used (Pseudocode or just plain English): Pseudocode
#----------------------------------------------------------------------------------------------------
# Program Inputs
class HomeInventory:
    # constructor
    def __init__(self):
        """
         squarefeet: number in integer format.
         address: string format
         city: string format
         state: string format
         zipcode: integer format
         Modelname: string format
         salestatus: string format (sold, available, under contract)
         
        """
        # Class attributes are listed below.
        self.__squarefeet = 0 
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zipcode = 0
        self.__modelname = ""
        self.__salesstatus = ""

    def AddHome(self):
        # Created new method to add a new home to inventory
        self.__squarefeet = int(input('Enter square feet: '))
        self.__address = input('Enter address: ')
        self.__city = input('Enter city: ')
        self.__state = input('Enter state: ')
        self.__zipcode = int(input("Enter zip code: "))
        self.__modelname = input('Enter model name: ')
        self.__salesstatus = input('Enter sales status (ex. sold, available, under contract): ')

    def SubHome(self):
        # Created a new method to remove a home from inventory
        self.__squarefeet = 0
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zipcode = 0
        self.__modelname = ""
        self.__salesstatus = ""
        print("Address Removed!")

    def UpdateHome(self):
        # Created a new method update home attributes
        self.__squarefeet = int(input('Enter square feet: '))
        self.__address = input('Enter address: ')
        self.__city = input('Enter city: ')
        self.__state = input('Enter state: ')
        self.__zipcode = int(input("Enter zip code: "))
        self.__modelname = input('Enter model name: ')
        self.__salesstatus = input('Enter sales status (ex. sold, available, under contract): ')
        print("Address Updated!")

    def getSquareFeet(self):
        return self.__squarefeet

    def getAddress(self):
        return self.__address

    def getCity(self):
        return self.__city

    def getState(self):
        return self.__state

    def getZipCode(self):
        return self.__zipcode

    def getModelName(self):
        return self.__modelname

    def getSalesStatus(self):
        return self.__salesstatus

# --------------------------------------------------------------------------------  
# Program Outputs
if __name__ == '__main__':
    # Create a list to store home address inventory information
    home_list = []
    while True:
    # print out menu items
        print('1. Add a new home: ')
        print('2. Update home: ')
        print('3. Remove home: ')
        print('4. Save to file.')
        print('5. Exit.')
    # user inputs a menu item
        option = int(input('Enter a menu item number: '))
        # Adds new home to inventory, which is stored in the home_list list.
        if option == 1:
            temp = HomeInventory()
            temp.AddHome()
            home_list.append(temp)

        # Updates home attributes from inventory.
        elif option == 2:
            address = input('Enter address to update: ')
            index = -1
            for i in range(len(home_list)):
                if home_list[i].getAddress() == address:
                    index = i
                    break
                else: 
                    print('Address not found.')
            if (index != -1):
                home_list[index].UpdateHome()
        # Deletes a home from inventory.
        elif option == 3:
            address = input('Enter address to remove: ')
            index = -1
            for i in range(len(home_list)):
                if home_list[i].getAddress() == address:
                    index = i
                    break
            if (index != -1):
                home_list[index].SubHome()
                del home_list[index]
            else: 
                print('Address not found.')

        # Saves to file name home.txt
        elif option == 4:
            myfile = open("home.txt", "w")
            for x in range(len(home_list)):
                myfile.write(str(home_list[x].getSquareFeet())+ '\n')
                myfile.write(str(home_list[x].getAddress())+ '\n')
                myfile.write(str(home_list[x].getCity())+ '\n')
                myfile.write(str(home_list[x].getState())+ '\n')
                myfile.write(str(home_list[x].getZipCode())+ '\n')
                myfile.write(str(home_list[x].getModelName())+ '\n')
                myfile.write(str(home_list[x].getSalesStatus())+ '\n')
        # Exits program
        elif option == 5:
            break

        else:
            print('Invalid option!  Please enter a valid option number.')
        







