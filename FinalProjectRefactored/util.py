import time
import sys



def quitter(info):
    quitcheck = 0
    time.sleep(1)
    print("\nPLAYERINFO:")
    for key, value in info.items():
        if key == 'Inventory':
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')
        quitcheck += 1    
    if quitcheck == 6:
        time.sleep(2)
        print("\nGame over, you remain lost at sea")
        time.sleep(2)
        sys.exit()

def restart(info):
        noYes = input("Are you sure you want to restart, y/n?\n")
        if noYes in {"yes", "y"}:
            print("\nRestarting the game")
            time.sleep(2)
            info["Health"] = 0
            return info
        else:
            print("Returning to game\n")
            return info


def playerStats(info):
    print("\nPLAYERINFO:")
    for key, value in info.items():
        if key == 'Inventory':
            print(f'{key}: {", ".join(value)}')
        else:
            print(f'{key}: {value}')
    print("")



def startingInventory(info):
    info["Inventory"] = ["Paddle", "Burlap Sack", "Compass"]
    time.sleep(1)
    return info
    
    
    
def apples(info):
    if info["Health"] <= 94:
        info["Health"] = info["Health"] + 5
        print("\nYou are healed")
        time.sleep(1)
        print(info["Health"], "/ 100")
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


def bag():
    print("Bag is full of appels, they look tasty and will help with both thirst and hunger")
    print('To consume the apples, input "eat"')

def hint():
    print("It is usually good idea to LOOK around and to use the INFO you have been given")
    helpNoYes = input("Would you like additional assitance?\n")
    if helpNoYes in {"yes", "y"}:
        print('The goal of the game is to find the \nitems using the "Look" command when in a location')
        print("You need some amount of items that will \nhelp you before you can attempt to be rescued")
    else:
        return    

def nameLegalCheck(legalCommands):
    noGoNames = legalCommands
    while True:
        name = input("Hello, please input a name to begin\n")
        name = name.lower()

        if name in noGoNames:
            print(f'\nName "{name}" is no good, choose a different one')
            continue
            
        else:
            name = name.capitalize()
            return name
            










        
