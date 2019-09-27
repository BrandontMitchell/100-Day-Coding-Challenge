/* Query 1 */

SELECT DISTINCT language
FROM languages
WHERE official='T'
ORDER BY language DESC;

/* Query 2 */

SELECT name
FROM countries
WHERE name LIKE '%Republic%';

/* Query 3 */

SELECT name
FROM countries
WHERE continent != 'Africa';

/* Query 4 */

SELECT name, gnp
FROM countries
WHERE gnp BETWEEN 10000 AND 50000;

/* Query 5 */

SELECT name, population, surface_area,
   population / surface_area as population_density
FROM countries
ORDER BY population_density DESC;
