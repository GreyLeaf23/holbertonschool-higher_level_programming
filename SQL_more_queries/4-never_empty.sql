-- Creates a table in MySQL server that can't be empty.
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
);
