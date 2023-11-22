-- Show all cities of specied state in the database hbtn_0d_usa
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` IN (
    SELECT `id`
	FROM `states`
	WHERE `name` = "California"
)
ORDER BY `id`;
