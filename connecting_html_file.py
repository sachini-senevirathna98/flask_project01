from flask import Flask, render_template
from datetime import datetime
server = Flask(__name__)

@server.route("/mydetail")
def show_my_details():
    current_time = datetime.now()
    return render_template("my/mydetail.html",current_time=current_time)

server.run(debug=True)