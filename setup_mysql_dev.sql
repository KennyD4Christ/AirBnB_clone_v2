-- Script to prepare MySQL server for the project:
-- 1. Create database hbnb_dev_db if it doesn't already exist
-- 2. Create user hbnb_dev if it doesn't already exist and set the password to hbnb_dev_pwd
-- 3. Grant all privileges on the hbnb_dev_db database to the user hbnb_dev
-- 4. Grant SELECT privilege on the performance_schema database to the user hbnb_dev

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
