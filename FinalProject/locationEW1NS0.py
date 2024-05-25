import time
import util
import startSpot
import locationEW2NS0


def EW1NS0(info):
    quitcheck = 0
    print("The sun is blazing hot, you lose 5 hp")
    info["Health"] = info["Health"] - 5
    if info["Health"] <= 1:
        print("Your health has reached 0, you have lost\n")
        time.sleep(2)
        for key, value in info.items():
            print(f'{key}: {value}')
            quitcheck += 1
            if quitcheck == 6:
                time.sleep(5)
                sys.exit()

    while True:
        command = input("\nWhat do you wish to do?\n")
        command = command.lower()
        if command == "quit":
            util.quitter(info)

        if command == "row west":
            print("You row away from the sun")
            info["EastWest"] = info["EastWest"] - 1
            startSpot.startingSpot(info)

        if command == "row east":
            print("You again row towards blazing the sun")
            info["EastWest"] = info["EastWest"] + 1
            locationEW2NS0.EW2NS0(info)
      

        if command in {"hint", "help", "help me"}:
            util.hint()
            continue
 
        if command == "info":
                util.playerStats(info)                
        if command in {"open bag", "bag", "search bag"}:
            util.bag()
            continue
        if command[0:3] == "eat":
            util.apples(info)
        if command[0:4] == "look":
            print("You see a better looking paddle, do you wish to pick it up")
            while True:
                command = input("Yes or No\n")
                command = command.lower()
                if command == "yes":
                    if not "Superpaddle" in info["Inventory"]:
                        info["Inventory"] = info["Inventory"] + "Superpaddle"
                        break
                if command == "no":
                    break
        else:
            print("Command unclear")
            continue
                
            
    

            
        
    return info


