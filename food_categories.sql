USE healthy_food_db;

-- Create table for Step 2 Categories
CREATE TABLE IF NOT EXISTS food_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100),
    examples TEXT,
    benefits TEXT
);

-- Insert Step 2 data
INSERT INTO food_categories (category_name, examples, benefits) VALUES 
('Fruits', 'Apple, banana, orange, papaya, mango', 'Rich in vitamins & fiber, Improves digestion, Boosts immunity'),
('Vegetables', 'Carrot, spinach, broccoli, beans', 'Good for eyes, skin, and blood, Prevents many diseases, Low in calories'),
('Whole Grains', 'Brown rice, oats, whole-wheat bread', 'Gives long-lasting energy, Good for digestion, Controls blood sugar'),
('Protein Foods', 'Animal: Fish, eggs, milk, chicken | Plant: Lentils, beans, nuts', 'Builds muscles, Repairs body tissues, Strengthens immunity'),
('Healthy Fats', 'Nuts, seeds, avocado, olive oil', 'Good for heart and brain, Helps absorb vitamins');