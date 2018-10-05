DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    id INTEGER PRIMARY KEY,
    ocena INTEGER,
    rok DATE,
    id_przedmiotu INTEGER,
    
    FOREIGN KEY (id_przedmiotu) REFERENCES przedmioty(id_przedmiotu)
);

DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    id INTEGER PRIMARY KEY,
    nazwisko TEXT,
    imie TEXT,
    adres TEXT,
    numer INTEGER,
    id_klasy TEXT
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
    id_przedmiotu INTEGER PRIMARY KEY,
    przedmiot TEXT,
    n_naucz TEXT,
    i_naucz TEXT
)
