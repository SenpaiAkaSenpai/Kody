DROP TABLE IF EXISTS miasta;
CREATE TABLE miasta (
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    Nazwa_miasta TEXT (30),
    Wojewodztwo TEXT (20)
);

DROP TABLE IF EXISTS powierzchnie;
CREATE TABLE powierzchnie (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Powierzchnia_miasta DECIMAL,
    Powierzchnia_terenow_zielonych DECIMAL,
    Data_aktualizacji DATE,
    FOREIGN KEY (id) REFERENCES miasta(id_miasta)
    );

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Liczba_mieszkancow INTEGER,
    Liczba_kobiet INTEGER
    Liczba_meszczyzn INTEGER,
    Grupa_wiekowa TEXT (20),
    Data_aktualizacji DATE,
    FOREIGN KEY (id) REFERENCES miasta(id_miasta)
);


/*sqlpedia.pl*/
