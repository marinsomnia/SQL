CREATE DATABASE IF NOT EXISTS homework3; 
USE homework3;

DROP TABLE IF EXISTS staff;
CREATE TABLE staff
(
     id INT PRIMARY KEY AUTO_INCREMENT,
     firstname VARCHAR(45),
     lastname VARCHAR(45),
     post VARCHAR(45),
     seniority INT,
     salary DECIMAL(8,2),
     age INT	
);
INSERT INTO staff (firstname, lastname, post, seniority, salary, age)
VALUES
 ('Вася', 'Петров', 'Начальник', 40, 100000, 60),
 ('Петр', 'Власов', 'Начальник', 8, 70000, 30),
 ('Катя', 'Катина', 'Инженер', 2, 70000, 25),
 ('Саша', 'Сасин', 'Инженер', 12, 50000, 35),
 ('Иван', 'Петров', 'Рабочий', 40, 30000, 59),
 ('Петр', 'Петров', 'Рабочий', 20, 55000, 60),
 ('Сидр', 'Сидоров', 'Рабочий', 10, 20000, 35),
 ('Антон', 'Антонов', 'Рабочий', 8, 19000, 28),
 ('Юрий', 'Юрков', 'Рабочий', 5, 15000, 25),
 ('Максим', 'Петров', 'Рабочий', 2, 11000, 19),
 ('Юрий', 'Петров', 'Рабочий', 3, 12000, 24),
 ('Людмила', 'Маркина', 'Уборщик', 10, 10000, 49);
SELECT * FROM staff;

-- Отсортируйте данные по полю заработная плата (salary) в порядке: убывания; возрастания

SELECT * FROM staff
ORDER BY salary DESC;  -- по убыванию

SELECT * FROM staff
ORDER BY salary;      -- по возрастанию


-- Выведите 5 максимальных заработных плат (saraly)

SELECT salary 
FROM staff
ORDER BY salary DESC
LIMIT 5;

-- Посчитайте суммарную зарплату (salary) по каждой специальности (роst)

SELECT post, SUM(salary)
FROM staff
GROUP BY post; 

-- Найдите кол-во сотрудников с специальностью (post) «Рабочий» в возрасте от 24 до 49 лет включительно.

SELECT post, count(post) AS count_workers
FROM staff
WHERE post = "Рабочий" AND age >=24 AND age <= 49;


-- Найдите количество специальностей

SELECT COUNT(DISTINCT post) AS count_specialty
FROM staff;

-- Выведите специальности, у которых средний возраст сотрудников меньше 30 лет

SELECT post , AVG(age) AS average_age
FROM staff
GROUP BY post
HAVING AVG(age) <= 30;

-- Посчитать количество документов у каждого пользователя

SELECT
	COUNT(id) AS count_media,
    user_id, -- Внешний ключ на таблицу users
    (SELECT firstname FROM users WHERE users.id = media.user_id) AS user_name
FROM media
WHERE filename RLIKE "\.doc[x]?"
GROUP BY user_id
ORDER BY count_media DESC;

-- Посчитать лайки для моих документов (моих медиа)

SELECT
	CONCAT(u.firstname, " ", u.lastname) AS fullname, 
    m.filename AS media_name,
    m.id,
	COUNT(*) AS total_likes
FROM media m 
JOIN users u ON u.id = m.user_id
JOIN likes l ON l.media_id = m.id
WHERE u.id = 1
GROUP BY m.id;

