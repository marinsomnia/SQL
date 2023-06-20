# 1. Создайте таблицу с мобильными телефонами, используя графический интерфейс. Заполните БД данными.

CREATE DATABASE IF NOT EXISTS homework1;
USE homework1;

DROP TABLE IF EXISTS phone;
CREATE TABLE phone
(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    ProductName VARCHAR(45),
    Manufacturer VARCHAR(20),
    ProductCount INT,
    Price INT
 );
 
 INSERT phone (ProductName, Manufacturer, ProductCount, Price) 
 VALUES
     ("IPhone X", "Apple", 3, 76000), 
     ("IPhone 8", "Apple", 2, 51000),  
	 ("Galaxy S9", "Samsung", 2, 56000),
     ("Galaxy S8", "Samsung", 1, 41000),
     ("P20 Pro", "Huawei", 5, 36000);
     
SELECT * FROM phone;


# 2. Выведите название, производителя и цену для товаров, количество которых превышает 2.

SELECT ProductName, Manufacturer, Price
FROM phone
WHERE ProductCount > 2;

# 3. Выведите весь ассортимент товаров марки “Samsung”.

SELECT * FROM phone
WHERE Manufacturer = "Samsung";

# 4. Выведите информацию о телефонах, где суммарный чек больше 100 000 и меньше 145 000.

SELECT * FROM phone
WHERE ProductCount * Price > 100000 AND ProductCount * Price < 145000;

# 5. С помощью регулярных выражений найти (можно использовать операторы “LIKE”, “RLIKE” для 4.3 ):
#	4.1. Товары, в которых есть упоминание "Iphone"

SELECT * FROM phone
WHERE ProductName LIKE "Iphone%";

# 4.2. "Galaxy"

SELECT * FROM phone
WHERE ProductName LIKE "Galaxy%";


# Товары, в которых есть ЦИФРЫ.

SELECT * FROM phone
WHERE ProductName RLIKE "[0-9]";

# Товары, в которых есть ЦИФРА "8" 

SELECT * FROM phone
WHERE ProductName RLIKE "8";
