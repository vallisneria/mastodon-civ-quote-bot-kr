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

with open("./quotes/civ5quotes.json", encoding="utf-8") as json_file:
    quotes = json.load(json_file)

i = rand.choice(quotes)

if i["author"] is None:
    post = "["+i["name"]+"]\n" + \
        i["quote"]+"\n#"+i["version"]
else:
    post = "["+i["name"]+"]\n" + \
        i["quote"]+"\n- " + \
        i["author"]+"\n#"+i["version"]


if "image" in i:
    medialocation = "." + i["image"]
    media = Civbot.media_post(medialocation)
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")

print(post)
