import locationItemFunctions

def locationSpecificItems(info):

    #start spot
    if info["EastWest"] == 0 and info["NorthSouth"] == 0:
        print("You are where you started from")
        print("You see a lot of ocean and the sun in your East")

    #Swiss army knife
    if info["EastWest"] == 0 and info["NorthSouth"] == 1:
        info = locationItemFunctions.EW0SN1(info)
        return info
    
    #Superpaddler
    if info["EastWest"] == 0 and info["NorthSouth"] == -1:
        info = locationItemFunctions.EW0SN9(info)
        return info
    
    #Map of routes
    if info["EastWest"] == 1 and info["NorthSouth"] == 1:
        info = locationItemFunctions.EW1SN1(info)
        return info
    
    #Monty Python dvd
    if info["EastWest"] == 2 and info["NorthSouth"] == 2:
        info = locationItemFunctions.EW2SN2(info)
        return info
    
    #Rudder
    if info["EastWest"] == -1 and info["NorthSouth"] == 0:
        info = locationItemFunctions.EW9SN0(info)
        return info     
    
    #Signal Flare
    if info["EastWest"] == -1 and info["NorthSouth"] == -1:
        info = locationItemFunctions.EW9SN9(info)
        return info
     
    #Jellyfish             
    if info["EastWest"] == -2 and info["NorthSouth"] == 0:
        info = locationItemFunctions.EW8SN0(info)
        return info
    
    #Captain's hat  
    if info["EastWest"] == -2 and info["NorthSouth"] == 1:
        info = locationItemFunctions.EW8SN1(info)
        return info
      
    #Shortwave Radio
    if info["EastWest"] == 2 and info["NorthSouth"] == -1:
        info = locationItemFunctions.EW2SN9(info)
        return info
    
    #Whistle
    if info["EastWest"] == 2 and info["NorthSouth"] == -2:
        info = locationItemFunctions.EW2SN8(info)
        return info
    
    #nothingButSea  
    if info["EastWest"] == 1 and info["NorthSouth"] == 0:
        info = locationItemFunctions.nothingButSea(info)
        return info
    
    #nothingButSea  
    if info["EastWest"] == 0 and info["NorthSouth"] == -2:
        info = locationItemFunctions.nothingButSea(info)
        return info   
    
    #nothingButSea  
    if info["EastWest"] == 1 and info["NorthSouth"] == -1:
        info = locationItemFunctions.nothingButSea(info)
        return info
    
    #nothingButSea  
    if info["EastWest"] == 1 and info["NorthSouth"] == -2:
        info = locationItemFunctions.nothingButSea(info)
        return info
    
    #nothingButSea  
    if info["EastWest"] == 2 and info["NorthSouth"] == 0:
        info = locationItemFunctions.nothingButSea(info)
        return info
    
    #nothingButSea  
    if info["EastWest"] == 2 and info["NorthSouth"] == 1:
        info = locationItemFunctions.nothingButSea(info)
        return info
    
    #nothingButSea
    if info["EastWest"] == -2 and info["NorthSouth"] == 2:
        info = locationItemFunctions.nothingButSea(info)
        return info

    #nothingButSea           
    if info["EastWest"] == -2 and info["NorthSouth"] == -1:
        info = locationItemFunctions.nothingButSea(info)
        return info

    #nothingButSea                    
    if info["EastWest"] == -2 and info["NorthSouth"] == -2:
        info = locationItemFunctions.nothingButSea(info)
        return info
    
    #nothingButSea                
    if info["EastWest"] == -1 and info["NorthSouth"] == 2:
        info = locationItemFunctions.nothingButSea(info)
        return info



    

    
    

    






