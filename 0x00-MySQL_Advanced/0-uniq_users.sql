-- creates a table users
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
