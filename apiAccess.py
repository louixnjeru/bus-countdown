import json,requests

class API:
    
    def __init__(self):
        self.apiKey = {'app_key' :'c6a9fc6196c948c79075408ead9420fe'}
        
    def getStopNames(self,query):
        query = query.replace(' ','%20')
        try:
            response = requests.get(f"https://api.tfl.gov.uk/StopPoint/Search?query={query}&modes=bus",params=self.apiKey).json()
            return response
        except response.status_code != 200:
            return False
    
    def getStopsById(self,stopPointId):
        try:
            response = requests.get(f"https://api.tfl.gov.uk/StopPoint/{stopPointId}",params=self.apiKey).json()
            return response
        except response.status_code != 200:
            return False
        
    def getArrivalsForStop(self,stopId):
        try:
            response = requests.get(f"https://api.tfl.gov.uk/StopPoint/{stopId}/Arrivals",params=self.apiKey).json()
            return response 
        except response.status_code != 200:
            return False
        
    def getCoordinatesForPostcode(self,postcode):
        try:
            response = requests.get(f"https://api.postcodes.io/postcodes/{postcode}")
            return response 
        except response.status_code != 200:
            return False
    
    

