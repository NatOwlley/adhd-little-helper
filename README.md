Little helper for my ADHD friend. WIP

Notes:
Connect to db and create a table beforehand:
CREATE TABLE entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time VARCHAR(5) NOT NULL,  
    text VARCHAR(200) NOT NULL
);