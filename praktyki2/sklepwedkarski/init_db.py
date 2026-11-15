# --- Kod wygenerowany przez AI ---
import sqlite3
import json

DB_NAME = 'sklep.db'

produkty_startowe = [
    # ==================== WĘDKI (20 szt.) ====================
    ("Wędka Spinningowa Pro", "Lekka i wytrzymała wędka idealna na szczupaki i okonie. Wykonana z włókna węglowego.", 299.99, "Wędki", 1),
    ("Wędka Karpiowa Magnum 3.6m", "Mocna trzyczęściowa wędka karpiowa o krzywej ugięcia 3.5lbs do dalekich rzutów.", 349.00, "Wędki", 1),
    ("Wędka Feeder Master 3.9m", "Wędka gruntowa z trzema wymiennymi szczytówkami węglowymi o różnej czułości.", 279.50, "Wędki", 1),
    ("Wędka Spławikowa Tele-Float 4.2m", "Lekka teleskopowa wędka spławikowa do połowu białej ryby na jeziorach.", 149.99, "Wędki", 1),
    ("Wędka Okoniowa UltraLight 2.1m", "Niezwykle czuła wklejanka o ciężarze wyrzutu 1-7g na okonie i pstrągi.", 219.00, "Wędki", 1),
    ("Wędka Szczupakowa Predator 2.7m", "Sztywny kij spinningowy 15-45g stworzony do prowadzenia dużych woblerów i gum.", 319.00, "Wędki", 1),
    ("Wędka Sumowa Monster Cat 2.8m", "Ekstremalnie wytrzymałe wędzisko z włókna kompozytowego na największe sumy.", 420.00, "Wędki", 1),
    ("Wędka Method Feeder Pro 3.3m", "Paraboliczna wędka zaprojektowana specjalnie specjalnie do techniki Method Feeder.", 259.00, "Wędki", 1),
    ("Wędka Matchowa Distance 4.2m", "Klasyczna trzyskładowa odległościówka do łowienia spławikiem typu waggler.", 289.00, "Wędki", 1),
    ("Wędka Podlodowa Ice Hunter 60cm", "Krótka wędka zimowa z czułą szczytówką do połowu na mormyszkę i błystkę.", 49.99, "Wędki", 1),
    ("Wędka Bolonka River 5.0m", "Długa wędka z przelotkami do prowadzenia spławika w nurcie rzeki.", 235.00, "Wędki", 1),
    ("Wędka Bat Teleskopowy 6.0m", "Szybki bat bezprzelotkowy do dynamicznego połowu płoci i leszczy.", 165.00, "Wędki", 1),
    ("Wędka Sandaczowa Zander Jig 2.4m", "Bardzo szybka wędka o akcji X-Fast pozwalająca wyczuć najdelikatniejsze branie z opadu.", 389.00, "Wędki", 1),
    ("Wędka Pstrągowa Trout Stream 1.98m", "Krótki, precyzyjny spinning do łowienia w małych, zakrzaczonych rzekach.", 245.00, "Wędki", 1),
    ("Wędka Morska Baltic Pilk 2.4m", "Wędka dorszowa odporna na słoną wodę, ciężar wyrzutu do 200g.", 295.00, "Wędki", 1),
    ("Wędka Castingowa Jerkbait 1.95m", "Sztywna wędka pod multiplikator do szarpania ciężkich jerków szczupakowych.", 330.00, "Wędki", 1),
    ("Wędka Karpiowa Stalker 3.0m", "Krótka wędka karpiowa do łowienia z podchodu i wywózki pontonem.", 269.00, "Wędki", 1),
    ("Wędka Picker Light 2.7m", "Delikatna wędka z drgającą szczytówką na wody stojące i kanały.", 179.00, "Wędki", 1),
    ("Wędka Muchowa Fly Classic 2.7m", "Wędzisko muchowe w klasie AFTM #5 do suchej i mokrej muchy.", 359.00, "Wędki", 1),
    ("Wędka Turystyczna Travel Spin 2.4m", "Czteroczęściowy spinning mieszczący się w plecaku lub walizce.", 229.00, "Wędki", 1),

    # ==================== KOŁOWROTKI (20 szt.) ====================
    ("Kołowrotek Karpiowy 5000", "Niezawodny kołowrotek z wolnym biegiem, dużym nawijaniem i precyzyjnym hamulcem.", 189.50, "Kołowrotki", 1),
    ("Kołowrotek Spinningowy Pro 2500", "Lekki kołowrotek z aluminiową szpulą i 6 łożyskami kulkowymi.", 159.00, "Kołowrotki", 1),
    ("Kołowrotek Feederowy Distance 4000", "Płytka szpula typu Long Cast ułatwiająca dalekie i celne rzuty koszyczkiem.", 215.00, "Kołowrotki", 1),
    ("Kołowrotek Okoniowy Micro 1000", "Ultralekki kołowrotek z precyzyjnym hamulcem przednim do cienkich plecionek.", 139.00, "Kołowrotki", 1),
    ("Kołowrotek Karpiowy Big Pit 8000", "Ogromny kołowrotek z przekładnią ślimakową do wywózki na dużych zbiornikach.", 349.00, "Kołowrotki", 1),
    ("Kołowrotek Spławikowy Match 3000", "Szybkie przełożenie 6.2:1 pozwalające błyskawicznie zwijać zestaw z dużej odległości.", 169.00, "Kołowrotki", 1),
    ("Kołowrotek Sumowy Heavy Duty 7000", "Wzmocniona metalowa obudowa i stalowa oś odporna na ekstremalne przeciążenia.", 399.00, "Kołowrotki", 1),
    ("Multiplikator Niskoprofilowy Cast Pro", "Multiplikator z magnetycznym hamulcem rzutowym na szczupaki i sandacze.", 289.00, "Kołowrotki", 1),
    ("Kołowrotek z Tylnym Hamulcem Classic 3000", "Uniwersalny kołowrotek spławikowo-gruntowy z szybką regulacją hamulca.", 99.00, "Kołowrotki", 1),
    ("Kołowrotek Method Feeder 4500", "Wyposażony w dwa metalowe klipsy na szpuli do zaznaczania dystansu łowienia.", 229.00, "Kołowrotki", 1),
    ("Kołowrotek Morski Saltwater 6000", "Uszczelnione łożyska odporne na korozję i działanie słonej wody morskiej.", 310.00, "Kołowrotki", 1),
    ("Kołowrotek Spinningowy Carbon 3000", "Rotor i korpus z kompozytu węglowego zapewniające niską wagę i sztywność.", 249.00, "Kołowrotki", 1),
    ("Kołowrotek Podlodowy Ice Reel", "Mały kołowrotek odporny na zamarzanie smaru w niskich temperaturach.", 55.00, "Kołowrotki", 1),
    ("Kołowrotek Muchowy Fly Alu #5/6", "Wycinany maszynowo z aluminium kołowrotek muchowy z płynnym hamulcem.", 195.00, "Kołowrotki", 1),
    ("Kołowrotek Wolny Bieg Baitrunner 4000", "Świetny wybór na sandacza z gruntu oraz mniejsze karpie i liny.", 175.00, "Kołowrotki", 1),
    ("Kołowrotek Sandaczowy Power Spin 4000", "Mocna przekładnia dostosowana do ciężkich główek jigowych.", 265.00, "Kołowrotki", 1),
    ("Kołowrotek Pstrągowy Finesse 2000", "Płynny start hamulca chroniący cienkie żyłki przed zerwaniem podczas holu.", 209.00, "Kołowrotki", 1),
    ("Multiplikator Morski Trolling 400", "Wyposażony w licznik głębokości w metrach do połowu z łodzi.", 329.00, "Kołowrotki", 1),
    ("Kołowrotek Uniwersalny Starter 2000", "Budżetowy kołowrotek z nawiniętą żyłką dla początkujących wędkarzy.", 69.00, "Kołowrotki", 1),
    ("Kołowrotek Karpiowy Camo 6000", "Wykończenie w barwach maskujących i system wolnego biegu szpuli.", 239.00, "Kołowrotki", 1),

    # ==================== PRZYNĘTY (20 szt.) ====================
    ("Zestaw Przynęt Gumowych", "Komplet 20 sztuk skutecznych twisterów i ripperów w różnych atrakcyjnych kolorach.", 45.00, "Przynęty", 1),
    ("Wobler Pływający Szczupak 10cm", "Realistyczna imitacja płoci o agresywnej pracy bocznej, schodzi do 2m.", 32.00, "Przynęty", 1),
    ("Wobler Tonący Okoń 5cm", "Drobny wobler z grzechotką na okonie, klenie i pstrągi.", 24.50, "Przynęty", 1),
    ("Błystka Obrotowa Srebrna Nr 3", "Klasyczna obrotówka z czerwonym chwościkiem na szczupaki i okonie.", 12.99, "Przynęty", 1),
    ("Wahadłówka Klasyczna Mors 22g", "Legendarna polska błystka wahadłowa o szerokiej pracy na szczupaka.", 16.50, "Przynęty", 1),
    ("Kulki Proteinowe Truskawka 1kg", "Tonące kulki karpiowe o intensywnym słodkim aromacie truskawki.", 34.99, "Przynęty", 1),
    ("Kulki Pop-Up Ananas 12mm", "Pływające jaskrawe kulki proteinowe do zestawów Chod Rig i Ronnie Rig.", 22.00, "Przynęty", 1),
    ("Pellet Haczykowy Halibut 8mm", "Tłusty pellet z otworem do szybkiego montażu na włosie, waga 500g.", 18.90, "Przynęty", 1),
    ("Zanęta Leszcz Sekret 2kg", "Słodka zanęta korzenno-piernikowa przyciągająca duże leszcze.", 19.50, "Przynęty", 1),
    ("Method Mix Krill 1kg", "Drobno mielona zanęta wysokobiałkowa idealnie klejąca się do podajnika.", 23.00, "Przynęty", 1),
    ("Jaskółka Sandaczowa 9cm (10 szt.)", "Miękkie przynęty do metody Drop Shot i łowienia w opadzie.", 21.00, "Przynęty", 1),
    ("Jerkbait Bezsterowy Slider 10cm", "Przynęta szybowcowa na płytkie, zarośnięte zatoki szczupakowe.", 42.00, "Przynęty", 1),
    ("Wobler Kleniowo-Jaziowy Smużak 3cm", "Imitacja owada pracująca tuż pod powierzchnią wody na przelewach.", 26.00, "Przynęty", 1),
    ("Ripper Szczupakowy Perła 12cm (5 szt.)", "Klasyczne kopyto z szerokim ogonem generujące silną falę hydroakustyczną.", 19.99, "Przynęty", 1),
    ("Wirujący Ogonek Spinmad 10g", "Dalekosiężna przynęta z wirującym skrzydełkiem na okonie i bolenie.", 25.00, "Przynęty", 1),
    ("Wobler Boleniowy Ukleja 7cm", "Ciężki, wąski wobler do ekspresowego prowadzenia w warkoczach rzecznych.", 31.00, "Przynęty", 1),
    ("Dumbellsy Wafters Czosnek 8mm", "Zbalansowane przynęty do Method Feeder o wyrazistym zapachu czosnku.", 21.50, "Przynęty", 1),
    ("Kukurydza Konserwowa Miód 300g", "Duże, selektywne ziarna kukurydzy w słodkiej zalewie miodowej.", 9.99, "Przynęty", 1),
    ("Liquid Booster Kałamarnica 250ml", "Gęsty zalewacz do pelletu, ziaren i zanęt nie rozpuszczający materiałów PVA.", 27.00, "Przynęty", 1),
    ("Zestaw Much Wędkarskich (12 szt.)", "Pudełeczko z ręcznie wiązanymi suchymi muchami i nimfami na pstrąga i lipienia.", 49.00, "Przynęty", 1),

    # ==================== ŻYŁKI (20 szt.) ====================
    ("Żyłka Wędkarska 0.25mm", "Wytrzymała żyłka główna o długości 150m, o małej pamięci kształtu i dużej odporności na przetarcia.", 24.99, "Żyłki", 1),
    ("Plecionka 8-splotowa Zielona 0.14mm", "Idealnie okrągła i cicha na przelotkach plecionka spinningowa 150m.", 69.00, "Żyłki", 1),
    ("Żyłka Karpiowa Camo 0.32mm 600m", "Duża szpula żyłki tonącej o podwyższonej odporności na przetarcia o zaczepy.", 54.00, "Żyłki", 1),
    ("Fluorocarbon Przyponowy 0.40mm 25m", "Niewidoczny w wodzie materiał przyponowy odporny na drobne zęby drapieżników.", 29.00, "Żyłki", 1),
    ("Żyłka Przyponowa Competition 0.12mm", "Bardzo precyzyjnie kalibrowana żyłka na przypony spławikowe i feederowe 50m.", 16.50, "Żyłki", 1),
    ("Plecionka Okoniowa Fluo 0.08mm", "Jaskrawa żółta plecionka ułatwiająca obserwację brania z opadu 135m.", 59.00, "Żyłki", 1),
    ("Żyłka Feederowa Tonąca 0.22mm 200m", "Ciemnobrązowa żyłka o niskiej rozciągliwości sygnalizująca każde skubnięcie.", 26.00, "Żyłki", 1),
    ("Plecionka Sumowa Monster 0.50mm 250m", "Ekstremalnie mocna plecionka o wytrzymałości 55kg na rekordowe okazy.", 95.00, "Żyłki", 1),
    ("Żyłka Spławikowa Match 0.18mm 150m", "Miękka żyłka szybko tonąca pod powierzchnią wody do metody odległościowej.", 21.00, "Żyłki", 1),
    ("Fluorocarbon Szczupakowy 0.70mm 10m", "Gruby fluorocarbon zastępujący stalowe stalki przy łowieniu dużych szczupaków.", 38.00, "Żyłki", 1),
    ("Plecionka Przyponowa Karpiowa 25lbs", "Miękka tonąca plecionka w kolorze mułu do wiązania przyponów włosowych 20m.", 34.00, "Żyłki", 1),
    ("Żyłka Zimowa Ice Line 0.10mm 50m", "Żyłka podlodowa zachowująca elastyczność nawet przy dużym mrozie.", 12.50, "Żyłki", 1),
    ("Plecionka 4-splotowa Szara 0.16mm 150m", "Odporna na przetarcia o kamienie i muszle plecionka na rzekę.", 44.00, "Żyłki", 1),
    ("Żyłka Spinningowa Predator 0.28mm 150m", "Niskorozciągliwa żyłka na szczupaka świetnie współpracująca z obrotówkami.", 22.90, "Żyłki", 1),
    ("Żyłka Morska Surfcasting 0.35mm 300m", "Odporna na sól morską i promienie UV żyłka do połowów z plaży.", 39.00, "Żyłki", 1),
    ("Sznur Muchowy Pływający WF5F", "Pływająca linka muchowa o profilu głowicowym ułatwiająca dalekie rzuty.", 89.00, "Żyłki", 1),
    ("Strzałówka Konusowa Shockleader 0.26-0.57mm", "Zestaw 5 odcinków żyłki strzałowej do dalekich rzutów ciężkimi zestawami.", 35.00, "Żyłki", 1),
    ("Leadcore Karpiowy z Rdzeniem Ołowianym 10m", "Ciężki materiał liderowy idealnie przylegający do dna łowiska.", 36.00, "Żyłki", 1),
    ("Żyłka Pstrągowa Red 0.20mm 150m", "Czerwona żyłka dobrze widoczna dla wędkarza nad wodą, a zanikająca w toni.", 23.50, "Żyłki", 1),
    ("Stalka Wolframowa z Krętlikiem 25cm (10 szt.)", "Wytrzymałe przypony wolframowe chroniące przed obcięciem przynęty przez szczupaka.", 15.00, "Żyłki", 1),

    # ==================== AKCESORIA (20 szt.) ====================
    ("Krzesło Wędkarskie Składane", "Wygodne, stabilne krzesło z oparciem i praktycznym uchwytem na kubek.", 120.00, "Akcesoria", 0),
    ("Podbierak Teleskopowy", "Gumowana siatka chroniąca rybę przed uszkodzeniem, łatwa w czyszczeniu i szybkoschnąca.", 85.99, "Akcesoria", 1),
    ("Pokrowiec na Wędki 3-komorowy 150cm", "Usztywniany pokrowiec z szelkami i kieszeniami bocznymi na podpórki.", 135.00, "Akcesoria", 1),
    ("Skrzynka Wędkarska Dwupoziomowa", "Pojemna skrzynka z regulowanymi przegródkami na przynęty, spławiki i drobiazgi.", 65.00, "Akcesoria", 1),
    ("Sygnalizator Brań Elektroniczny", "Wodoodporny sygnalizator z regulacją głośności, tonu oraz czułości.", 59.00, "Akcesoria", 1),
    ("Mata Karpiowa Kołyska", "Gruba, bezpieczna dla ryb mata odhaczająca z podwyższonymi bokami.", 149.00, "Akcesoria", 1),
    ("Zestaw Haczyków z Przyponami (10 szt.)", "Gotowe zawiązane haczyki bezzadziorowe do Method Feeder z gumką na pellet.", 14.50, "Akcesoria", 1),
    ("Koszyczek Method Feeder 30g + Foremka", "Zestaw 3 podajników zanętowych wraz z elastyczną foremką do ładowania.", 29.00, "Akcesoria", 1),
    ("Zestaw Spławików Wędkarskich (5 szt.)", "Komplet czułych spławików przelotowych i stałych o wyporności od 1g do 4g.", 24.00, "Akcesoria", 1),
    ("Szczypce Wędkarskie Długie 22cm", "Stalowe szczypce do bezpiecznego odhaczania szczupaków i zaciskania tulejek.", 28.00, "Akcesoria", 1),
    ("Waga Wędkarska Cyfrowa do 50kg", "Podświetlany ekran LCD, funkcja tarowania i wbudowana miarka 1m.", 39.00, "Akcesoria", 1),
    ("Latarka Czołowa LED USB", "Mocna czołówka z białym oraz czerwonym światłem niepłoszącym ryb w nocy.", 49.00, "Akcesoria", 1),
    ("Parasol Wędkarski z Osłoną Boczną 2.5m", "Wodoodporny parasol z dopinanym bokiem chroniącym przed wiatrem i deszczem.", 189.00, "Akcesoria", 1),
    ("Podpórki Teleskopowe Aluminiowe (2 szt.)", "Regulowane widełki z gwintem pod sygnalizatory brań lub grzebień feederowy.", 32.00, "Akcesoria", 1),
    ("Siatka na Ryby Długa 3.0m", "Gęsta, szybkoschnąca siatka zawodnicza ze sztywnymi obręczami i regulacją kąta.", 99.00, "Akcesoria", 1),
    ("Pudełko Dwustronne na Woblery", "Przezroczyste pudełko z systemem odprowadzania wody chroniącym kotwiczki przed rdzą.", 34.00, "Akcesoria", 1),
    ("Główki Jigowe Zestaw 3g-15g (25 szt.)", "Komplet ostrych haków jigowych o różnej gramaturze w praktycznym pudełku.", 42.00, "Akcesoria", 1),
    ("Krętliki z Agrafką Wzmacniane (20 szt.)", "Stalowe agrafki typu Cross-Lock o wytrzymałości do 25kg.", 11.99, "Akcesoria", 1),
    ("Ciężarki Ołowiane Śruciny Zestaw 100g", "Okrągłe pudełko z naciętymi śrucinami o różnej wadze do wyważania spławika.", 16.00, "Akcesoria", 1),
    ("Okulary Polaryzacyjne Wędkarskie", "Usuwają odblaski z tafli wody, pozwalając dostrzec ryby i strukturę dna.", 79.00, "Akcesoria", 1)
]

def inicjalizuj_baze():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Tabela produktów
    cursor.execute('DROP TABLE IF EXISTS produkty')
    cursor.execute('''
        CREATE TABLE produkty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazwa TEXT NOT NULL,
            opis TEXT NOT NULL,
            cena REAL NOT NULL,
            kategoria TEXT NOT NULL,
            dostepnosc INTEGER NOT NULL DEFAULT 1
        )
    ''')

    cursor.executemany('''
        INSERT INTO produkty (nazwa, opis, cena, kategoria, dostepnosc)
        VALUES (?, ?, ?, ?, ?)
    ''', produkty_startowe)

    # 2. Tabela zarejestrowanych użytkowników
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uzytkownicy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            haslo TEXT NOT NULL,
            data_utworzenia DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 3. Tabela zapisująca każde logowanie na stronie
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logowania (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            email TEXT NOT NULL,
            data_logowania DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # 4. Tabela przechowująca złożone zamówienia z koszyka
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS zamowienia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            klient TEXT NOT NULL,
            adres TEXT NOT NULL,
            produkty_lista TEXT NOT NULL,
            suma REAL NOT NULL,
            data_zamowienia DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()

    # Aktualizacja pliku bazawedek.json
    cursor.execute('SELECT id, nazwa, opis, cena, kategoria, dostepnosc FROM produkty')
    wiersze = cursor.fetchall()
    lista_json = [
        {
            "id": w[0],
            "nazwa": w[1],
            "opis": w[2],
            "cena": w[3],
            "kategoria": w[4],
            "dostepnosc": bool(w[5])
        }
        for w in wiersze
    ]
    with open('bazawedek.json', 'w', encoding='utf-8') as f:
        json.dump(lista_json, f, ensure_ascii=False, indent=2)

    conn.close()
    print(f"Gotowe! Baza '{DB_NAME}' zaktualizowana (100 produktów, logowania, zamówienia).")

if __name__ == '__main__':
    inicjalizuj_baze()