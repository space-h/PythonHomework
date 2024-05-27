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
        if info["Points"] <=20:
            info["Points"] += 2
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
        if info["Points"] <=20:
            info["Points"] += 2
        print("\nYou are healed")
        time.sleep(1)
        print(info["Health"], "/ 100")
        return info

    if info["Health"] == 100:
        print("\nYou are fully healed")        
        return info

def bag():
    print("Bag is full of appels, they look tasty and will help with both thirst and hunger")
    print('To consume the apples, write "eat"')

def hint():
    print("It is usually good idea to LOOK around and to use the INFO you have been given")

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
            










        
