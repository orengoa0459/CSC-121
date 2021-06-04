#Import python support file
import OrengoAnthony_game_functions as gameFunctions
import os
 

# This program is a version of the "Rock", "Paper", "Scissors" game, using the python
#console. The user will have the option to play a 1, 2, or 3 round game. The winner will
#be display to the user upon completion of the game. 
# Date 05/31/2021
# CSC121- M2Lab Code Modularizing
# Anthony Orengo
 
#Pseudocode
#1. Import game functions file "OrengoAnthony_game_functions".
#2. Define main function and create an active menu for the user.
#3. Declare and initialize input and loop sentinel.
#4. Create a while loop to control main menu flow.
#5: Add 4 options to the menu (1 round, 2 round, 3 round,Exit)
#6: Add the game function to the appropriate menu choice(Ex: gameFunctions.gameOne() will go with menu choice 1)
#7: ****Refer to OrengoAnthony_game_functions for additional information.
#8: End the program/loop by changing loop variable to true.  

# main function
def main():
    choice = ""
    menuLoop = False
    while menuLoop == False:
        gameFunctions.mainMenu()
        # Get input from user
        choice = input("\nChoose from the Menu --> ")
        if choice == "1":
            #Start Highest Number game 
            gameFunctions.gameOne()
        elif choice == "2":
            #Start Highest Number game 
             gameFunctions.gameTwo()
        elif choice == "3":
            #Start Highest Number game 
            gameFunctions.gameThree()  
        elif choice == "4":
            #Exits program
            print("Goodbye")
            menuLoop = True
            exit()
        else:
           print(gameFunctions.displayMessageInvalid())
 
# Call the main function.

    
if __name__ == "__main__":
    
    main()





    


