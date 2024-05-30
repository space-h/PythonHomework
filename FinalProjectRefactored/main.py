import time
import sys
import locationEventLibrary
import allowedActions
import validCommand
import util

info = {"Name": "Empty", "Inventory": "", "Health": 0, "Points": 0, "EastWest": 0, "NorthSouth":0}

while info["Health"] == 0:
         
        info["Health"] = 50
        info["Inventory"] = ""
        info["EastWest"] = 0
        info["NorthSouth"] = 0
        info["Points"] = 0


        legalCommands = ["yes", "no", "restart", "y", "n", "look", "info", "hint", "help", "help me", "burlap sack", "sack", "look around", "bag", "backbag", "search bag", "search", "row north", "row east", "row west", "row south", "eat", "quit"]

        info["Name"] = util.nameLegalCheck(legalCommands)


        print(f"\n\nHello {info["Name"]}, nice to meet you.")
        print("Type 'info' to see your player info in the future")
        print('Type "quit" to end the game. \nYou will see your player info and the game will end\n')
        info["Points"] = info["Points"] + 10
        print("You are stranded at sea in a small boat. Situation is bleak. You are all alone")


        while True:
            if info["Health"] == 0:
                 again = input("Play again, y/n\n")
                 if again in {"y", "yes"}:
                    print("\n")
                    break
                 else:
                    command = "quit"

            if info["Health"] > 0:
                command = input("\n\nWhat do you wish to do?\n")
                command = command.lower()

                 

            if command not in legalCommands:
                print(f'Unclear input "{command}", please try again\n')
                continue


            else:
                validCommand.allCommands(command, info)
                
    
   





