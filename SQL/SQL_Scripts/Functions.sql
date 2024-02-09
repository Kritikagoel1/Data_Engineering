select ascii("Kritika") from customer;
select length("Kritika")from customer;
select lower('KRITIKA');/*convert to lowercase*/
select replace('Microsoft sql','sql','server');
select reverse('python');
select upper('kritika');
-- math functions
select  NOW();/*get current date and time*/
select date_add('2023-12-07', INTERVAL 2 MONTH);
SELECT TIMESTAMPDIFF(YEAR, '2006-05-06', '2009-01-01');
-- Extract month 
SELECT MONTH('2008-05-22');
-- Extract day
SELECT DAY('2023-05-30');
-- Extract year
SELECT YEAR('2023-05-03');
select abs(-101);/*returns absolute value*/
select sin(1.5);/*returns angle in radians*/
select ceiling(14.01);/*returns the smallest or greater to the specified value*/
select exp(4.5);/*returns the exponencial value*/
select floor(14.75);
select log(5.4);/*return logarithmic value*/

use techshop;
select count(product_name) from products;
select distinct(price) from products;
select min(price) from products;
select max(price) from products;
select sum(price) from products;
select AVG(price) from products;

use techshop;
SELECT
    product_id,
    product_name,
    RANK() OVER (ORDER BY product_id) AS rankin
FROM products;
SELECT
    product_id,
    product_name,
    DENSE_RANK() OVER (ORDER BY product_id) AS denserank
FROM products;






