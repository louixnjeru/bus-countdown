import apiAccess as access
import printer
import sanitise as san
#import keyboard

def sendError():
    print('An error occurred - Please try again')

def getStation():
    stopQuery = input("Enter stop location name: ")
    stationList = api.getStopNames(stopQuery)
    selectedStation = p.printStationList(stationList)
    if not selectedStation:
        return False
    else:
        return (selectedStation["id"], selectedStation["name"])
    
def getStop(stationId,stationName):
    stationStops = api.getStopsById(stationId)
    sanitisedStops = s.findBusStops(stationStops)
    if len(sanitisedStops) > 1:
        return p.printStopList(sanitisedStops,stationName)
    elif len(sanitisedStops) == 1:
        return sanitisedStops[0]
    else:
        return False
    
def generateArrivals(stopInfo):
    busTimes = api.getArrivalsForStop(stopInfo["id"])
    busTimes = s.sanitiseArrivals(busTimes)
    p.printArrivals(busTimes,stopInfo)
    
    
if __name__ == "__main__":
    api = access.API()
    p = printer.Printer()
    s = san.Sanitiser()
    
    while True:
        station = getStation()
        if not station:
            sendError()
            continue
        stationId, stationName = station
        
        stop = getStop(stationId, stationName)
        if not stop:
            sendError()
            continue
        
        generateArrivals(stop)
        
        print()
        print('Press Q to quit, or any other key to continue: ')
        
        ans = input()
        if ans.upper() == 'Q': break
        """
        if keyboard.is_pressed('Q'):
            break
        """
        print('='*60)
        print('='*60)
        print('='*60)


        
    
    