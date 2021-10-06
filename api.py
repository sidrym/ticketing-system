import datetime
import json

import gspread

import venmo.data


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def get_fighters():
    print("getting fighters")
    # auth
    client = gspread.authorize(venmo.data.creds)

    # get the instance of the Spreadsheet
    sheet = client.open(venmo.data.spreadsheet_name)

    # read data in from sheets
    data = {}
    for i in range(0, 3):
        page = sheet.get_worksheet(i)
        data["Fight " + str(i + 1)] = {
            page.range('G14:G14')[0].value: str(round(float(page.range('G15:G15')[0].value), 2)) + " to 1",
            page.range('G17:G17')[0].value: str(round(float(page.range('G18:G18')[0].value), 2)) + " to 1",
        }

    page = sheet.get_worksheet(6)
    data["Fight " + str(4)] = {
        page.range('G14:G14')[0].value: str(round(float(page.range('G15:G15')[0].value), 2)) + " to 1",
        page.range('G17:G17')[0].value: str(round(float(page.range('G18:G18')[0].value), 2)) + " to 1",
    }

    page = sheet.get_worksheet(7)
    data["Fight " + str(5)] = {
        page.range('G14:G14')[0].value: str(round(float(page.range('G15:G15')[0].value), 2)) + " to 1",
        page.range('G17:G17')[0].value: str(round(float(page.range('G18:G18')[0].value), 2)) + " to 1",
    }

    with open('static/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=myconverter)

    # read data in from sheets
    page = sheet.get_worksheet(3)
    data = {}

    donation = page.range('A1:A13')
    events = page.range('B1:B13')

    for i in range(0, 13):
        data[donation[i].value] = events[i].value

    with open('static/schedule.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=myconverter)

    # read data in from sheets
    page = sheet.get_worksheet(4)
    data = {}

    donation = page.range('A1:B1')

    data[donation[0].value] = donation[1].value
    data['updated'] = datetime.datetime.now()

    with open('static/donations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=myconverter)
