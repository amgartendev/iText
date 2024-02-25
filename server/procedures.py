from flask import Flask, jsonify
from PySide6.QtCore import QThread, Signal

app = Flask(__name__)

class FlaskServerThread(QThread):
    server_started = Signal()

    def run(self):
        app.run(port=7000, debug=True, use_reloader=False)

    @app.route("/test", methods=["GET"])
    @staticmethod
    def get_user():
        data = {"user": "John Doe", "birthdate": "12/16/2003"}
        return data, 201
