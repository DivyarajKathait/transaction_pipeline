CREATE DATABASE transaction_db;

-- Connect to this database and run:
CREATE TABLE transactions (
    transaction_id TEXT PRIMARY KEY,
    user_id INT,
    amount FLOAT,
    timestamp TIMESTAMP,
    location TEXT,
    status TEXT
);
