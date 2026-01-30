-- Create the database
CREATE DATABASE healthy_food_db;

-- Switch to using it
USE healthy_food_db;

-- Create your table
CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    guideline TEXT
);employeetemployeet