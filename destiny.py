from pprint import pprint
from settings import *
import requests
import json


class Destiny:
    __urlBase = "https://www.bungie.net/platform/destiny2/2"
    __apiKey = ""

    def set_api_key(self, apiKey):
        self.__apiKey = apiKey

    def get_profile(self, userId):
        url = self.__urlBase + "/Profile/" + userId + "?components=100,200"
        response = requests.get(url, headers=self.get_headers())
        return json.loads(response.content)

    def get_headers(self):
        return {'x-api-key': self.__apiKey}