def getfare(src,dst):
    map = { "TH" : 800, "GA" : 600, "IC" : 750, "HA" : 900, "TE" : 1400, "LU" : 1200, "NI" : 1100, "CA" : 1500}
    fare = 0
    places = list(map)
    if src == dst:
        print("Error!")
        exit()
    elif places.index(src)>places.index(dst):
        for i in range(places.index(src)+1,len(map)):
            fare += map[places[i]]
            print(places[i]+"->"+str(map[places[i]]))
        for i in range(0,places.index(dst)+1):
            print(places[i]+"->"+str(map[places[i]]))
            fare += map[places[i]]
        print(fare/200)
        fare = round(fare/200)
    return fare
src = input("Enter Source: ").upper()
dst = input("Enter Destination: ").upper()
print(getfare(src,dst))