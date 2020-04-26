# 모듈 import 부분
from mastodon import Mastodon
import random as rand
import json
from key import MASTODON_ACCESS_TOKEN
import os
DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# 메인 코드 부분
Civbot = Mastodon(
    access_token=MASTODON_ACCESS_TOKEN,
    api_base_url='https://mastodon.social'
)

with open(DIRECTORY + "/quotes/civ5quotes.json", encoding="utf-8") as json_file:
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
    medialocation = DIRECTORY + i["image"]
    media = Civbot.media_post(medialocation)
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")

print(post)
