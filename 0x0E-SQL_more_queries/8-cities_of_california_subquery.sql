-- lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT cities.id, cities.name FROM cities
WHERE (SELECT name FROM states WHERE id = cities.state_id) = 'California'
ORDER BY cities.id