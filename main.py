from pprint import pprint
from settings import *
import requests
import json
from destiny import *

destiny = Destiny()
destiny.setApiKey(BUNGIE_API_KEY)

for key, value in DESTINY_USERS.items():
    pprint(destiny.getProfile(value))
