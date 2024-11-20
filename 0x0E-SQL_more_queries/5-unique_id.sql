-- This script creates the table `unique_id` on your MySQL server.
-- unique_id description:
-- - `id` is an INT column with the default value 1 and must be unique.
-- - `name` is a VARCHAR column with a maximum length of 256 characters.
-- The database name will be passed as an argument of the mysql command.
-- If the table `unique_id` already exists, your script should not fail.

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
