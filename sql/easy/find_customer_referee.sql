-- Table: Customer
-- id: int (primary key)
-- name: varchar
-- referee_id: int
--
-- Find customers not referred by customer with id = 2, or not referred by anyone.

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;

-- Follow-up: Why is IS NULL needed?
-- In SQL, any comparison with NULL (including != 2) returns NULL, not TRUE.
-- So rows where referee_id IS NULL would be excluded without the explicit IS NULL check.
