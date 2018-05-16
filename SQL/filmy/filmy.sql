CREATE TABLE tbFilmy (
	id INTEGER PRIMARY KEY,
	name TEXT,
	genre TEXT,
    year INTEGER,
	imdb_rating NUMERIC
);

INSERT INTO tbFilmy(id, name, genre, year, imdb_rating) VALUES (1, 'Avatar', 'action', 2009, 7.9);
