CREATE TABLE athletes(
    id SERIAL,
    name text,
    sex text,
    age int,
    height int,
    weight int
);

CREATE TABLE nations(
    id SERIAL,
    NOC text,
    team text
);

CREATE TABLE games(
    id SERIAL,
    game_year int,
    season text,
    city text
);

CREATE TABLE contest(
    id SERIAL,
    contest text,
    sport text
);

CREATE TABLE medals(
    id SERIAL,
    medal text,
    game_id int,
    contest_id int
);

CREATE TABLE contests_athletes(
    contest_id int,
    athlete_id int
);

CREATE TABLE medals_athletes(
    medal_id int,
    athlete_id int
);

CREATE TABLE athletes_nations(
    athelte_id int;
    nation_id int
);

CREATE TABLE athletes_games(
    athletes int,
    games int
);