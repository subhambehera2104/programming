CREATE USER 'flask_app'@'localhost' IDENTIFIED BY '12345678';
GRANT ALL ON *.* TO 'flask_app'@'localhost' WITH GRANT OPTION;

create database flask_db;
use flask_db;
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(255) NOT NULL,
phone varchar(15) NOT NULL,
gender VARCHAR(1) NOT NULL,
created_at datetime default current_timestamp,
updated_at datetime default current_timestamp 
);
insert into users(name, email, password, gender)
value("subham behera", "subhambehera2104@gmail.com", "12345678", "m");