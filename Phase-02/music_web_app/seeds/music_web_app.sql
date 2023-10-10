DROP TABLE IF EXISTS artists CASCADE;
DROP SEQUENCE IF EXISTS artists_id_seq;

DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;


CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre varchar(300)
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title varchar(300),
    release_year int,
    artist_id int,
    constraint fk_artist foreign key(artist_id) references artists(id) on delete cascade
);

INSERT INTO artists (name, genre) VALUES ('artist1', 'genre1');
INSERT INTO artists (name, genre) VALUES ('artist2', 'genre2');
INSERT INTO artists (name, genre) VALUES ('artist3', 'genre3');

INSERT INTO albums (title, release_year, artist_id) VALUES ('title1', 2023, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('title2', 2023, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('title3', 2023, 3);