DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska (
    Nr_ucz INTEGER PRIMARY KEY,
    Nazwisko TEXT NOT NULL,
    Imie1 TEXT NOT NULL,
    Imie2 TEXT DEFAULT ''
);

DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe (
    Nr_ucz INTEGER PRIMARY KEY,
    Dzien TEXT NOT NULL,
    Miesiac TEXT NOT NULL,
    Rok TEXT NOT NULL,
    M_urodzenia TEXT,
    Wojewodztwo TEXT,
    FOREIGN KEY (Nr_ucz) REFERENCES Nazwiska(Nr_ucz)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    Nr_ucz INTEGER PRIMARY KEY,
    Zach TEXT DEFAULT '',
    Rel_Ety INTEGER DEFAULT '',
    Jpol INTEGER DEFAULT '',
    Jang INTEGER DEFAULT '',
    Jniem INTEGER DEFAULT '',
    Mat INTEGER DEFAULT '',
    Hist INTEGER DEFAULT '',
    Geog INTEGER DEFAULT '',
    Biol INTEGER DEFAULT '',
    Fiz INTEGER DEFAULT '',
    Che INTEGER DEFAULT '',
    Tech INTEGER DEFAULT '',
    Info INTEGER DEFAULT '',
    Plas INTEGER DEFAULT '',
    PO INTEGER DEFAULT '',
    WF TEXT  '',
    FOREIGN KEY (Nr_ucz) REFERENCES Nazwiska(Nr_ucz)
);
