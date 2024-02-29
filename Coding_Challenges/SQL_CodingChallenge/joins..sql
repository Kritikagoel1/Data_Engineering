use techshop;
-- Natural Join
select * from products as p
natural join inventory as i;
-- self join or equi join
SELECT p.product_name, SUM(p.price) AS total_price
FROM products AS p
JOIN inventory i ON i.product_id = p.product_id
GROUP BY p.product_name;
-- left join
select o.Order_status,p.product_id from orders o
left join products p on p.product_id=o.product_id
order by p.product_id desc;
-- right join
select o.order_status,p.product_name,sum(p.price) as total  from orders o 
right join products p on p.product_id=o.product_id
group by p.product_name,o.order_status
having (total>300);
-- inner join
select o.order_id,count(p.product_name)as cp from products p 
inner join orders o on o.product_id=p.product_id
group by p.product_name,o.order_id
having cp>0;
-- non equi join
select p.product_name,o.order_date,p.purchase_date from products p
join orders o on o.order_date>p.purchase_date; 
-- cross join
select o.order_status, p.product_id from orders o
cross join products p on p.product_id=o.product_id;
-- full outer join
SELECT * FROM products
left  OUTER JOIN orders ON products.product_id = orders.product_id
UNION
SELECT * FROM products
RIGHT OUTER JOIN orders ON orders.product_id = products.product_id;

