import asyncio
import datetime

from pypresence import Presence
from requests_futures.sessions import FuturesSession


def run_async():
    print("started!")
    session = FuturesSession()
    releases_json = session.get("https://api.github.com/repos/NoahOnFyre/FyUTILS/releases").result().json()
    newest_release = releases_json[0]
    for r in range(len(newest_release["assets"])):
        release_download_url = ""
        if newest_release["assets"][r]["name"] == "main.py":
            release_download_url = newest_release["assets"][r]["browser_download_url"]
            break
        else:
            release_download_url = ""
            continue
    newest_version_note = newest_release["body"]
    newest_version = newest_release["tag_name"]
    print(newest_version_note)
    print(newest_version)
    print("done!")


async def main():
    await asyncio.gather(asyncio.to_thread(run_async), asyncio.to_thread(run))


def run():
    t = datetime.datetime.now().strftime("%H:%M:%S")

    while True:
        if datetime.datetime.now().strftime("%H:%M:%S") != t:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(t)


asyncio.run(main())
