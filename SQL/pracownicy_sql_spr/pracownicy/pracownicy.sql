DROP TABLE IF EXISTS kontakty;
CREATE TABLE kontakty (
    id_p INTEGER PRIMARY KEY,
    typ_k INT,
    kontakt TEXT,
    uwagi TEXT
);

DROP TABLE IF EXISTS place;
CREATE TABLE place (
    id_p INTEGER,
    id_s INTEGER,
    placa INTEGER,
    data_z TEXT,

    FOREIGN KEY (id_s) REFERENCES stanowiska(id_s),
    FOREIGN KEY (id_p) REFERENCES kontakty(id_p)
);

DROP TABLE IF EXISTS pracownicy;
CREATE TABLE pracownicy (
    id_p INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT,
    nazwisko TEXT,
    kod TEXT,
    miasto_z TEXT,
    ulica TEXT,
    data_u TEXT,
    miasto_u TEXT,
   
    FOREIGN KEY (id_p) REFERENCES kontakty(id_p)
);

DROP TABLE IF EXISTS stanowiska;
CREATE TABLE stanowiska (
    id_s INTEGER PRIMARY KEY AUTOINCREMENT,
    stanowisko TEXT
);
