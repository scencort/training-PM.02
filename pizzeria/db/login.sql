DROP DATABASE pizzeria;
CREATE DATABASE pizzeria;

USE pizzeria;

CREATE TABLE Roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO Roles (role_name) VALUES
('guest'),
('client'),
('operator'),
('manager'),
('admin');

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    contact_info VARCHAR(255),

    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);

INSERT INTO Users (username, password_hash, role_id, contact_info) VALUES
('admin', 'admin123', 5, 'admin@mail.ru'),
('client1', 'client123', 2, 'client@mail.ru'),
('operator1', 'operator123', 3, 'operator@mail.ru');

CREATE TABLE MenuItems (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(8,2) NOT NULL,
    category VARCHAR(50)
);

INSERT INTO MenuItems (name, description, price, category) VALUES
('Маргарита', 'Томатный соус, моцарелла', 450.00, 'Пицца'),
('Пепперони', 'Пепперони, сыр, соус', 550.00, 'Пицца'),
('4 сыра', 'Моцарелла, дорблю, чеддер, пармезан', 600.00, 'Пицца'),
('Цезарь', 'Курица, салат, соус', 350.00, 'Салат'),
('Тирамису', 'Классический десерт', 300.00, 'Десерт');

CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(50) DEFAULT 'Ожидает приготовления',
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE OrderItems (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (item_id) REFERENCES MenuItems(item_id)
);
