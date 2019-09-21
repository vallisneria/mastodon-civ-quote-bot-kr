from mastodon import Mastodon
import json
import random as rand


with open("../key/mastodon.json", encoding="utf-8") as key:
    token: dict = json.load(key)

Civbot = Mastodon(
    access_token=token["key"],
    api_base_url='https://mastodon.social'
)

with open("./quotes/quotes.json", encoding="utf-8") as fp:
    quotes: dict = json.load(fp)

i = rand.randint(0, len(quotes)-1)

post = "["+quotes[i]["name"]+"]\n" + \
    quotes[i]["quote"]+"\n- " + \
    quotes[i]["author"]+"\n#"+quotes[i]["version"]

if "image" in quotes[i]:
    media = Civbot.media_post(quotes[i]["image"])
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")
