show databases;
create database ecommerce_db;
use ecommerce_db; 
---------------------------------------
create table users(
	id integer auto_increment primary key,
	name varchar(63) not null,
	email varchar(127),
	passward varchar(127),
	phone varchar(15),
	created_at datetime default current_timestamp,
	modified_at datetime default current_timestamp
);
show tables;
SELECT * FROM users LIMIT 2;
SELECT * FROM users ORDER BY created_at DESC LIMIT 2;
SELECT DISTINCT gender FROM users;
-- Select 2 new users
SELECT * FROM users ORDER BY created_at DESC LIMIT 2;
-- Select 2 old or first 2 users:
SELECT * FROM users ORDER BY created_at ASC LIMIT 2;
-- Count the number of female users
SELECT COUNT(*) AS female_users_count FROM users WHERE gender = 'F';
desc users; 
alter table users drop column name;
alter table users drop column  modifide_at;
alter table users add column modified_at datetime default current_timestamp;
alter table users add column name varchar(63) not null after id;
drop table user;
insert into users(name) values("subham");
select * from users;
delete from users where id=2;
UPDATE users SET name = "Subham", email = "subham@gmail.com" WHERE id = 1;

insert into users(name, email, passward, phone) 
	values("dev", "dev@gmail.com", "4651@58", "1554358"),
	("ram", "ram@gmail.com", "545sf35", "455268582");
update users set phone="8542665452" where name="ram"; 
select * from users where name="ram";
select count(*) from users;
insert into users(id, name, email, passward, phone, created_at, modified_at)
	select id, name, email, passward, phone, created_at, modified_at from user;
--------------------------

create table products(
	id integer auto_increment primary key,
	name varchar(63) not null,
	description varchar(1024),
	mrp decimal(10,2),
	sale_price decimal(10,2),
	created_at datetime default current_timestamp,
	modified_at datetime default current_timestamp
);
insert into products(name, description, mrp, sale_price) 
values("Pen3", "This pen color is blue", 180.50, 179),
	  ("Book3", "This Book is math", 239.20, 138.20),
	  ("duster", "This duster is use a clear the blacKbord", 80.50, 75);
select * from products;
select name, mrp from products where mrp <=15;
select name, mrp from products where mrp >=15;

Most expensive ( high or maximum cost)
select max(mrp) from products;

Cheapest or less expensive (low cost)
select min(mrp) from products;
-------------------------------------
create table carts(
	id integer auto_increment primary key,
	user_id integer references users(id) on delete cascade,
	created_at datetime default current_timestamp,
	modified_at datetime default current_timestamp);

or

create table carts(
	id integer auto_increment,
	user_id integer,
	created_at datetime default current_timestamp,
	modified_at datetime default current_timestamp,
	primary key(id),
	foreign key(user_id) references users(id) on delete cascade);

insert into carts(user_id)
values(1),
	  (3),
	  (5);


insert into carts(id, user_id)
values (1, 3),
(2,6);
	 
desc carts;
alter table carts drop column users_id;
alter table carts add column user_id integer;
alter table carts drop column user_id;
alter table carts add column user_id integer foreign key references user(id) on delete cascade;
alter table carts add  column user_id integer not null after id;
----------------------------------------------------
create table cart_items(
	id integer auto_increment primary key,
	cart_id integer,
	product_id integer references products(id) on delete cascade,
    quantity integer);
insert into cart_items(cart_id, product_id, quantity)
values(1, 3, 3),
(1, 4, 1),
(11, 9, 1);

--------------------------------
create table orders(
	id integer auto_increment primary key,
	cart_id integer references carts(id) on delete cascade,
	order_total_amount decimal (10,2),
	discount decimal (10,2),
	created_at datetime default current_timestamp,
	modified_at datetime default current_timestamp);
insert into orders(cart_id, order_total_amount, discount)
values(7,627, 0),
(11, 75, 70);
desc orders;
update orders set cart_id=1 where id=1;
delete from orders where id in(3);
update orders set id=3 where cart_id=11;
--------------------------
create table order_items (     
	id integer auto_increment primary key,
	order_id integer references orders(id) on delete  cascade,
	product_id integer references products(id) on delete cascade,
	product_name varchar(255),
	product_description varchar(1023),
	product_mrp decimal(10,2),
	product_sale_price decimal(10,2),
	quantity integer,
	created_at datetime default current_timestamp,
	modified_at datetime default current_timestamp
	);       
insert into order_items(order_id, product_id, product_name, product_description, product_mrp, product_sale_price, quantity)
values(1, 3, "Pen2", "This pen color is blue", 160.50, 150, 3),
(1, 4, "Book2", "This Book is math", 1.20, 1.20, 1),
(2 ,5, "pen1,","This pen is black", 5.50, 4, 1),
(2, 6, "Book1,", "This book is scienc", 199, 199,1),
(2, 7, "Pen2", "This pen is No:1", 10, 9, 1),
(2, 8,"Book2", "This book is english", 299, 297, 1)
(3, 9, "duster", "This duster is use a clear the blacKbord", );
desc order_items;
select u.name, u.email, ci.* from users u
join carts c on u.id=c.user_id
join order_items ci on c.id= ci.cart_id
where u.id=3;
delete from order_items where product_id in (7,8);
update order_items set quantity=5 where id=10;
----------------------------------------------
                  
-------------------------------------------------------------
create table payment_methods(
	id integer auto_increment primary key,
	name varchar(1023),
	config json );
insert into payment_methods(name, config)
values ("cash", '{}'),
( "Phonepe", '{"user_name": "abc", "passward": "1234556"}'),
	  ( "paytm", '{"user_name": "abc", "passward": "1234556"}');
-------------------------------------------------------------
create table payments(
	id integer auto_increment primary key,
	order_id integer references orders(id) on delete cascade,
	payment_method_id integer,
	payment_amount decimal(10,2));
insert into payments(order_id, payment_method_id, payment_amount)
values(1, 1, 600),
(2, 2, 798);
desc payments;
--------------------------------------------------------------
create table return_orders(id integer auto_increment primary key,
amount decimal (10,2),
payment_method_id integer references payment_methods(id) on delete cascade,
created_at datetime default current_timestamp,
modified_at datetime default current_timestamp);
insert into return_orders(payment_method_id)
values(1);
update return_orders o set amount = (select sum(product_sale_price*quantity) from order_items oi where order_id=1)
------------------------------------------------------                   
create table return_items(
id integer auto_increment primary key,
return_order_id integer references orders(id) on delete cascade,
order_item_id integer references order_items(id) on delete cascade,
product_name varchar(511),
product_mrp decimal(10,2),
product_sale_price decimal(10,2),
quantity integer, 
reason varchar(1023),
created_at datetime default current_timestamp,
modified_at datetime default current_timestamp);

insert into return_items(return_order_id, order_item_id, product_name, product_mrp, product_sale_price, quantity, reason)
values(1, 1, "Pen2", 160.50, 150, 2, "item defective");                                                                                          

-----------------------------
select u.id, u.name, o.id, oi.*
from users u 
join carts c on u.id = c.user_id
join orders o on o.cart_id = c.id
join order_items oi on oi.order_id = o.id
where u.name="subham";

select sum(mrp) from products;
select id, mrp from products where id = 1;
select * from products where name like "p%";
select * from products where name like "%2";
select count(*) from products;
select * from products where mrp <=10;
select * from products where mrp >10 and mrp <100;
select * from products where year(created_at)=2024;
select * from products where month(created_at)=12;
select year(created_at), count(*) from products group by year(created_at);
select year(created_at), count(*) from products group by year(created_at) order by year(created_at) desc;
-- // desc means descending order 
select * from products order by name asc;
-- // asc means ascending order
select * from products order by name desc;
select year(created_at), count(*) from orders group by year(created_at) order by year(created_at) desc;
update orders o set order_total_amount =(select sum(product_sale_price*quantity) from order_items oi where oi.order_id = 2)
	where o.id=2;

insert into cart_items(cart_id, product_id, quantity)
	select 7, product_id, quantity from order_items where order_id = 2;

select u.id, u.name, o.id, oi.*, o.created_at, pm.name from users u
join carts c on u.id = c.user_id
join orders o on o.cart_id = c.id 
join order_items oi on oi.order_id = o.id 
join payments p on p.order_id = o.id
join payment_methods pm  on pm.id = p.payment_method_id;

select date(created_at), sum(quantity) from order_items where product_id = 5 group by date(created_at);
----------------------
insert into users(name, email, passward, phone) 
	values("dev", "dev@gmail.com", "4651@58", "1554358");

insert into products(name, description, mrp, sale_price) 
values("duster", "This duster is use a clear the blacKbord", 80.50, 75),
("keybord", "this keybord brand is intex", 700, 699);

insert into carts(user_id)
values(5);

insert into cart_items(cart_id, product_id, quantity)
values(11, 9, 1);

insert into orders(cart_id, order_total_amount, discount)
values(11, 75, 70);

insert into order_items(order_id, product_id, product_name, product_description, product_mrp, product_sale_price, quantity)
values(3, 9, "duster", "This duster is use a clear the blacKbord",  80.50, 75, 1);

insert into payment_methods(name, config)
values( "paytm", '{"user_name": "abc", "passward": "1234556"}');

insert into payments(order_id, payment_method_id)
values(3, 3);

update payments set payment_amount=75 where order_id=3;


update payments set payment_amount=(select sum(product_sale_price*quantity) from order_items where order_id=3)
where order_id=3;

update cart_items set quantity=3 where id=15;
update order_items set quantity=3 where id=7;
                   