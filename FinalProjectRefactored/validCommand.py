import time
import sys
import locationEventLibrary
import allowedActions
import validCommand
import util
import locationItemLibrary


def allCommands(command, info):

    if command == "quit":
        util.quitter(info)
        return info

    if command in {"hint", "help", "help me"}:
        util.hint()
        return info
    
    if command in {"restart"}:
        util.restart(info)
        return info
        
        
    if command == "info":
        util.playerStats(info)
        return info

    if command == "eat":
        allowedActions.apples(info)
        return info      
    
    if command in {"look around", "look", "seek"} and info["Inventory"] == "":
        print("You find a Compass, a Paddle and a Burlap Sack.")
        info = util.startingInventory(info)   
        print('To use the paddle, type "row" and the direction you wish to go. \nFor example "row east"')
        return info

    if command in {"look", "seek", "look around"} and info["Inventory"] != "Empty":
        locationItemLibrary.locationSpecificItems(info)

    
    if command in {"hint", "help", "help me"}:
        util.hint()
        return info
    
    if command in {"bag" ,"burlap sack", "sack" "search sack"}:
        util.bag()
        if not "Bag of apples" in info["Inventory"]:
            info["Inventory"].append("Bag of apples")
        return info
    
    if command[0:3] == "row":
        allowedActions.row(info, command)
        return info

    if command == "radio":
        allowedActions.row(info)
        return info        


    


