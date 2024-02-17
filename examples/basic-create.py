#!/usr/bin/env python

import aiohttp
import asyncio
import json
import configparser


URL = "https://test-wp.murlock.org/wp-json/tribe/events/v1/events"


async def main():
    config = configparser.ConfigParser()
    config.read("config.ini")

    auth = aiohttp.BasicAuth(
        login=config.get("wordpress", "login"),
        password=config.get("wordpress", "password_app")
    )

    data = {
        "title": "Permanence",
        "start_date": "2024-02-18 12:00",
        "end_date": "2024-02-18 15:00",
        "timezeone": "Europe/Paris",
        "excerpt": "Découverte Voidfall",
        "description": "Découverte Voidfall",
        # "id": 1 l'auteur, par défaut le user de l'application
    }
    async with aiohttp.ClientSession(auth=auth) as session:

        async with session.post(URL, data=data) as response:
            print("Status:", response.status)
            html = await response.text()
            data = json.loads(html)
            print(json.dumps(data, indent=2))
            # id should be saved to be able to delete / edit event

# example of output
"""
{
  "id": 10,
  "global_id": "test-wp.murlock.org?id=10",
  "global_id_lineage": [
    "test-wp.murlock.org?id=10"
  ],
  "author": "1",
  "status": "publish",
  "date": "2024-02-17 15:34:40",
  "date_utc": "2024-02-17 14:34:40",
  "modified": "2024-02-17 15:34:40",
  "modified_utc": "2024-02-17 14:34:40",
  "url": "https://test-wp.murlock.org/event/permanence/",
  "rest_url": "https://test-wp.murlock.org/wp-json/tribe/events/v1/events/10",
  "title": "Permanence",
  "description": "<p>D\u00e9couverte Voidfall DESC</p>",
  "excerpt": "<p>D\u00e9couverte Voidfall EXC</p>",
  "slug": "permanence",
  "image": false,
  "all_day": false,
  "start_date": "2024-02-18 09:00:00",
  "start_date_details": {
    "year": "2024",
    "month": "02",
    "day": "18",
    "hour": "09",
    "minutes": "00",
    "seconds": "00"
  },
  "end_date": "2024-02-18 10:00:00",
  "end_date_details": {
    "year": "2024",
    "month": "02",
    "day": "18",
    "hour": "10",
    "minutes": "00",
    "seconds": "00"
  },
  "utc_start_date": "2024-02-18 08:00:00",
  "utc_start_date_details": {
    "year": "2024",
    "month": "02",
    "day": "18",
    "hour": "08",
    "minutes": "00",
    "seconds": "00"
  },
  "utc_end_date": "2024-02-18 09:00:00",
  "utc_end_date_details": {
    "year": "2024",
    "month": "02",
    "day": "18",
    "hour": "09",
    "minutes": "00",
    "seconds": "00"
  },
  "timezone": "Europe/Paris",
  "timezone_abbr": "CET",
  "cost": "",
  "cost_details": {
    "currency_symbol": "",
    "currency_code": "",
    "currency_position": "",
    "values": []
  },
  "website": "https://test-wp.murlock.org/event/permanence/",
  "show_map": false,
  "show_map_link": false,
  "hide_from_listings": false,
  "sticky": false,
  "featured": false,
  "categories": [],
  "tags": [],
  "venue": [],
  "organizer": []
}
"""



asyncio.run(main())
