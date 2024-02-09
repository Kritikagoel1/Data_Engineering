use case_study;
SELECT c.*
FROM customer AS c
WHERE EXISTS ( SELECT *
    FROM reservation r
    WHERE r.customerID = c.customerID);
    
    
    
use techshop;
select product_name from products where product_id = ALL(select product_id 
from inventory where quantity_in_stock=120); 

select product_name from products where product_id = ANY(select product_id from 
inventory where quantity_in_stock>50); 
