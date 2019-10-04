# DROP DATABASE IF EXISTS relationship_app;

# CREATE DATABASE IF NOT EXISTS relationship_app;

USE relationship_app

DROP TABLE IF EXISTS relationships;
DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS types;

CREATE TABLE people(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255),
	node_color CHAR(6)
);

CREATE TABLE types(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE,
	line_color CHAR(6),
	line_style ENUM('Solid', 'Dashed', 'Dotted') DEFAULT 'Solid' NOT NULL
);

CREATE TABLE relationships(
	people_a_id INT NOT NULL,
	people_b_id INT NOT NULL,
	type_id INT NOT NULL,
	FOREIGN KEY(people_a_id) REFERENCES people(id) ON DELETE CASCADE,
	FOREIGN KEY(people_b_id) REFERENCES people(id) ON DELETE CASCADE,
	FOREIGN KEY(type_id) REFERENCES types(id) ON DELETE CASCADE,
	UNIQUE(people_b_id,	people_a_id)
);

source bootstrap_data.sql
source test_data.sql