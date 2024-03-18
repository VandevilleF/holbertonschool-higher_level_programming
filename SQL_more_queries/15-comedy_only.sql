-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = show_id
INNER JOIN tv_genres
ON tv_genres.id = genre_id
WHERE name = "Comedy"
ORDER by title ASC;
