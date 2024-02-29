import psycopg2
from flask import Flask, jsonify
from PySide6.QtCore import QThread, Signal

app = Flask(__name__)

connection = psycopg2.connect(
    database="itext", user="amgarten", host="localhost", password="261199", port=5433
)


class FlaskServerThread(QThread):
    server_started = Signal()

    def run(self):
        app.run(port=7000, debug=True, use_reloader=False)

    @app.get("/api/get-user")
    @staticmethod
    def get_user(email):
        try:
            with connection:
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT * FROM func_get_account('{email}')")
                    test = cursor.fetchone()
            return test
        except Exception as error_code:
            error_code = str(error_code)
            raise Exception(error_code)
