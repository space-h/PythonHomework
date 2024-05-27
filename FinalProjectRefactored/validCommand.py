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
        
        
    if command == "info":
        util.playerStats(info)
        return info

    if command == "eat":
        allowedActions.apples(info)
        return info      
    
    if command in {"look", "seek", "look around"} and info["Inventory"] == "":
        print("You see a Compass, a Paddle and a Burlap Sack.")
        info = util.startingInventory(info)   
        print('To use the paddle, type "row" and the direction you wish to go. \nFor example "row east"')
        return info

    if command in {"look", "seek", "look around"} and info["Inventory"] != "Empty":
        locationItemLibrary.locationSpecificItems(info)

    
    if command in {"hint", "help", "help me"}:
        util.hint()
        return info
    
    if command in {"open bag", "bag", "backbag", "search bag", "search"}:
        util.bag()
        if not "Bag of apples" in info["Inventory"]:
            info["Inventory"].append("Bag of apples")
        return info

#Add max and min values to directions
    if command == "row east":
        info["EastWest"] = info["EastWest"] + 1
        info = locationEventLibrary.locationStoryPoints(info)
        return info
    
    if command == "row west":
        info["EastWest"] = info["EastWest"] - 1
        info = locationEventLibrary.locationStoryPoints(info)
        return info    
        

    if command == "row north":
        info["NorthSouth"] = info["NorthSouth"] + 1
        info = locationEventLibrary.locationStoryPoints(info)
        return info
    
    if command == "row south":
        info["NorthSouth"] = info["NorthSouth"] - 1
        info = locationEventLibrary.locationStoryPoints(info)
        return info
    


