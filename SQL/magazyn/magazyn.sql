DROP TABLE IF EXISTS tbCustomers;
CREATE TABLE tbCustomers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    address TEXT
)

DROP TABLE IF EXISTS tbOrders;
CREATE TABLE tbOrders (
    order_id INTEGER,
    customer_id INTEGER INTEGER PRIMARY KEY AUTOINCREMENT,
    subscription_id INTEGER,
    purchase_date DATE
    
    FOREIGN KEY (customer_id) REFERENCES tbCustomers(customer_id),
    FOREIGN KEY (customer_id) REFERENCES tbSubscriptions(customer_id)
    FOREIGN KEY (order_id) REFERENCES tbSubscriptions(order_id)
)

DROP TABLE IF EXISTS tbSubscriptions;
CREATE TABLE tbSubscriptions (
    subscription_id INTEGER,
    description TEXT,
    price_per_month NUMERIC,
    subscription_length TEXT
)
