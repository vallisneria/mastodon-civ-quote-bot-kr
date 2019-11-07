# 모듈 import 부분
from mastodon import Mastodon
import random as rand
import json
from key import MASTODON_ACCESS_TOKEN


# 메인 코드 부분
Civbot = Mastodon(
    access_token=MASTODON_ACCESS_TOKEN,
    api_base_url='https://mastodon.social'
)

with open("quotes/civquotes.json", encoding="utf-8") as json_file:
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
    media = Civbot.media_post(quotes[i]["image"])
    Civbot.status_post(post, media_ids=media, visibility="unlisted")
else:
    Civbot.status_post(post, visibility="unlisted")
