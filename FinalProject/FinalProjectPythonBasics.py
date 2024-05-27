import time
import sys
import locationEW1NS0
import locationEW9NS0
import locationEW0NS1
import locationEW0NS9
import util


 
info = {"Name": "Empty", "Inventory": "", "Health": 90, "Points": 0, "EastWest": 0, "NorthSouth":0}
info["Name"] = util.nameLegalCheck()
info["Name"] = info["Name"].capitalize()

print(f"Hello {info["Name"]}, nice to meet you. You have gained 10 points.\n\nType 'info' to see your player info in the future")
print('Type "quit" to end the game. You will see your player info and the game will end\n')
info["Points"] = info["Points"] + 10

print("You are stranded at sea in a small boat")


while True:
    command = input("\nWhat do you wish to do?\n")
    command = command.lower()
    
    if command == "quit":
        util.quitter(info)
        continue

    if command in {"hint", "help", "help me"}:
        util.hint()
        continue
    
        
    if command == "info":
        util.playerStats(info)
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
        for key, value in info.items():
            print(f'{key}: {value}')
        continue

    if command in {"open bag", "bag", "backbag", "search bag"}:
        util.bag()
        if not "Bag of apples" in info["Inventory"]:
            info["Inventory"] = info["Inventory"] + "Bag of apples"
        continue

    if command == "row east":
        print("You row towards the sun, it is morning")
        info["EastWest"] = info["EastWest"] + 1
        info = locationEW1NS0.EW1NS0(info)
        #Jump to file locationEW1NS0
    
    if command == "row west":
        print("You row away from the sun, it is morning")
        info["EastWest"] = info["EastWest"] - 1
        info = locationEW9NS0.EW9NS0(info)
        #Jump to file locationEW9NS0
        
    if command == "row north":
        print("You row north, sun is at your right, it is morning")
        info["EastWest"] = info["NorthSouth"] + 1
        info = locationEW0NS1.EW0NS1(info)
        #Jump to file locationEW0NS1
    
    if command == "row south":
        print("You row south, sun is at your left, it is morning")
        info["EastWest"] = info["NorthSouth"] - 1
        info = locationEW0NS9.EW0NS9(info)
        #Jump to file locationEW0NS9

    
    if command[0:3] == "eat":
            util.apples(info)
            continue

   
    else:
        print(command)
        print("Unclear, please try again\n")
        continue




