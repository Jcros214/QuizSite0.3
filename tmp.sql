PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE user (
        id INTEGER NOT NULL, 
        email VARCHAR(100), 
        password VARCHAR(100), 
        name VARCHAR(1000), 
        PRIMARY KEY (id), 
        UNIQUE (email)
);
-- INSERT INTO user VALUES(1,'jcros214@gmail.com','sha256$YUAgH910WcYSn9eg$cd1b1b802a3360043cb34e3e8297d1da7b3a8bda33ca3678caf3a3b2eec983d3','Jon');
COMMIT;


-- Drop the table 'TableName' in schema 'SchemaName'
IF EXISTS (
	SELECT *
		FROM sys.tables
		JOIN sys.schemas
			ON sys.tables.schema_id = sys.schemas.schema_id
	WHERE sys.schemas.name = N'SchemaName'
		AND sys.tables.name = N'TableName'
)
	DROP TABLE SchemaName.TableName
GO