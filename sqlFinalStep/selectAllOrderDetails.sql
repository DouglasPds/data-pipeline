SELECT * 
FROM orders
INNER JOIN order_details
WHERE orders.order_id = order_details.order_id