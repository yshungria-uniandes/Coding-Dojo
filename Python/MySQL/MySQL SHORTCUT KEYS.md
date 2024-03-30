MYSQL
-----------
Run this on the command line. Not in mysql console.
eg. $alberta_makeever: mysql -u root -p user_development << sample.sql

mysql5 -u root -p
enter password:kwame1
mysql> exit;

Order.includes(:order_products).where("order_products.product_id = 16227").references(:order_products)
 SELECT * FROM orders INNER JOIN order_products ON order_products.order_id = orders.id WHERE order_products.product_id = 16227;

SELECT products.id, products.magstar_id  FROM products ORDER BY id ASC LIMIT 20;
 SELECT `orders`.* FROM `orders` WHERE (orders.magstar_id IS NOT null AND orders.magstar_submitted_at IS NOT null) AND (order_type IS NOT null AND orders.order_type != 'C') AND `orders`.`deleted` = 0 AND (orders.magstar_id NOT LIKE '%F%') AND (submitted_at between '2015-04-29 00:00:00' and '2015-04-29 23:59:59') AND (total_cost >= 900.00)


SELECT DISTINCT COUNT(DISTINCT `orders`.`id`) FROM `orders` INNER JOIN `order_products` ON `order_products`.`order_id` = `orders`.`id` WHERE (orders.magstar_id IS NOT null AND orders.magstar_submitted_at IS NOT null) AND (order_type IS NOT null AND orders.order_type != 'C') AND `orders`.`deleted` = 0 AND (orders.magstar_id NOT LIKE '%F%') AND (submitted_at >= '2015-04-27 00:00:00.000000') AND (orders.magstar_id NOT LIKE '%F%') AND (order_product_quantities_count >= 12) AND (order_product_quantities_count > order_products_count) AND (order_products.quantity >= 12)


Create a database on the sql server.
mysql> create database [databasename];

List all databases on the sql server.
mysql> show databases;

Switch to a database.
mysql> use [db name];

To see all the tables in the db.
mysql> show tables;

To see database's field formats.
mysql> describe [table name];

To delete a db.
mysql> drop database [database name];

To delete a table.
mysql> drop table [table name];

Show all data in a table.
mysql> SELECT * FROM [table name];

Returns the columns and column information pertaining to the designated table.
mysql> show columns from [table name];

Show certain selected rows with the value "whatever".
mysql> SELECT * FROM [table name] WHERE [field name] = "whatever";

Show all records containing the name "Bob" AND the phone number '3444444'.
mysql> SELECT * FROM [table name] WHERE name = "Bob" AND phone_number = '3444444';

Show all records not containing the name "Bob" AND the phone number '3444444' order by the phone_number field.
mysql> SELECT * FROM [table name] WHERE name != "Bob" AND phone_number = '3444444' order by phone_number;

Show all records starting with the letters 'bob' AND the phone number '3444444'.
mysql> SELECT * FROM [table name] WHERE name like "Bob%" AND phone_number = '3444444';

Show all records starting with the letters 'bob' AND the phone number '3444444' limit to records 1 through 5.
mysql> SELECT * FROM [table name] WHERE name like "Bob%" AND phone_number = '3444444' limit 1,5;

Use a regular expression to find records. Use "REGEXP BINARY" to force case-sensitivity. This finds any record beginning with a.
mysql> SELECT * FROM [table name] WHERE rec RLIKE "^a";

Show unique records.
mysql> SELECT DISTINCT [column name] FROM [table name];

Show selected records sorted in an ascending (asc) or descending (desc).
mysql> SELECT [col1],[col2] FROM [table name] ORDER BY [col2] DESC;

Return number of rows.
mysql> SELECT COUNT(*) FROM [table name];

Sum column.
mysql> SELECT SUM(*) FROM [table name];

Join tables on common columns.
mysql> select lookup.illustrationid, lookup.personid,person.birthday from lookup left join person on lookup.personid=person.personid=statement to join birthday in person table with primary illustration id;

Delete a row(s) from a table.
mysql> DELETE from [table name] where [field name] = 'whatever';

Delete a column.
mysql> alter table [table name] drop column [column name];

Add a new column to db.
mysql> alter table [table name] add column [new column name] varchar (20);

Change column name.
mysql> alter table [table name] change [old column name] [new column name] varchar (50);

Make a unique column so you get no dupes.
mysql> alter table [table name] add unique ([column name]);

Make a column bigger.
mysql> alter table [table name] modify [column name] VARCHAR(3);

Delete unique from table.
mysql> alter table [table name] drop index [colmn name];

Load a CSV file into a table.
mysql> LOAD DATA INFILE '/tmp/filename.csv' replace INTO TABLE [table name] FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (field1,field2,field3);

Dump all databases for backup. Backup file is sql commands to recreate all db's.
# [mysql dir]/bin/mysqldump -u root -ppassword --opt >/tmp/alldatabases.sql

Dump one database for backup.
# [mysql dir]/bin/mysqldump -u username -ppassword --databases databasename >/tmp/databasename.sql

Dump a table from a database.
# [mysql dir]/bin/mysqldump -c -u username -ppassword databasename tablename > /tmp/databasename.tablename.sql

Restore database (or database table) from backup.
# [mysql dir]/bin/mysql -u username -ppassword databasename < /tmp/databasename.sql

Create Table Example 1.
mysql> CREATE TABLE [table name] (firstname VARCHAR(20), middleinitial VARCHAR(3), lastname VARCHAR(35),suffix VARCHAR(3),officeid VARCHAR(10),userid VARCHAR(15),username VARCHAR(8),email VARCHAR(35),phone VARCHAR(25), groups VARCHAR(15),datestamp DATE,timestamp time,pgpemail VARCHAR(255));

Create Table Example 2.
mysql> create table [table name] (personid int(50) not null auto_increment primary key,firstname varchar(35),middlename varchar(50),lastnamevarchar(50) default 'bato');

//LEFT JOIN
 the row’s content are selected as an output row. When row in the left table has no match it is still selected for output, but combined with a “fake” row from the right table that contains NULL in all columns. In short, the MySQL LEFT JOIN clause allows you to select all rows from the left table even there is no match for them in the right table. ( t1 = table 1, c1 = column 1 ... )
*************
SELECT t1.c1, t1.c2,…t2.c1,t2.c2
FROM t1
LEFT JOIN t2 ON t1.c1 = t2.c1 …(join_condition)
WHERE where_condition

eg,
Position(FK)  Age
--------      ---
Dad	      41
Mom	      45
Daughter      17
Dog
	
Meal	Position(FK)
----    --------
Steak	Dad
Salad	Mom
Spinach Soup	
Tacos	Dad

SELECT c.customerNumber, customerName,orderNUmber, o.status
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber;
*****customerNumber here is the the foreign key that links the two table.

"SELECT family.Position, food.Meal ".
"FROM family 
LEFT JOIN food ".
	"ON family.Position = food.Position";
*****Position here is the the foreign key that links the two table.
OUTPUT

Position  Meal
-------   ----
Dad - Steak
Dad - Tacos
Mom - Salad
Daughter -
Dog -

//INNER JOIN
For example, if you join two tables A and B, the MySQL INNER JOIN clause compares each record of the table A with each record of table B to find all pair of records that satisfy the join-condition. When the join-condition are satisfied, column values for each matched pair of record of table A and table B are combined into a returned record. Note that the records on both tables have to match based on the join-condition. 

** If no record on both table A and B matches, the query will return an empty result

Avoid column ambiguous error in MySQL INNER JOIN

f you join multiple tables that has column with similar name, you have to use table qualifier to refer to column to avoid column ambiguous error. Suppose if table tbl_A and tbl_B has the same column M. In the SELECT statement with MySQL INNER JOIN clause, you have to refer to column M by using the table qualifier as tbl_A.M or tbl_B.M (table_name.column_name). 


SELECT A.productCode, A.productName, B.orderNumber
FROM products A
INNER JOIN orderDetails B on A.productCode = B.productCode;

*****productCode here is the the foreign key that links the two table.

eg, Table Products
ProductName(FK)  ProductCode
--------      ---
Mercedes      41
Ford	      45
Jaguar        17
Land Rover    29

Table Orderdetails	
OrderNumber	ProductCode(FK)
----            --------
102	        41
103         	45
104             17	
105	        23


SELECT A.productCode, A.productName, B.orderNumber
FROM products A
INNER JOIN orderDetails B on A.productCode = B.productCode;