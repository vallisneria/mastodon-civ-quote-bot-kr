# 모듈 import 부분
from mastodon import Mastodon
import random as rand
import json
import os

# 메인 코드 부분
Civbot = Mastodon(
    access_token=os.environ["MASTODON_ACCESS_TOKEN"],
    api_base_url=os.environ["MASTODON_BASE_URL"]
)

with open("./quotes/civ5.json", encoding="utf-8") as json_file:
    quotes = json.load(json_file)

i = rand.choice(quotes)
post = ""

if "title" in i:
    post += "[" + i["title"] + "]\n"

if "quote" in i:
    post += i["quote"] + "\n"

if "author" in i:
    post += "- " + i["author"] + "\n"

if "version" in i:
    post += "#" + i["version"]


print(post)

if "_file" in i:
    medialocation = "." + i["_file"]
    media = Civbot.media_post(medialocation, mime_type="image/png")
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")
