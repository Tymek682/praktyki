from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = 'sklep.db'

def pobierz_polaczenie():
    conn = sqlite3.connect(DB_NAME)
    # Row pozwala odwoływać się do kolumn po nazwach (np. produkt['nazwa'])
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint API zwracający przefiltrowane produkty
@app.route('/api/produkty', methods=['GET'])
def filtruj_produkty():
    nazwa = request.args.get('nazwa', '').strip()
    cena_max = request.args.get('cena_max', '').strip()

    zapytanie = "SELECT id, nazwa, cena, opis FROM produkty WHERE 1=1"
    wartosci = []

    # Filtracja po fragmencie nazwy (niezależnie od wielkości liter)
    if nazwa:
        zapytanie += " AND nazwa LIKE ?"
        wartosci.append(f"%{nazwa}%")

    # Filtracja po maksymalnej cenie
    if cena_max:
        try:
            zapytanie += " AND cena <= ?"
            wartosci.append(float(cena_max))
        except ValueError:
            pass  # Jeśli ktoś wpisał litery zamiast cyfr, ignorujemy ten filtr

    conn = pobierz_polaczenie()
    kursor = conn.cursor()
    kursor.execute(zapytanie, wartosci)
    wiersze = kursor.fetchall()
    conn.close()

    # Przekształcamy wyniki do zwykłej listy słowników
    produkty = [dict(wiersz) for wiersz in wiersze]
    return jsonify(produkty)

@app.route('/')
def strona_glowna():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)