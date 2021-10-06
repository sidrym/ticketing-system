import twilio.rest as twclient
from PIL import ImageFont
from oauth2client.service_account import ServiceAccountCredentials
from venmo_api import Client

# ticket price configuration
basic_price = 10.50
vip_price = 15.50

# venmo authentication
# access_token =
# venmo_client = Client(access_token=access_token)
# me = venmo_client.user.get_my_profile()

# twilio authentication
# twilio_auth =
# twilio_sid =
# twilio_number =
# twilio_client = twclient.Client(twilio_sid, twilio_auth)

# google drive authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('JSON-GOES-HERE.json', scope)
# spreadsheet_name =

# qrcode configuration
basewidth = 100
QRcolor = 'White'
font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
# base_ticket_url =
# base_qr_url =
