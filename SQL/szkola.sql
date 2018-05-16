DROP TABLE IF EXISTS tbUczniowie;
/**/

CREATE TABLE tbUczniowie
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		/* INTEGER- typ danych (liczby całkowite); PRIMARY KEY- klucz główny; AUTOINCREMENT- autonumeracja wzrastająca kolejno o jeden*/
		imie TEXT,
		nazwisko TEXT,
		plec INTEGER,
		/* BOOLEAN- wartość typu prawda-fałsz*/
		id_klasa INTEGER,
		egzHum NUMERIC NOT NULL DEFAULT 0,
		/* NUMERIC i REAL- typ danych (liczby dziesiętne); NOT NULL- wynik nie może być wartością nieoznaczoną; 0 można zamienić '' np. na pusty ciąg znak*/
		egzMat NUMERIC NOT NULL DEFAULT 0,
		egzJez NUMERIC NOT NULL DEFAULT 0,
		FOREIGN KEY (id_klasa) REFERENCES tbKlasy(id)	/* FOREIGN KEY- klucz obcy, REFERENCES- powiązania*/

	);

DROP TABLE IF EXISTS tbKlasy;

	CREATE TABLE tbKlasy
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		klasa TEXT,
		rokNaboru INTEGER,
		rokMatury INTEGER
	);

	INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1A', 2017, 2020);
	INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '1B', 2017, 2020);
	INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL, '2A', 2016, 2019);
	/* INSERT INTO- dodawanie danych do tabeli*/

	INSERT INTO tbUczniowie VALUES (NULL, 'Leszek', 'Gajewski', 0, 2, 8, 5, 7.8);
	INSERT INTO tbUczniowie VALUES (NULL, 'Jakub', 'Gagat', 1, 1, 88, 79, 94);

UPDATE tbUczniowie SET egzJez = 100 WHERE id = 1;