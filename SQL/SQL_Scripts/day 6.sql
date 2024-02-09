use techshop;
select customer_id from customer union select product_id from products;
SELECT customer_id FROM customer
WHERE customer_id NOT IN (SELECT product_id FROM products);
select customer_id from customer intersect select product_id from products;

SELECT * FROM customer WHERE last_name LIKE '%e';

SELECT * FROM customer WHERE last_name REGEXP '^Sm';

SELECT * FROM customer WHERE REGEXP_LIKE(last_name, '^Sm');

SELECT REGEXP_REPLACE('Hello World', 'World', 'Universe');

SELECT REGEXP_SUBSTR('John Doe', '[A-Z][a-z]+') AS first_name;
