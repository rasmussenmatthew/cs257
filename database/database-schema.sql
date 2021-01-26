CREATE TABLE athletes(
    id SERIAL,
    athlete_name text,
    sex text,
    height int,
    athlete_weight float
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

CREATE TABLE athletes_games(
    id int,
    athlete_id int,
    nation_id int,
    game_id int
);

CREATE TABLE contests_medals(
    id int,
    athletes_nations_games_id int,
    contest_id int,
    medal text
);
