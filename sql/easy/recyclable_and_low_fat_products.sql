-- Table: Products
-- product_id: int (primary key)
-- low_fats: ENUM('Y', 'N')
-- recyclable: ENUM('Y', 'N')
--
-- Find the ids of products that are both low fat and recyclable.

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
