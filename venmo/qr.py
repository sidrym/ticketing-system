import qrcode
from PIL import ImageDraw

from venmo.data import *
from venmo.models import Users
from venmo.models import Tickets


def generate_qr(target_user, target_ticket):
    url = base_ticket_url + target_ticket

    # update target user tickets
    target_user = Users.get_or_none(Users.uid == target_user.uid)
    message = target_user.first_name + ' ' \
              + target_user.last_name + \
              ', ticket ' + str(target_user.tickets)

    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    code.add_data(url)
    code.make()

    newcolor = Tickets.get_or_none(Tickets.uid == target_ticket)
    if newcolor.value == vip_price:
        color = 'Gold'
    else:
        color = 'White'

    img = code.make_image(
        fill_color=color, back_color="black").convert('RGB')

    draw = ImageDraw.Draw(img)
    draw.text((40, 5), message, (255, 255, 255), font=font)
    img.save('static/qr/' + target_ticket + '.png')
