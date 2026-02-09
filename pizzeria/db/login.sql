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

