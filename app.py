from flask import Flask
import mysql.connector
from base import host, user, password, database
app = Flask(__name__)

@app.route("/")
def home():
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM usuarios")
    resultados = cursor.fetchall()

    lista = [r[0] for r in resultados]

    return "<h1>Usuarios:</h1>" + "<br>".join(lista)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
