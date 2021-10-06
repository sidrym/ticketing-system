from server import app, ticket_refresh, stats_refresh
from venmo.db import initialize_db

if __name__ == '__main__':
    initialize_db()
    app.add_task(ticket_refresh())
    app.add_task(stats_refresh())
    app.run(host='0.0.0.0', port=80)
