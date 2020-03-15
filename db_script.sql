INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject) VALUES('demouser','localhost',PASSWORD('demopassword'),'','','');
FLUSH PRIVILEGES;
SELECT User, Host, authentication_string FROM mysql.user;

CREATE DATABASE IF NOT EXISTS financial_database;
USE financial_database;

DROP TABLE IF EXISTS financial;
CREATE TABLE financial ( financial_id int unsigned not null auto_increment, segment varchar(128), country varchar(128), product varchar(128), discount_band varchar(128), units_sold float, manufacturing_price int, sale_price int, gross_sales float, discounts float, sales float, cogs float, profit float, date datetime, month_number int, month_name varchar(128), year int, primary key (financial_id) );