use case_study;
select c.FirstName,c.LastName from customer as c
inner join reservation r on r.customerID=c.customerID
where r.status="completed";

select * from customer as c
left join reservation r on r.customerID =c.customerID;

select * from customer as c
right join reservation r on r.customerID =c.customerID;

SELECT *
FROM customer AS c
NATURAL JOIN reservation AS r;

SELECT c.*, COUNT(r.reservationID) AS reservation_count
FROM customer AS c
LEFT JOIN reservation r ON r.customerID = c.customerID
GROUP BY c.customerID;

SELECT c.*, COUNT(r.reservationID) AS reservation_count
FROM customer AS c
LEFT JOIN reservation r ON r.customerID = c.customerID
GROUP BY c.customerID
HAVING reservation_count > 1;

/*Non equijoin*/
SELECT *
FROM customer AS c
JOIN reservation AS r ON c.customerID <> r.customerID;

use case_study;
select * from customer as c
right join reservation r on r.customerID =c.customerID
order by c.customerID desc;

-- cross join
select * from customer as c
cross join reservation r on r.customerID =c.customerID;

USE techshop;

SELECT p.product_name, SUM(p.price) AS total_price
FROM products AS p
JOIN inventory i ON i.product_id = p.product_id
GROUP BY p.product_name;



