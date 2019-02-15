create database candystore;
use candystore;
drop table products;
create table products (
	product_id int not null auto_increment,
    description_tx varchar(255) not null,
    primary key(product_id)
);
insert into products(description_tx) values('Bitcoin');
insert into products(description_tx) values('Litecoin');
insert into products(description_tx) values('Ether');
select * from products;
create table orders (
	order_id int not null auto_increment,
    product_id int not null,
    primary key(order_id)
)