DROP TABLE IF EXISTS zamowienia;
CREATE TABLE zamowienia (
    id_zam INTEGER PRIMARY KEY AUTOINCREMENT,
    elem_zam TEXT (40),
    ilosc INTEGER
);

DROP TABLE IF EXISTS klient;
CREATE TABLE klient (
    id_kl INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_kl TEXT (20),
    adres DECIMAL (40),
    kod_pocztowy TEXT (6),
    FOREIGN KEY (id_kl) REFERENCES zamowienia(id_zam)
    );

DROP TABLE IF EXISTS ;
CREATE TABLE  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Liczba_mieszkancow INTEGER,
    Liczba_kobiet INTEGER
    Liczba_meszczyzn INTEGER,
    Grupa_wiekowa TEXT (20),
    Data_aktualizacji DATE,
    FOREIGN KEY (id) REFERENCES miasta(id_miasta)
);


/*sqlpedia.pl*/
