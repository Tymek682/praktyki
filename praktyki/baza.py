import sqlite3

conn = sqlite3.connect('sklep.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produkty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL,
    cena REAL NOT NULL,
    opis TEXT
)
''')

# Przykładowe dane testowe
dane = [
    ('Wędka spinningowa 2.4m', 189.99, 'Lekka wędka na szczupaka i okonia'),
    ('Kołowrotek z przednim hamulcem', 129.50, 'Rozmiar 3000, 5 łożysk'),
    ('Wobler tonący 7cm', 24.90, 'Przynęta szczupakowa, wzór okoń'),
    ('Żyłka wędkarska 0.25mm 150m', 15.00, 'Mocna żyłka uniwersalna'),
    ('Podbierak teleskopowy', 75.00, 'Siatka gumowana, długość 2m')
]

cursor.executemany('INSERT INTO produkty (nazwa, cena, opis) VALUES (?, ?, ?)', dane)
conn.commit()
conn.close()
print("Baza danych utworzona z przykładowymi produktami!")