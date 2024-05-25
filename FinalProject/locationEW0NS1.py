import util
def EW0NS1(info):

    print("Winds are slightly stronger here")
    
    while True:
        command = input("\nWhat do you wish to do?\n")
        command = command.lower()
        if command == "quit":
            util.quitter(info)
        

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
            print("Towards north, you see the lights of a city. LAND!\nDo you proceed towards it?")
            while True:
                command = input("Yes or No\n")
                command = command.lower()
                if command == "yes":
                    if not "Superpaddle" in info["Inventory"]:
                        print("Your paddle is not strong enough to fight the winds")
                        break
                if command == "no":
                    break
