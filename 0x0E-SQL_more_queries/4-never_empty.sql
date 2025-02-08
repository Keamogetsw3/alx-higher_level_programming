-- This script creates the table `id_not_null` in a MySQL database.
-- Table description:
-- - `id` is an INT column with a default value of 1.
-- - `name` is a VARCHAR column with a maximum length of 256 characters.
-- The database name is passed as an argument to the MySQL command.
-- If the table `id_not_null` already exists, the script ensures it will not fail.

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
