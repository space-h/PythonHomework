import time
import sys

def locationStoryPoints(info):

    if info["EastWest"] == 0 and info["NorthSouth"] == 0:
        print("You are where you started")
        return
    
    if info["EastWest"] == 0 and info["NorthSouth"] == -1:
        print("You have rowed south and unfortunately died")
        info["Health"] = 0
        return info
    
    if info["EastWest"] == 0 and info["NorthSouth"] == 1:
        print("You have rowed north")
        return
        
    if info["EastWest"] == 0 and info["NorthSouth"] == 1:
        print("You have rowed north")
        return
    
    if info["EastWest"] == 2 and info["NorthSouth"] == 0:
        print("You have even further rowed east")
        return
    
    if info["EastWest"] == 1 and info["NorthSouth"] == 1:
        print("You have rowed East and North")
        return
    
    if info["EastWest"] == -1 and info["NorthSouth"] == -1:
        print("You have rowed West and South")
        return

    if info["NorthSouth"] >= 3:
        ship(info)

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
        if info["Health"] < 80:
            print("You are too weak and hungry to fight the waves")
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
            time.sleep(1)
            print("Exiting the game")
            time.sleep(3)        
            sys.exit() 
    
    