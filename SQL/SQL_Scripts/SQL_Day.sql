use case_study;
select firstName, LastName from admin;
select distinct Username from admin;
commit;
INSERT INTO customer (customerid, firstname, lastname, email, phonenumber, address, username, password, registrationdate)
VALUES (12, 'John', 'Doe', 'john.doe@email.com', '1234567890', '123 Main St', 'jhndoe', 'password123', '2024-01-19');
delete from customer where customerid=11;

select customerid from customer
union 
select status from reservation;  

select * from customer
union all 
select * from admin;
select * from customer
Intersect
select * from admin;

SELECT customerid FROM customer
WHERE customerid NOT IN (SELECT adminid FROM admin);


