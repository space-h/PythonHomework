

def locationSpecificItems(info):
    if info["EastWest"] == 1 and info["NorthSouth"] == 0:
        info = EW1SN0(info)
        return info
    
    if info["EastWest"] == -1 and info["NorthSouth"] == 0:
        info = EW9SN0(info)
        return info
    
def EW9SN0(info):     

    if "Rudder" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Rudder" in info["Inventory"]:
        yesNo = input("You see boat rudder, it could be useful, do you wish to pick it up?\n")
        if yesNo == "yes":
            if not "Rudder" in info["Inventory"]:
                info["Inventory"].append("Rudder")
                info["Points"] =  info["Points"] + 5
                return info
        else:
            return info


def EW1SN0(info):

    if "Superpaddler" in info["Inventory"]:
         print("You have found everything you can from here")
         return info

    if not "Superpaddler" in info["Inventory"]:
        yesNo = input("You see Superpaddler, do you wish to pick it up?\n")
        if yesNo == "yes":
            if not "Superpaddler" in info["Inventory"]:
                info["Inventory"].append("Superpaddler")
                info["Points"] =  info["Points"] + 5
                return info
        else:
            return info
    
    
            
    
    
