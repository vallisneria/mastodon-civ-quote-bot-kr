# 모듈 import 부분
from mastodon import Mastodon
import random as rand
import json
from key import MASTODON_ACCESS_TOKEN
from dir import DIRECTORY


# 메인 코드 부분
Civbot = Mastodon(
    access_token=MASTODON_ACCESS_TOKEN,
    api_base_url='https://mastodon.social'
)

with open(DIRECTORY + "/quotes/civ5quotes.json", encoding="utf-8") as json_file:
    quotes = json.load(json_file)

i = rand.randint(0, len(quotes)-1)

if quotes[i]["author"] is None:
    post = "["+quotes[i]["name"]+"]\n" + \
        quotes[i]["quote"]+"\n#"+quotes[i]["version"]
else:
    post = "["+quotes[i]["name"]+"]\n" + \
        quotes[i]["quote"]+"\n- " + \
        quotes[i]["author"]+"\n#"+quotes[i]["version"]


if "image" in quotes[i]:
    medialocation = DIRECTORY + quotes[i]["image"]
    media = Civbot.media_post(medialocation)
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")

print(post)
