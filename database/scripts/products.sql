-- QA Script: Inventory and Product Catalog Validation

-- 1. Find boundary condition products (Out of stock)
SELECT id, name, price, stock 
FROM products 
WHERE stock = 0;

-- 2. Find low-stock products (Boundary testing for maximum quantity limits)
SELECT id, name, price, stock 
FROM products 
WHERE stock BETWEEN 1 AND 5
ORDER BY stock ASC;

-- 3. Verify category associations (Basic JOIN)
SELECT p.name AS product_name, p.price, c.name AS category_name
FROM products p
JOIN categories c ON p.category_id = c.id
ORDER BY c.name;