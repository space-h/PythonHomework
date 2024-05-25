import time
import sys
import locationEW1NS0
import locationEW9NS0
import locationEW0NS1
import locationEW0NS9
import util


 
playerInfo = {"Name": "Empty", "Inventory": "", "Health": 90, "Points": 0, "EastWest": 0, "NorthSouth":0}
playerInfo["Name"] = util.nameLegalCheck()
playerInfo["Name"] = playerInfo["Name"].capitalize()

print(f"Hello {playerInfo["Name"]}, nice to meet you. You have gained 10 points.\n\nType 'info' to see your player info in the future")
print('Type "quit" to end the game. You will see your player info and the game will end\n')
playerInfo["Points"] = playerInfo["Points"] + 10

print("You are stranded at sea in a small boat")


while True:
    command = input("\nWhat do you wish to do?\n")
    command = command.lower()
    
    if command == "quit":
        util.quitter(playerInfo)
        continue

    if command in {"hint", "help", "help me"}:
        util.hint()
        continue
    
        
    if command == "info":
        util.playerStats(playerInfo)
        continue
    
    if command in {"look", "seek", "look around"}:
        print("You see a PADDLE and a BACKBAG.")
        print('To use the paddle, type "row" and the direction you wish to go. \nFor example "row east"')
        break
    else:
        print('Command: "' + command + '" is unclear, please try again\n')


while True:
    command = input("\n\nwhat do you wish to DO?\n")
    command = command.lower()

    if command in {"hint", "help", "help me"}:
        util.hint()
        continue
    
    if command == "info":
        for key, value in playerInfo.items():
            print(f'{key}: {value}')
        continue

    if command in {"open bag", "bag", "backbag", "search bag"}:
        util.bag()
        if not "Bag of apples" in playerInfo["Inventory"]:
            playerInfo["Inventory"] = playerInfo["Inventory"] + "Bag of apples"
        continue

    if command == "row east":
        print("You row towards the sun, it is morning")
        playerInfo["EastWest"] = playerInfo["EastWest"] + 1
        playerInfo = locationEW1NS0.EW1NS0(playerInfo)
        #Jump to file locationEW1NS0
    
    if command == "row west":
        print("You row away from the sun, it is morning")
        playerInfo["EastWest"] = playerInfo["EastWest"] - 1
        playerInfo = locationEW9NS0.EW9NS0(playerInfo)
        #Jump to file locationEW9NS0
        
    if command == "row north":
        print("You row north, sun is at your right, it is morning")
        playerInfo["EastWest"] = playerInfo["NorthSouth"] + 1
        playerInfo = locationEW0NS1.EW0NS1(playerInfo)
        #Jump to file locationEW0NS1
    
    if command == "row south":
        print("You row south, sun is at your left, it is morning")
        playerInfo["EastWest"] = playerInfo["NorthSouth"] - 1
        playerInfo = locationEW0NS9.EW0NS9(playerInfo)
        #Jump to file locationEW0NS9

    
    if command[0:3] == "eat":
            util.apples(playerInfo)
            continue

   
    else:
        print(command)
        print("Unclear, please try again\n")
        continue




