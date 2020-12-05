CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at DATE NOT NULL,
    passhash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS shortcuts (
  shortcut_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  token VARCHAR(32) NOT NULL UNIQUE,
  target_url VARCHAR(500) NOT NULL,
  created_at DATE NOT NULL,
  visits INT NOT NULL,
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);
