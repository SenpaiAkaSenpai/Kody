DROP TABLE IF EXISTS filmy,
CREATE TABLE tbFilmy (
	id INTEGER PRIMARY KEY,
	name TEXT NOT NULL,
	genre TEXT DEFAULT '',
    year INTEGER,
	imdb_rating DECIMAL
);

INSERT INTO tbFilmy(id, name, genre, year, imdb_rating) VALUES (1, 'Avatar', 'action', 2009, 7.9);
