-- show all records with a score >= 10 in table second_table in database hbtn_0c_0
-- Results should display both the score and the name
-- Record should be ordered by score (top first)

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;