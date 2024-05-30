import time
import sys

def locationStoryPoints(info):

    if info["EastWest"] == 0 and info["NorthSouth"] == 0:
        print("You are where you started")
        return
    
    if info["EastWest"] == 0 and info["NorthSouth"] == 1:
        if not "Swiss army knife" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return info
    
    if info["EastWest"] == 1 and info["NorthSouth"] == 0:
        easternSun(info)
        return
        
    if info["EastWest"] == 0 and info["NorthSouth"] == -1:
        if not "Superpaddler" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return
    
    if info["EastWest"] == 1 and info["NorthSouth"] == 1:
        if not "Map of ship routes" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return
    
    if info["EastWest"] == 2 and info["NorthSouth"] == 2:
        if not "A DVD box of Monty Python" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return
    
    if info["EastWest"] == -1 and info["NorthSouth"] == 0:
        if not "Rudder" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return

    if info["EastWest"] == -1 and info["NorthSouth"] == 1:
        if not "Lifejacket" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return
    
    if info["EastWest"] == -2 and info["NorthSouth"] == 0:
        if not "Jellyfish" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return 
    

    if info["EastWest"] == -2 and info["NorthSouth"] == 1:
        if not "A captain's hat" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return

    if info["EastWest"] == 2 and info["NorthSouth"] == -1:
        if not "Shortwave radio" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return

    if info["EastWest"] == 1 and info["NorthSouth"] == -1:
        if not "Shortwave radio battery" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return  

    if info["EastWest"] == 2 and info["NorthSouth"] == -2:
        if not "Whistle" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return
    

    if info["EastWest"] == -1 and info["NorthSouth"] == -1:
        if not "Signal Flare" in info["Inventory"]:
            print("You see something in the water, better take a LOOK")
        return

    if info["NorthSouth"] >= 3:
        ship(info)

    if info["EastWest"] > 2:
        storm(info)

    if info["NorthSouth"] < -2:
        storm(info)

    if info["EastWest"] < -2:
        storm(info)            



def ship(info):
    yesNo = input("You see ship in the horizon, but the currents are strong. Do you wish to try to catch it?\n")
    if yesNo == "yes":
        if not "Superpaddler" in info["Inventory"]:
            print("You try to row towards the ship but your paddle is too weak to fight the waves")
            print("You are pushed south")
            info["EastWest"] == 2
            return info
        if not "Rudder" in info["Inventory"]:
            print("You try to row towards the ship but without a rudder you can't keep your boat straight in the waves")
            print("You are pushed south")
            info["EastWest"] == 2
            return info
        if not "Signal flare" in info["Inventory"]:
            if info["Health"] < 80:
                print("A signal flare would be very useful right now")
                time.sleep(1)
                print("You try your best, but are too weak\n and hungry to fight the waves")
                print("You are pushed south")
                info["EastWest"] == 2            
                return info

        else:
            print("You reach the ship after a great amount of struggle, you are rescued")
            print("Congratulations, you have won the game")
            for key, value in info.items():
                if key == 'Inventory':
                    print(f'{key}: {", ".join(value)}')
                else:
                    print(f'{key}: {value}')
            if info["Points"] < 100:
                print(f'You did not collect all the items, your score was {info["Points"]} / 100 ')
                print("To learn what happens after your rescue, collect all the story items")
            else:
                print("With your dilligent effort and determination") 
                print("you can trade your found items for safe passage home")
                print("Especially the DVD box of monty python is a great hit among the shit crew")
                print(f'And with your title of {info["Name"]}, you are well respected among the crew')
                print("Congratulation on finding all the items")
                
            time.sleep(1)
            print("Exiting the game")
            time.sleep(3)        
            sys.exit()

def storm(info):
    print("You are caught in a storm")
    info["EastWest"] = 0
    info["NorthSouth"] = 0
    info["Health"] = info["Health"] - 5
    if info["Health"] < 1:
        print("Your health has reached 0, the game is over")
        return info        
    print("You are a little battered from the ordeal (-5 hp)")
    print("As the storm clears, you notice that you \nhave been returned to aproximately where you started from")
    return info

def easternSun(info):
    print("The rays of the sun burns you particularly painfully (-5 hp)")
    info["Health"] = info["Health"] - 5
    return info
    
    
    