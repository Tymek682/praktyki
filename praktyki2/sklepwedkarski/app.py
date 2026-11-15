# --- Kod wygenerowany przez AI ---
from flask import Flask, request, jsonify, render_template, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'tajny_klucz_zloty_haczyk_admin'
DB_NAME = 'sklep.db'

def polacz_baze():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ==================== PODSTRONY SKLEPU ====================
@app.route('/')
def strona_glowna():
    return render_template('index.html', wybrana_kategoria='Wszystkie', widok='produkty')

@app.route('/wedki')
def podstrona_wedki():
    return render_template('index.html', wybrana_kategoria='Wędki', widok='produkty')

@app.route('/kolowrotki')
def podstrona_kolowrotki():
    return render_template('index.html', wybrana_kategoria='Kołowrotki', widok='produkty')

@app.route('/przynety')
def podstrona_przynety():
    return render_template('index.html', wybrana_kategoria='Przynęty', widok='produkty')

@app.route('/zylki')
def podstrona_zylki():
    return render_template('index.html', wybrana_kategoria='Żyłki', widok='produkty')

@app.route('/akcesoria')
def podstrona_akcesoria():
    return render_template('index.html', wybrana_kategoria='Akcesoria', widok='produkty')

@app.route('/koszyk')
def podstrona_koszyk():
    return render_template('index.html', wybrana_kategoria='Koszyk', widok='koszyk')

@app.route('/logowanie')
def podstrona_logowanie():
    return render_template('index.html', wybrana_kategoria='Logowanie', widok='logowanie')

# ==================== PODSTRONY ZE STOPKI ====================
@app.route('/regulamin')
def podstrona_regulamin():
    return render_template('index.html', wybrana_kategoria='Regulamin', widok='regulamin')

@app.route('/kontakt')
def podstrona_kontakt():
    return render_template('index.html', wybrana_kategoria='Kontakt', widok='kontakt')

@app.route('/reklamacje')
def podstrona_reklamacje():
    return render_template('index.html', wybrana_kategoria='Reklamacje', widok='reklamacje')

@app.route('/admin')
def podstrona_admin():
    czy_zalogowany = session.get('admin_zalogowany', False)
    return render_template('index.html', wybrana_kategoria='Admin', widok='admin', admin_zalogowany=czy_zalogowany)

# ==================== API: AUTORYZACJA ADMINA (tymek / alan) ====================
@app.route('/api/admin/login', methods=['POST'])
def api_admin_login():
    dane = request.get_json()
    login = dane.get('login', '').strip()
    haslo = dane.get('haslo', '').strip()

    if login == 'tymek' and haslo == 'alan':
        session['admin_zalogowany'] = True
        return jsonify({"sukces": True, "komunikat": "Zalogowano do Panelu Administratora!"})
    return jsonify({"sukces": False, "komunikat": "Nieprawidłowy login lub hasło administratora!"}), 401

@app.route('/api/admin/logout', methods=['POST'])
def api_admin_logout():
    session.pop('admin_zalogowany', None)
    return jsonify({"sukces": True, "komunikat": "Wylogowano z panelu administratora."})

@app.route('/api/admin/klienci', methods=['GET'])
def api_admin_klienci():
    if not session.get('admin_zalogowany'):
        return jsonify({"blad": "Brak dostępu"}), 403

    conn = polacz_baze()
    uzytkownicy = conn.execute(
        "SELECT id, login, email, data_utworzenia FROM uzytkownicy ORDER BY id DESC"
    ).fetchall()
    logowania = conn.execute(
        "SELECT id, login, email, data_logowania FROM logowania ORDER BY id DESC LIMIT 50"
    ).fetchall()
    conn.close()

    return jsonify({
        "uzytkownicy": [dict(u) for u in uzytkownicy],
        "logowania": [dict(l) for l in logowania]
    })

# ==================== API: PRODUKTY (GET, POST, PUT, DELETE) ====================
@app.route('/api/produkty', methods=['GET'])
def api_pobierz_produkty():
    kategoria = request.args.get('kategoria', '').strip()
    nazwa = request.args.get('nazwa', '').strip()
    cena_max = request.args.get('cena_max', '').strip()

    zapytanie = "SELECT id, nazwa, opis, cena, kategoria, dostepnosc FROM produkty WHERE 1=1"
    parametry = []

    if kategoria and kategoria != 'Wszystkie':
        zapytanie += " AND kategoria = ?"
        parametry.append(kategoria)

    if nazwa:
        zapytanie += " AND LOWER(nazwa) LIKE LOWER(?)"
        parametry.append(f"%{nazwa}%")

    if cena_max:
        try:
            zapytanie += " AND cena <= ?"
            parametry.append(float(cena_max))
        except ValueError:
            pass

    zapytanie += " ORDER BY id DESC"

    conn = polacz_baze()
    wiersze = conn.execute(zapytanie, parametry).fetchall()
    conn.close()

    return jsonify([dict(w) for w in wiersze])

@app.route('/api/produkty', methods=['POST'])
def api_dodaj_produkt():
    dane = request.get_json()
    nazwa = dane.get('nazwa', '').strip()
    opis = dane.get('opis', '').strip()
    kategoria = dane.get('kategoria', 'Wędki').strip()
    cena = dane.get('cena', 0)

    if not nazwa or not opis or not cena or float(cena) <= 0:
        return jsonify({"sukces": False, "komunikat": "Podaj poprawną nazwę, opis oraz cenę!"}), 400

    conn = polacz_baze()
    conn.execute(
        "INSERT INTO produkty (nazwa, opis, cena, kategoria, dostepnosc) VALUES (?, ?, ?, ?, 1)",
        (nazwa, opis, float(cena), kategoria)
    )
    conn.commit()
    conn.close()
    return jsonify({"sukces": True, "komunikat": f"Dodano produkt: {nazwa}"})

@app.route('/api/produkty/<int:produkt_id>', methods=['PUT'])
def api_edytuj_produkt(produkt_id):
    dane = request.get_json()
    nowa_cena = float(dane.get('cena', 0))
    nowa_dostepnosc = 1 if dane.get('dostepnosc') else 0

    conn = polacz_baze()
    conn.execute(
        "UPDATE produkty SET cena = ?, dostepnosc = ? WHERE id = ?",
        (nowa_cena, nowa_dostepnosc, produkt_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"sukces": True, "komunikat": "Zaktualizowano produkt."})

@app.route('/api/produkty/<int:produkt_id>', methods=['DELETE'])
def api_usun_produkt(produkt_id):
    conn = polacz_baze()
    conn.execute("DELETE FROM produkty WHERE id = ?", (produkt_id,))
    conn.commit()
    conn.close()
    return jsonify({"sukces": True, "komunikat": "Usunięto produkt z bazy."})

# ==================== API: KOSZYK I ZAMÓWIENIA ====================
@app.route('/api/zamowienia', methods=['POST'])
def api_zloz_zamowienie():
    dane = request.get_json()
    klient = dane.get('klient', '').strip()
    adres = dane.get('adres', '').strip()
    produkty_lista = dane.get('produkty_lista', '').strip()
    suma = float(dane.get('suma', 0))

    if not klient or not adres or not produkty_lista:
        return jsonify({"sukces": False, "komunikat": "Wypełnij dane dostawy i dodaj produkty do koszyka!"}), 400

    conn = polacz_baze()
    conn.execute(
        "INSERT INTO zamowienia (klient, adres, produkty_lista, suma) VALUES (?, ?, ?, ?)",
        (klient, adres, produkty_lista, suma)
    )
    conn.commit()
    conn.close()
    return jsonify({"sukces": True, "komunikat": "Zamówienie zostało złożone i zapisane w bazie!"})

@app.route('/api/zamowienia', methods=['GET'])
def api_pobierz_zamowienia():
    conn = polacz_baze()
    wiersze = conn.execute(
        "SELECT id, klient, adres, produkty_lista, suma, data_zamowienia FROM zamowienia ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return jsonify([dict(w) for w in wiersze])

# ==================== API: LOGOWANIE KLIENTÓW ====================
@app.route('/api/zaloguj', methods=['POST'])
def api_zaloguj():
    dane = request.get_json()
    login = dane.get('login', '').strip()
    email = dane.get('email', '').strip()
    haslo = dane.get('haslo', '').strip()

    if not login or not email or not haslo:
        return jsonify({"sukces": False, "komunikat": "Wypełnij wszystkie pola!"}), 400

    conn = polacz_baze()
    cursor = conn.cursor()
    uzytkownik = cursor.execute("SELECT * FROM uzytkownicy WHERE login = ?", (login,)).fetchone()

    if uzytkownik:
        if uzytkownik['haslo'] != haslo:
            conn.close()
            return jsonify({"sukces": False, "komunikat": "Błędne hasło dla tego loginu!"}), 401
    else:
        cursor.execute(
            "INSERT INTO uzytkownicy (login, email, haslo) VALUES (?, ?, ?)",
            (login, email, haslo)
        )

    cursor.execute("INSERT INTO logowania (login, email) VALUES (?, ?)", (login, email))
    conn.commit()
    conn.close()

    return jsonify({"sukces": True, "komunikat": f"Witaj {login}! Twoje logowanie zostało zapisane."})

if __name__ == '__main__':
    app.run(debug=True)