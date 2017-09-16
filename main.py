from pprint import pprint
from settings import *
import requests
import json
from destiny import *
from helpers import Time

destiny = Destiny()
destiny.set_api_key(BUNGIE_API_KEY)

for key, value in DESTINY_USERS.items():
    profile = destiny.get_profile(value)
    characters = profile["Response"]["characters"]["data"]
    characterIds = profile["Response"]["profile"]["data"]["characterIds"]
    seconds = 0
    maxLight = 0

    for characterId in characterIds:
        character = characters[characterId]
        seconds += int(character["minutesPlayedTotal"])*60
        light = int(character["light"])

        if light > maxLight:
            maxLight = light

    if seconds > 0:
        message = "{}: Time:{} Light:{}".format(key, Time.elapsed(seconds), maxLight)

        pprint(message)