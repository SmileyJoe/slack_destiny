from pprint import pprint
from settings import *
import requests
import json
from destiny import *
from helpers import Time
from slack import *

destiny = Destiny()
destiny.set_api_key(BUNGIE_API_KEY)

users = []

FORMAT_COMPACT = 1
FORMAT_EXPANDED = 2

messageFormat = FORMAT_COMPACT

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
        hours = seconds/60/60
        elapsed = Time.elapsed(seconds)

        if messageFormat == FORMAT_COMPACT:
            message = "\n*{}:* {} hours ({})".format(key, hours, elapsed)
        else:
            message = "\n\n*{}*\nTime: {} hours ({})\nMax Light: {}".format(key, hours, elapsed, maxLight)

        valueTuple = (key, hours, message)
        users.append(valueTuple)

users.sort(key=lambda tup: tup[1], reverse=True)

slackMessage = ""
for user in users:
    slackMessage += user[2]

slack = Slack()
slack.token(SLACK_TOKEN)
slack.channel(SLACK_CHANNEL)
slack.userName("Destiny Bot")
slack.text(slackMessage)
slack.postMessage()
#pprint(slackMessage)
