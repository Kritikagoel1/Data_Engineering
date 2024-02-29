use techshop;
SELECT product_id,product_name,price,
SUM(price) OVER (PARTITION BY product_name, product_id) AS subtotal
from products;
SELECT product_id, product_name, price,Max(price) 
OVER (PARTITION BY product_id, product_name ORDER BY product_id, product_name) AS runningtotal
FROM products;
SELECT product_id, product_name, price,Min(price) 
OVER (PARTITION BY product_id, product_name ORDER BY product_id, product_name) AS runningtotal
FROM products;

SELECT product_id,product_name,price,
avg(price) OVER (PARTITION BY product_name, product_id) AS subtotal
from products;
SELECT product_id,product_name,price,
count(price) OVER (PARTITION BY product_name, product_id) AS subtotal
from products;


