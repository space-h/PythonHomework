import util
def EW9NS0(info):
    quitcheck = 0 
    print("The sun is warm on your back, it's pleasant, you recover 5 hp")
    if info["Health"] <= 94:
        info["Health"] = info["Health"] + 5
        info["Points"] = info["Points"] + 10
    elif info["Health"] >= 95:
        info["Health"] = 100
        info["Points"] = info["Points"] + 10

    while True:
        command = input("What do you wish to do?\n")

        if command == "quit":
            util.quit(command)
            
   
        if command == "info":
            util.playerStats(info)
            continue
        if command in {"open bag", "bag", "search bag"}:
            util.bag()
            continue
        if command[0:3] == "eat":
            util.apples(info)
        if command[0:4] == "look":
            print("You see a boat rudder, do you wish to pick it up")
            while True:
                command = input("Yes or No\n")
                command = command.lower()
                if command == "yes":
                    if not "Rudder" in info["Inventory"]:
                        info["Inventory"] = info["Inventory"] + "Rudder"
                        break
                if command == "no":
                    break
 
       
    return info
