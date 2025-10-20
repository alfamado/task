-- CREATE TABLE authors(
--   authorId serial primary key,
--   authorName varchar(100),
--   countryOfOrigin varchar(200),
--   numberOfBooksWritten int
-- );

-- CREATE TABLE books(
--   bookId serial primary key,
--   title varchar(100),
--   authorId int,
--   genre varchar(100),
--   dateOfPublication date,
--   publisher varchar(100),
--   isbn varchar(100) unique,
--   language varchar (100),
--   availableCopies int,
--   ageRating varchar (100),
--   FOREIGN KEY (authorId) REFERENCES authors(authorId)
-- );

-- CREATE TYPE fulfillment AS ENUM ('Fulfilled', 'Pending', 'Processing');
-- CREATE TABLE bookOrders(
--   orderId serial primary key,
--   orderDate date,
--   bookId int,
--   cost decimal,
--   quantity int,
--   supplyDate date,
--   fulfillmentStatus fulfillment,
--   supplierName varchar(200),
--   FOREIGN KEY (bookId) REFERENCES books(bookId)
-- );

-- CREATE TYPE gender AS ENUM ('Female', 'Male');
-- CREATE TYPE memberstatus AS ENUM ('Active', 'Suspended');
-- CREATE TABLE members(
--   memberId serial primary key,
--   name varchar (100),
--   gender gender,
--   emailAddress varchar(100),
--   phoneNumber varchar(100),
--   address varchar(200),
--   age int,
--   typeOfMembership varchar(100),
--   dateOfMembership date,
--   status memberstatus
-- );

-- CREATE TABLE borrowHistory(
--   borrowId int primary key,
--   bookId int,
--   memberId int,
--   borrowDate date,
--   returnDate date,
--   FOREIGN KEY (memberId) REFERENCES members(memberId),
--   FOREIGN KEY (bookId) REFERENCES books(bookId)
-- );

-- CREATE TABLE departments(
--   deptId serial primary key,
--   departmentName varchar(100),
--   managerName varchar(100)
-- );

-- CREATE TABLE libraryStaff(
--   staffId serial primary key,
--   name varchar (100),
--   jobTitle varchar(100),
--   departmentId int,
--   gender gender,
--   address varchar(255),
--   phoneNumber varchar(100),
--   hireDate date,
--   managerId int,
--   FOREIGN KEY (departmentId) REFERENCES departments(deptId)
-- );

-- select * from librarystaff;

