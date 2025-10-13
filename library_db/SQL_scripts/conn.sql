SELECT title, authorid
FROM books
WHERE EXTRACT(YEAR FROM dateofpublication) > 2015;
