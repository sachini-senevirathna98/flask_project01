from flask import Flask
from datetime import datetime
server = Flask(__name__)

@server.route("/page")
def page():
    current_time = datetime.now()
    return f"Current Time {current_time}"

server.run(debug=True)