from mastodon import Mastodon
from datetime import datetime
import json
import random as rand


with open("./key/key.json", encoding="utf-8") as key:
    token: dict = json.load(key)

Civbot = Mastodon(
    access_token=token["key"],
    api_base_url='https://mastodon.social'
)


time = datetime.today().minute
if (time >= 40):
    with open("./quotes/civ5quotes.json", encoding="utf-8") as fp:
        quotes: dict = json.load(fp)
elif (time >= 20):
    with open("./quotes/civBEquotes.json", encoding="utf-8") as fp:
        quotes: dict = json.load(fp)
else:
    with open("./quotes/civ6quotes.json", encoding="utf-8") as fp:
        quotes: dict = json.load(fp)


i = rand.randint(0, len(quotes)-1)

if quotes[i]["author"] is None:
    post = "["+quotes[i]["name"]+"]\n" + \
        quotes[i]["quote"]+"\n#"+quotes[i]["version"]
else:
    post = "["+quotes[i]["name"]+"]\n" + \
        quotes[i]["quote"]+"\n- " + \
        quotes[i]["author"]+"\n#"+quotes[i]["version"]


if "image" in quotes[i]:
    media = Civbot.media_post(quotes[i]["image"])
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")
