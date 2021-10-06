from datetime import datetime
from time import *

from venmo.models import *
from venmo.qr import *
import venmo.data


def initialize_db():
    db.connect()
    db.create_tables([Users, Tickets])


def validate_transaction(t):
    return (t.amount == basic_price or t.amount == vip_price) and \
           t.status == "settled" and \
           t.payment_type == "pay"


def validate_message(t):
    message = t.note
    if len(message) == 10 and message.isdigit():
        return message
    else:
        return False


def insert_user(u, message):
    return Users.create(uid=u.id,
                        phone=message,
                        username=u.username,
                        first_name=u.first_name,
                        last_name=u.last_name,
                        tickets=1)


def insert_ticket(ticket, user):
    Tickets.create(uid=ticket.id,
                   date=datetime.utcfromtimestamp(ticket.date_completed),
                   amount=ticket.amount,
                   value=ticket.amount,
                   user=user)


def create_ticket(t, message):
    user_query = Users.get_or_none(Users.uid == t.actor.id)
    if user_query is None:
        user_query = insert_user(t.actor, message)
    else:
        new_tickets = user_query.tickets + 1
        Users.update({Users.tickets: new_tickets}).where(Users.uid == t.actor.id).execute()

    insert_ticket(t, user_query)
    sleep(1)
    generate_qr(user_query, t.id)
    send_msg(t.id, user_query.uid)


def send_msg(ticket_id, user_id):
    try:
        print("message sending")
        phonenumber = "+1" + str(Users.get_or_none(Users.uid == user_id).phone)
        twilio_client.api.account.messages.create(
            to=phonenumber,
            from_=twilio_number,
            body="only let the door staff scan this image!" + "\nticket id:\n"
                 + str(ticket_id) + "\nuser id:\n" + str(user_id),
            media_url=[venmo.data.base_qr_url + ticket_id + '.png']
        )
    except():
        print("error! message failed to send")


def update_tickets(target: Client):
    print("updating tickets")
    my_transactions = target.user.get_user_transactions(me.id)
    for t in my_transactions:
        if validate_transaction(t):
            message = validate_message(t)
            if message:
                print("message")
                if Tickets.get_or_none(Tickets.uid == t.id) is None:
                    create_ticket(t, message)


def get_ticket_scancount(ticketid):
    ticket_query = Tickets.get_or_none(Tickets.uid == ticketid)
    old_amount = ticket_query.amount
    new_amount = old_amount + 1
    Tickets.update({Tickets.amount: new_amount}).where(Tickets.uid == ticketid).execute()
    return ticket_query.amount
