****QR Ticketing system + live stats****


Welcome! This was created in a few days to help my friend with an amateur MMA event he put on for charity.


This repository serves two functions:
 - displays realtime schedule and fight information from google drive on the website
 - automatic ticketing system for staff

The ticketing system scrapes a Venmo account for payments of desired amount. For each transaction, it generates a QR ticket which it sends to the number of the customer. Then, door staff can scan the QR code to be taken to an endpoint to validate the ticket.


instructions for running:
- insert google sheets json api key
- populate data.py file with access tokens
- `pip install qrcode, venmo_api, pillow, peewee, sanic, twilio, oauth2client, gspread`
- `./main.py` and you're off!
