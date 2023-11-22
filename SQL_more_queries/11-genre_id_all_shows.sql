-- Shows all tv-shows of a genre contained in the database hbtn_0d_tvshows
-- On each avaivable record, display: tv_shows.title - tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
    LEFT JOIN `tv_show_genres` AS g
    ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
