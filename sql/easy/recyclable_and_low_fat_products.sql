-- Table: Products
-- product_id: int (primary key)
-- low_fats: ENUM('Y', 'N')
-- recyclable: ENUM('Y', 'N')
--
-- Find the ids of products that are both low fat and recyclable.

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Performance notes:
-- ENUM columns are stored as integers internally, making comparisons faster than VARCHAR.
-- Indexes on low_fats/recyclable could help at scale, but low cardinality means
-- the optimizer may prefer a full table scan regardless.
