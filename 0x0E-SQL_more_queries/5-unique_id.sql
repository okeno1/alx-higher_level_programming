-- Create a table unique id
-- DDL query to create a table with default value and must be unique
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);
