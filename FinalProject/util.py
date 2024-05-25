import time
import sys



def quitter(stats):
    quitcheck = 0
    time.sleep(1)
    print("\nPLAYERINFO:")
    for key, value in stats.items():
        print(f'{key}: {value}')
        quitcheck += 1    
    if quitcheck == 6:
        time.sleep(2)
        print("\nGame over, you remain lost at sea")
        time.sleep(2)
        sys.exit()

def playerStats(stats):
    print("\nPLAYERINFO:")
    for key, value in stats.items():
        print(f'{key}: {value}')
    print("")
    

 
    
    
def apples(stats):
    if stats["Health"] <= 94:
        stats["Health"] = stats["Health"] + 5
        if stats["Points"] <=20:
            stats["Points"] += 2
        print("\nYou are healed")
        time.sleep(1)
        print(stats["Health"], "/ 100")
        return stats
    elif stats["Health"] == 100:
        print("\nYou are fully healed")
        print(stats["Health"], "/ 100")
        time.sleep(1)
        return stats
    
    elif stats["Health"] >= 95:
        stats["Health"] = 100
        if stats["Points"] <=20:
            stats["Points"] += 2
        print("\nYou are healed")
        time.sleep(1)
        print(stats["Health"], "/ 100")
        return stats

    if stats["Health"] == 100:
        print("\nYou are fully healed")        
        return stats

def bag():
    print("Bag is full of appels, they look tasty and will help with both thirst and hunger")

def hint():
    print("It is usually good idea to LOOK around and to use the INFO you have been given")

def nameLegalCheck():
    noGoNames = ["look", "quit", "info", "eat", "row", "bag", "hint"]
    while True:
        name = input("Hello, please input a name to begin\n")

        if name in noGoNames:
            print(f'\nName "{name}" is no good, choose a different one')
            continue
            
        else:
            return name
            










        
