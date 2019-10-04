SELECT p1.name AS 'Person 1', p2.name AS 'Person 2', types.name AS 'Relationship' FROM relationships
	JOIN people AS p1
	ON relationships.people_a_id = p1.id
	JOIN people AS p2
	ON relationships.people_b_id = p2.id
	JOIN types
	ON relationships.type_id = types.id
	ORDER BY p1.id, types.id, p2.id;
	
SELECT types.name, types.id, types.line_color, types.line_style, relationships.people_a_id, relationships.people_b_id  FROM relationships
	JOIN types
	ON relationships.type_id = types.id;
	
SELECT * FROM types;