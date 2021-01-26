SELECT noc 
FROM nations
ORDER BY noc;


SELECT DISTINCT athletes.athlete_name, nations.NOC
FROM nations, athletes_games, athletes
WHERE athletes.id = athletes_games.athlete_id
AND nations.id = athletes_games.nation_id
AND nations.NOC = 'KEN';
ORDER BY athlete_name


SELECT DISTINCT athletes.athlete_name, games.game_year, games.season, games.city, contests_medals.medal                                                     
FROM athletes, games, contests_medals, athletes_games 
WHERE athletes.id = athletes_games.athlete_id
AND games.id = athletes_games.game_id
AND contests_medals.medal IS NOT NULL 
AND athletes.athlete_name LIKE '%"Greg" Louganis'
ORDER BY games.game_year;
