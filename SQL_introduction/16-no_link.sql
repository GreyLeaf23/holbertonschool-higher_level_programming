-- Shows all records in the 'second_table' that it doesn't have an empty name.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
