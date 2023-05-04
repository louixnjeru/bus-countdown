class Printer:
    
    def checkWaypoint(self,waypoint,newLine):
        if waypoint[0:10] == 'BikePoints' or waypoint[0:8] == 'TaxiRank':
            return " "
        else:
            if newLine == True:
                return f" Buses towards:\n {waypoint}"
            else:
                return f" Buses towards {waypoint}"
    
    def printArrivals(self,busTimes,stopDetails):
        print("="*60)
        print(f" {stopDetails['stopLetter'].ljust(8)}\t{stopDetails['name']}")
        print("-"*60)
        print(self.checkWaypoint(stopDetails['waypoint'],True))
        if len(busTimes) > 0:
            for bus in busTimes:
                print("-"*60)
                print(f" {bus['route'].ljust(8)}{bus['destination'].ljust(41)}{bus['due']}")
        else:
            print("-"*60)
            print(" No buses due within in the next 30 minutes")
        print("="*60)
        
    def printStationList(self,stationList):
        if len(stationList["matches"]) == 0:
            print("No matches found")
            return False
        elif len(stationList["matches"]) == 1:
            return stationList["matches"][0]
        else:
            print(f"Found {stationList['total']} result(s) that match '{stationList['query']}':")
            for i, stop in enumerate(stationList["matches"]):
                print(str(i+1).ljust(5),stop["name"],stop["id"])
            print()
            stopNum = self.getStopNum(len(stationList["matches"]))
            return stationList["matches"][int(stopNum-1)]
    
    def printStopList(self,stopList,stationName):
        print("="*60)
        print(f"{' '.ljust(5)}{stationName}")
        print("="*60)
        for i,stop in enumerate(stopList):
            if stop["name"] == stationName:
                print(f"{' '.ljust(5)}{stop['stopLetter'].ljust(13)}")
            else:
                print(f"{' '.ljust(5)}{stop['stopLetter'].ljust(7)} - {stop['name']}")
            print(f"{str(i+1).ljust(4)}"+self.checkWaypoint(stop['waypoint'], False))
            print(f"{' '.ljust(5)}Route(s) {', '.join(map(str.upper, stop['routes']))}")
            print("-"*60)
        print()
        stopNum = self.getStopNum(len(stopList))
        return stopList[int(stopNum-1)]
    
    def getStopNum(self,numOfStops):
        while True:
            try:
                stopNum = int(input("Select your stop by entering its number: "))
                if stopNum > 0 and stopNum <= numOfStops:
                    break
                else:
                    print("ERROR - Invalid number entered")
            except ValueError:
                print("ERROR - Please enter a number")
        return stopNum