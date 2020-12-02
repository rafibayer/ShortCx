CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    created_at DATE NOT NULL,
    passhash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS shortcuts (
    shorcut_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(255) NOT NULL,
    target_url VARCHAR(500) NOT NULL,
    created_at DATE NOT NULL,
    visits INT NOT NULL
);