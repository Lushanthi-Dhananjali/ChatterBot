-- 1. Use your existing database
USE healthy_food_db;

-- 2. Drop the old table and create a better one
DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),      -- Breakfast, Lunch, or Dinner
    food_name VARCHAR(100),    -- e.g., 'Oatmeal'
    description TEXT,          -- Why it is healthy
    is_healthy BOOLEAN DEFAULT TRUE
);

-- 3. Insert specific food data
INSERT INTO recipes (category, food_name, description) VALUES 
('Breakfast', 'Oatmeal', 'High in fiber and keeps you full for a long time.'),
('Breakfast', 'Eggs', 'Great source of protein and healthy fats for brain health.'),
('Lunch', 'Quinoa Salad', 'Contains all nine essential amino acids and is gluten-free.'),
('Lunch', 'Grilled Chicken', 'Lean protein that helps in muscle repair and growth.'),
('Dinner', 'Salmon', 'Rich in Omega-3 fatty acids which are great for heart health.'),
('Dinner', 'Steamed Broccoli', 'Packed with vitamins K and C, and helps with digestion.');

-- 4. Add some "unhealthy" items for the bot to recognize
INSERT INTO recipes (category, food_name, description, is_healthy) VALUES 
('General', 'Pizza', 'High in saturated fats and refined carbs.', FALSE),
('General', 'Soda', 'Contains high amounts of sugar and no nutritional value.', FALSE);