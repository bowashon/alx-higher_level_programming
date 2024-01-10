-- Lists all shows without the genre Comedy
SELECT DISTINCT title FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_shows.title NOT IN
        (SELECT title FROM tv_shows
		INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
		INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
		WHERE tv_genres.name = "Comedy")
	ORDER BY title;
