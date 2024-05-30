import time
import sys
import locationEventLibrary

def apples(info):
    if "Bag of apples" in info["Inventory"]:
        if info["Health"] <= 94:
            info["Health"] = info["Health"] + 5
            print("\nYou are healed")
            time.sleep(1)
            print(f'HP: {info["Health"]} / 100')
            return info
        elif info["Health"] == 100:
            print("\nYou are fully healed")
            print(info["Health"], "/ 100")
            time.sleep(1)
            return info
        
        elif info["Health"] >= 95:
            info["Health"] = 100
            print("\nYou are healed")
            time.sleep(1)
            print(info["Health"], "/ 100")
            return info

        if info["Health"] == 100:
            print("\nYou are fully healed")        
            return info
    else:
        print("You have nothing to eat")
        return info



def row(info, command):
    if "Paddle" in info["Inventory"]:
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

    else:
        print("You can't row without a Paddle")


def radio(info):
    if "Shortwave radio" in info["Inventory"]:
        if "Shortwave radio battery" in info["Inventory"]:

            print("You find the ship frequency after a great amount of struggle")
            print("They inform you that they are coming to rescue you")
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
        else:
            print("You need a working radio battery")
            return info
    else:
        print("You have no radio")
        return info