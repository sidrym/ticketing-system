import asyncio

from sanic import Sanic, json, response
import venmo.data

import api
from venmo.db import get_ticket_scancount, update_tickets

app = Sanic("http")
app.config.SERVER_NAME = "MDMMA"


@app.get("/ticket/<ticket:str>")
async def handler(ticket: str):
    return json({"ticket_scans": get_ticket_scancount(ticket)})


@app.get("/qr/<ticket:str>")
async def handler(ticket: str):
    return await response.file('static/qr/' + ticket)


@app.get("/")
async def handler():
    return await response.file(dist_directory + "/index.html")


dist_directory = './static'
app.static('/', dist_directory)


async def ticket_refresh():
    while True:
        await asyncio.sleep(10)
        update_tickets(target=venmo.data.venmo_client)


async def stats_refresh():
    while True:
        await asyncio.sleep(30)
        api.get_fighters()

