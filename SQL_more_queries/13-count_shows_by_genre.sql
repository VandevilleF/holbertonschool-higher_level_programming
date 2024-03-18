-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT name AS genre, count(show_id) AS number_of_shows
FROM tv_show_genres
LEFT JOIN tv_genres
ON genre_id = id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
