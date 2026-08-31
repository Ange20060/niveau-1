import os

import psycopg2
from flask import Flask

app = Flask(__name__)

# La config de connexion vient de l'environnement, jamais en dur dans le code.
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "")


def get_connexion():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def init_base():
    """Crée la table et insère quelques données si elles n'existent pas."""
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS stagiaires "
        "(id SERIAL PRIMARY KEY, nom TEXT)"
    )
    cur.execute("SELECT COUNT(*) FROM stagiaires")
    if cur.fetchone()[0] == 0:
        cur.execute(
            "INSERT INTO stagiaires (nom) VALUES (%s), (%s), (%s)",
            ("Alice", "Karim", "Sofia"),
        )
    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def liste_stagiaires():
    conn = get_connexion()
    cur = conn.cursor()
    cur.execute("SELECT nom FROM stagiaires ORDER BY id")
    noms = [ligne[0] for ligne in cur.fetchall()]
    cur.close()
    conn.close()
    return "Stagiaires enregistrés : " + ", ".join(noms) + "\n"


if __name__ == "__main__":
    init_base()
    app.run(host="0.0.0.0", port=5000)
