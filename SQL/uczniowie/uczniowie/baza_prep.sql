DROP TABLE IF EXISTS;
CREATE TABLE uczniowie:(
id INT PRIMARY KEY AUTOINCREMENT, 
imie TEXT,
nazwisko TEXT,
plec BOOLEAN,
id_klasa INT NOT NULL,
egz_hum NUMERIC NOT NULL DEFAULT 0,
egz_mat NUMERIC NOT NULL DEFAULT 0,
Iegz_jez NUMERIC NOT NULL DEFAULT 0,
FOREIGN KEY (id_klasa) REFERENCES klasy(id)
);

DROP TABLE IF EXISTS;
CREATE TABLE klasy:(
id INTEGER PRIMARY KEY AUTOINCREMENT,
klasa TEXT(2),
rok_naboru INT,
rok_matury INT,
FOREIGN KEY (id) REFERENCES uczniowie(id)
);

DROP TABLE IF EXISTS;
CREATE TABLE przedmioty:(
it INTEGER PRIMARY KEY AUTOINCREMENT,
przedmiot TEXT,
imie_naucz TEXT,
nazwisko_naucz TEXT,
plec_naucz BOOLEAN,
);

DROP TABLE IF EXISTS;
CREATE TABLE oceny:(
FOREIGN KEY (id) REFERENCES uczniowie(id),
datad DATA,
id_uczen INTEGER NOT NULL,
id_przedmiot INTEGER NOT NULL,
ocena INT,
FOREIGN KEY (id_uczen) REFERENCES uczniowie(id),
FOREIGN KEY (id_przedmiot) REFERENCES przedmioty(id)
)
