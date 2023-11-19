

CREATE TABLE Shoppers (
    shopper_id INT PRIMARY KEY,
    name VARCHAR(255),
);

CREATE TABLE Items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255),
    item_price DOUBLE,
);

CREATE TABLE ShoppingLists (
    list_id INT PRIMARY KEY,
    shopper_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (shopper_id) REFERENCES Shoppers(shopper_id)
);

CREATE TABLE ListItems (
    list_item_id INT PRIMARY KEY,
    list_id INT,
    item_id INT,
    FOREIGN KEY (list_id) REFERENCES ShoppingLists(list_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);