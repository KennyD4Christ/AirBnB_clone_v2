-- Script to prepare MySQL server for the project:
-- 1. Create database hbnb_test_db if it doesn't already exist
-- 2. Create user hbnb_test if it doesn't already exist and set the password to hbnb_test_pwd
-- 3. Grant all privileges on the hbnb_test_db database to the user hbnb_test
-- 4. Grant SELECT privilege on the performance_schema database to the user hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
