-- creates the table unique_id on my MySQL server
CREATE TABLE unique_id(
	id INT  DEFAULT 1,
	name VARCHAR(256),
	UNIQUE(id)
);
