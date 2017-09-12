from pprint import pprint
from settings import *
import requests
import json

class Destiny:
    __urlBase = "https://www.bungie.net/platform/destiny2/2"
    __apiKey = ""

    def setApiKey(self, apiKey):
        self.__apiKey = apiKey

    def getProfile(self, userId):
        url = self.__urlBase + "/Profile/" + userId + "?components=100,200"
        response = requests.get(url, headers=self.getHeaders())
        return json.loads(response.content)

    def getHeaders(self):
        return {'x-api-key': self.__apiKey}