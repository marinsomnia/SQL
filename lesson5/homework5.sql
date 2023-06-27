CREATE DATABASE IF NOT EXISTS hw5_1; 
USE hw5_1;
SELECT * FROM cars_generate;

-- Создайте представление, в которое попадут автомобили стоимостью  до 25 000 долларов

CREATE OR REPLACE VIEW view_cars 
AS SELECT *
FROM cars_generate 
WHERE price < 25000
ORDER BY price;
SELECT * FROM view_cars;

-- Изменить в существующем представлении порог для стоимости: пусть цена будет до 30 000 долларов 
-- (используя оператор ALTER VIEW) 

ALTER VIEW view_cars 
AS SELECT *
FROM cars_generate 
WHERE price < 30000
ORDER BY price;
SELECT * FROM view_cars;

-- Создайте представление, в котором будут только автомобили марки “BMW” и “Ауди”

CREATE OR REPLACE VIEW cars_audi_bmw 
AS SELECT *
FROM cars_generate 
WHERE make IN ('BMW', 'Audi')
ORDER BY make;
SELECT * FROM cars_audi_bmw;

-- Добавьте новый столбец под названием «время до следующей станции». 

DROP TABLE IF EXISTS train_schedule;
CREATE TABLE train_schedule
(
     train_id_integer INT,
     station_character_varying VARCHAR(45),
     station_time TIME
);
INSERT INTO train_schedule (train_id_integer, station_character_varying, station_time)
VALUES
 (110, 'San Francisco', '10:00:00'),
 (110, 'Redwood City', '10:54:00'),
 (110, 'Palo Alto', '11:02:00'),
 (110, 'San Jose', '12:35:00'),
 (120, 'San Francisco', '11:00:00'),
 (120, 'Palo Alto', '12:49:00'),
 (120, 'San Jose', '13:30:00');
 
SELECT train_id_integer, station_character_varying, station_time,
       TIMEDIFF(LEAD(station_time) OVER (PARTITION BY train_id_integer), station_time) AS time_to_next_station
FROM train_schedule;
