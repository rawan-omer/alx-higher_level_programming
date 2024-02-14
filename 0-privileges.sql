-- Create user_0d_1
CREATE USER 'user_0d_1'@'localhost';

-- Grant user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2
CREATE USER 'user_0d_2'@'localhost';

-- Grant user_0d_2
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;
