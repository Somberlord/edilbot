#!/usr/bin/env python

PASSWORD_APP = "fjSP wsdm iaPX kVNk MMUS r1vV"
URL = "https://test-wp.murlock.org/wp-json/tribe/events/v1/events"

import aiohttp
import asyncio
import json



async def main():
    auth = aiohttp.BasicAuth(login="murlock", password=PASSWORD_APP)
    data = {
        "title": "Permanence",
        "start_date": "2024-02-18 09:00",
        "end_date": "2024-02-18 10:00",
        "timezeone": "Europe/Paris",
        "excerpt": "Découverte Voidfall EXC",
        "description": "Découverte Voidfall DESC",
        # "id": 1 l'auteur de créa
    }
    async with aiohttp.ClientSession(auth=auth) as session:

        async with session.post(URL, data=data) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html)
            data = json.loads(html)
            print(json.dumps(data, indent=2))




asyncio.run(main())