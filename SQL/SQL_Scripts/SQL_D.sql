use pet_adoption;
CREATE TABLE animals (
id INt, name varchar(50), 
breed varchar(50), 
color varchar(50), 
gender varchar(50), 
status INTEGER);
CREATE TABLE adoptions (
animal_id INT, 
name varchar(50), 
contact varchar(50), 
date TIMESTAMP);
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('89354034-20d9-4c3d-8195-3294bfd9dbc5', 'Bellyflop', 'Beagle', 'Brown', 'Male', 0);
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('ae91cf1c-f972-42f3-8160-6c04d935699c', 'Snowy', 'Husky', 'White', 'Female', 0);
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('37df3388-b0f4-4f0d-b6ef-0d840923a4d8', 'Princess', 'Pomeranian', 'Black', 'Female', 0);
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('94545432-d27a-4ac8-ab7c-38270d7535f3', 'Cricket', 'Chihuahua', 'Brown', 'Male', 0);
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('a1e7a7fc-b429-41ec-9924-8bb39dd397c8', 'Princess', 'Poodle', 'Purple', 'Female', 0);
INSERT INTO animals (id, name, breed, color, gender, status) VALUES ('5138ed53-2ab2-400b-973c-91186f8c673d', 'Spot', 'Dalmation', 'Black and White', 'Male', 0);
show tables;
SELECT * FROM ANIMALS;
select breed from animals;
SELECT name FROM animals WHERE gender = 'Female';
SELECT id FROM animals WHERE status = 0;

UPDATE animals SET color = 'Brown' WHERE id = '2';
select color from animals where id=2;
UPDATE animals SET color = 'Brown' WHERE color = 'Purple';

DELETE FROM animals WHERE id = '1';

UPDATE animals SET status = 1 WHERE id = '4';
INSERT INTO adoptions (animal_id, name, contact, date) VALUES ('10', 'Pinocchio', 'realboy@cockroachlabs.com', NOW());
UPDATE animals SET status = 1 WHERE id = '5';
INSERT INTO adoptions (animal_id, name, contact, date) VALUES ('11', 'Patalie', 'poodlequeen@cockroachlabs.com', NOW());
UPDATE animals SET status = 1 WHERE id = '6';
INSERT INTO adoptions (animal_id, name, contact, date) VALUES ('12', 'Ella', 'ellacrew@cockroachlabs.com', NOW());

SELECT * FROM ADOPTIONS ORDER BY DATE DESC;
SELECT * FROM ANIMALS;

ALTER TABLE animals ADD COLUMN species VARCHAR(50);

SET sql_safe_updates = FALSE;

UPDATE animals SET species = 'Dog';
SELECT * FROM animals;

INSERT INTO animals (id, name, species, breed, color, gender, status) VALUES ('14', 'Meowmix', 'Cat', 'Munchkin', 'Yellow', 'Female', 0);
INSERT INTO animals (id, name, species, breed, color, gender, status) VALUES ('15', 'Ash', 'Cat', 'Persian', 'Gray', 'Female', 0);
INSERT INTO animals (id, name, species, breed, color, gender, status) VALUES ('16', 'Tiger', 'Cat', 'Bengal', 'Brown', 'Male', 0);
CREATE TABLE shelters (
id INTEGER, 
name VARCHAR(50), 
location VARCHAR(50));
INSERT INTO shelters (id, name, location) VALUES (1, 'Animals 4 Homes', 'Red City');

ALTER TABLE animals ADD COLUMN shelter INTEGER;
UPDATE animals SET shelter = 1;
INSERT INTO shelters (id, name, location) VALUES (12, 'Adopt A Buddy', 'Green Town');
INSERT INTO shelters (id, name, location) VALUES (11, 'Fluffy Animals', 'Blue Hills');
INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) VALUES ('10', 'Snoops', 2, 'Dog', 'Beagle', 'Brown', 'Male', 0);
INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) VALUES ('11', 'Salt', 2, 'Cat', 'Turkish Angora', 'White', 'Female', 0);
INSERT INTO animals (id, name, shelter, species, breed, color, gender, status) VALUES ('12', 'Fuzz', 3, 'Dog', 'Papillon', 'Gray', 'Male', 0);
CREATE INDEX animal_shelter ON animals (shelter);
SELECT * FROM animals JOIN shelters ON animals.shelter = shelters.id;
SELECT * FROM adoptions JOIN animals ON adoptions.animal_id = animals.id WHERE animals.shelter = 1;
show tables;















