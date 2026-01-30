-- 1. Create and use the database
CREATE DATABASE IF NOT EXISTS healthy_food_db;
USE healthy_food_db;

-- 2. Drop the old table to start fresh with new columns
DROP TABLE IF EXISTS recipes;

-- 3. Create the table with columns for category, food name, and description
CREATE TABLE recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),      -- Breakfast, Lunch, or Dinner
    food_name VARCHAR(100),    -- The specific food name
    description TEXT,          -- Why it is healthy (Step 4 & 5)
    is_healthy BOOLEAN DEFAULT TRUE -- To filter unhealthy items
);

-- 4. Insert the lists you provided in Step 3
-- BREAKFAST ITEMS
INSERT INTO recipes (category, food_name, description) VALUES 
('Breakfast', 'Oats', 'High in fiber to keep you full and improve heart health.'),
('Breakfast', 'Boiled eggs', 'Great source of high-quality protein and brain-healthy choline.'),
('Breakfast', 'Whole-wheat bread', 'Provides complex carbohydrates for steady energy levels.'),
('Breakfast', 'Milk', 'Rich in calcium and vitamin D for strong bones.'),
('Breakfast', 'Yogurt (curd)', 'Contains probiotics that are excellent for gut health.'),
('Breakfast', 'Fruits (banana, apple, papaya)', 'Loaded with essential vitamins and antioxidants.'),
('Breakfast', 'Vegetable omelette', 'Combines protein with fiber for a balanced start.'),
('Breakfast', 'Idli', 'Fermented food that is easy to digest and low in calories.');

-- LUNCH ITEMS
INSERT INTO recipes (category, food_name, description) VALUES 
('Lunch', 'Brown rice', 'Retains bran and germ, providing more fiber than white rice.'),
('Lunch', 'Red rice', 'Contains antioxidants and helps regulate blood sugar.'),
('Lunch', 'Whole-wheat roti', 'Better than refined flour for digestion and energy.'),
('Lunch', 'Dal (lentils)', 'Key plant-based protein source that supports muscle repair.'),
('Lunch', 'Grilled or boiled chicken', 'Lean protein that keeps metabolism active.'),
('Lunch', 'Fish curry (less oil)', 'Rich in Omega-3 fatty acids for brain and heart health.'),
('Lunch', 'Mixed vegetable curry', 'A variety of vitamins and minerals in one dish.'),
('Lunch', 'Green leafy vegetables', 'High in iron and vitamins A and C.');

-- DINNER ITEMS
INSERT INTO recipes (category, food_name, description) VALUES 
('Dinner', 'Vegetable soup', 'Light and hydrating, perfect for easy digestion before sleep.'),
('Dinner', 'Steamed vegetables', 'Retains maximum nutrients compared to frying.'),
('Dinner', 'Light dal', 'Provides protein without being too heavy on the stomach.'),
('Dinner', 'Grilled fish', 'Easy-to-digest protein with healthy fats.'),
('Dinner', 'Paneer (low fat)', 'Good calcium source for bone health while you sleep.'),
('Dinner', 'Boiled eggs', 'Simple protein source that supports body repair during sleep.'),
('Dinner', 'Stir-fried vegetables (less oil)', 'Quick to cook, keeps nutrients, and easy for the stomach.'),
('Dinner', 'Fruit bowl', 'Natural sweetness with vitamins and fiber for a light end to the day.');


-- 5. Add some "unhealthy" items so the bot can warn users later
INSERT INTO recipes (category, food_name, description, is_healthy) VALUES 
('General', 'Pizza', 'High in saturated fats and refined carbs.', FALSE),
('General', 'Soda', 'Contains excessive sugar and zero nutritional value.', FALSE);

-- 6. Verify the data is there
SELECT * FROM recipes;

USE healthy_food_db;

-- Create table for Step 2 Categories
TRUNCATE TABLE food_categories;

-- Insert Step 2 data
INSERT INTO food_categories (category_name, examples, benefits) VALUES 
('Fruits', 'Apple, banana, orange, papaya, mango', 'Rich in vitamins & fiber, Improves digestion, Boosts immunity'),
('Vegetables', 'Carrot, spinach, broccoli, beans', 'Good for eyes, skin, and blood, Prevents many diseases, Low in calories'),
('Whole Grains', 'Brown rice, oats, whole-wheat bread', 'Gives long-lasting energy, Good for digestion, Controls blood sugar'),
('Protein Foods', 'Animal: Fish, eggs, milk, chicken | Plant: Lentils, beans, nuts', 'Builds muscles, Repairs body tissues, Strengthens immunity'),
('Healthy Fats', 'Nuts, seeds, avocado, olive oil', 'Good for heart and brain, Helps absorb vitamins');

SELECT * FROM food_categories;