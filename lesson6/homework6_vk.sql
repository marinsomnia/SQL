USE homework6_vk;

-- Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, communities и messages в 
-- таблицу logs помещается время и дата создания записи, название таблицы, идентификатор первичного ключа. (Триггеры*)

-- Создание таблицы logs

DROP TABLE IF EXISTS `logs` ;
CREATE TABLE `logs` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  `table_name` VARCHAR(255) NOT NULL,
  primary_key_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Создание триггера для таблицы users
DELIMITER $$
CREATE TRIGGER users_insert_trigger AFTER INSERT ON users
FOR EACH ROW
BEGIN
  INSERT INTO `logs` (primary_key_id, `table_name`) VALUES (NEW.id, 'users');
END$$
DELIMITER ;

-- Создание триггера для таблицы communities

DELIMITER $$
CREATE TRIGGER communities_insert_trigger AFTER INSERT ON communities
FOR EACH ROW
BEGIN
  INSERT INTO `logs` (primary_key_id, `table_name`) VALUES (NEW.id, 'communities', );
END$$
DELIMITER ;

-- Создание триггера для таблицы messages

DELIMITER $$
CREATE TRIGGER messages_insert_trigger AFTER INSERT ON messages
FOR EACH ROW
BEGIN
  INSERT INTO `logs` (primary_key_id, `table_name`) VALUES (NEW.id, 'messages');
END$$
DELIMITER ;

SELECT * FROM `logs`;




-- Создать функцию, вычисляющей коэффициент популярности пользователя (по количеству друзей)

SELECT 
	CONCAT(u.firstname, " ", u.lastname) AS fullname,
	u.id AS user_id,
	COUNT(f.status) as total_friends,
    DENSE_RANK() OVER(ORDER BY COUNT(f.status) DESC) AS `rating`
FROM users u
JOIN friend_requests f ON f.initiator_user_id = u.id
WHERE f.`status` = 'approved'
GROUP BY u.id, f.`status`;





