-- lists all genres from hbtn_0d_tvshows and displays number of shows
SELECT tv_show_genres.genre AS genre, COUNT(tv_show_genres.tv_show_id) AS n
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY tv_show_genres.genre
ORDER BY n DESC;
