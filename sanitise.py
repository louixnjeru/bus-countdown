class Sanitiser:
    
    def checkAdditionalProperties(self,stop):
        if len(stop["additionalProperties"]) == 0:
            return " "
        elif len(stop["additionalProperties"]) > 1 and stop["additionalProperties"][1]["key"] == "Towards":
            return stop["additionalProperties"][1]["value"]
        else:
            return stop["additionalProperties"][0]["value"]
    
    def findBusStops(self,station):
        stopList = []
        if "children" in station and len(station["children"]) > 0:
            for child in station["children"]:
                if len(station["children"]):
                    stopList += self.findBusStops(child)
                if child["stopType"] == "NaptanPublicBusCoachTram" and len(child["lineModeGroups"]) != 0:
                    stopList.append({
                        "id" : child["naptanId"],
                        "name" : child["commonName"],
                        "stopLetter" : child["indicator"],
                        "routes" : child["lineModeGroups"][0]["lineIdentifier"],
                        "waypoint" : self.checkAdditionalProperties(child)
                        })
        return stopList
    
    def sanitiseArrivals(self,busTimes):
        if len(busTimes) == 0:
            return []
        else:
            sortedList = sorted(busTimes, key=lambda x: x['timeToStation'])
            sanitisedList = []
            for entry in sortedList:
                sanitisedList.append({
                    "destination" : entry["destinationName"],
                    "bearing" : entry["bearing"],
                    "direction" : entry["direction"],
                    "waypoint" : entry["towards"],
                    "route" : entry["lineName"],
                    "stopSign" : self.checkStopName(entry["platformName"]),
                    "stopId" : entry["naptanId"],
                    "stopName" : entry["stationName"],
                    "dueSeconds" : entry["timeToStation"],
                    "due" : self.calculateTime(entry["timeToStation"]),
                    "vehicleId" : entry["vehicleId"]
                    })
            return sanitisedList
        
    def checkStopName(self,stopName):
        if stopName == 'null':
            return " "
        else:
            return stopName
        
    def calculateTime(self,time):
        if time <= 60:
            return "Due"
        elif time > 60 and time <= 120:
            return "1 min"
        else:
            return f"{int(time/60)} mins"

