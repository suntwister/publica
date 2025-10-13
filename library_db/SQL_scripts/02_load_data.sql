
INSERT INTO Authors(AuthorID, AuthorName,CountryOfOrigin, NumberOfBooksWritten) VALUES
(1,'Margaret Atwood','Canada',23),
(2,'Haruki Murakami','Japan',18),
(3,'Chimamanda Ngozi Adichie','Nigeria',7),
(4,'Elena Ferrante','Italy',12),
(5,'Salman Rushdie','India',19),
(6,'Toni Morrison','United States',11),
(7,'Gabriel García Márquez','Colombia',15),
(8,'Yuval Noah Harari','Israel',4),
(9,'Stephen King','United States',64),
(10,'J.K. Rowling','United Kingdom',14),
(11,'Agatha Christie','United Kingdom',85),
(12,'Paulo Coelho','Brazil',30),
(13,'Khaled Hosseini','Afghanistan',4),
(14,'Isabel Allende','Chile',25),
(15,'Ayn Rand','Russia',8),
(16,'Chinua Achebe','Nigeria',5),
(17,'Octavio Paz','Mexico',12),
(18,'Umberto Eco','Italy',9),
(19,'Milan Kundera','Czech Republic',8),
(20,'Kazuo Ishiguro','Japan',10);


INSERT INTO Members (MemberID,Name,Gender,EmailAddress,PhoneNumber,Address,Age,TypeOfMembership,DateOfMembership,Status)
VALUES
(1, 'Sarah Johnson', 'Female', 'sarah.johnson@email.com', '-677', '123 Oak Street Springfield IL', 28, 'Premium', '2022-01-15', 'Active'),
(2, 'Michael Chen', 'Male', 'm.chen@gmail.com', '-788', '456 Pine Avenue Chicago IL', 34, 'Standard', '2021-03-22', 'Active'),
(3, 'Emily Rodriguez', 'Female', 'emily.r@hotmail.com', '-899', '789 Maple Drive Evanston IL', 22, 'Student', '2023-09-01', 'Active'),
(4, 'David Thompson', 'Male', 'd.thompson@yahoo.com', '-1010', '321 Elm Street Naperville IL', 45, 'Premium', '2020-06-10', 'Active'),
(5, 'Lisa Wang', 'Female', 'lisa.wang@outlook.com', '-1121', '654 Cedar Lane Aurora IL', 31, 'Standard', '2022-08-18', 'Active'),
(6, 'James Miller', 'Male', 'j.miller@email.com', '-1232', '987 Birch Road Rockford IL', 29, 'Standard', '2021-11-05', 'Suspended'),
(7, 'Amanda Davis', 'Female', 'amanda.d@gmail.com', '-1343', '147 Willow Street Peoria IL', 26, 'Premium', '2023-02-14', 'Active'),
(8, 'Robert Kim', 'Male', 'robert.kim@hotmail.com', '-1444', '258 Spruce Avenue Joliet IL', 38, 'Standard', '2020-12-03', 'Active'),
(9, 'Jessica Brown', 'Female', 'j.brown@yahoo.com', '-1455', '369 Poplar Drive Waukegan IL', 24, 'Student', '2023-01-20', 'Active'),
(10, 'Christopher Lee', 'Male', 'chris.lee@outlook.com', '-1566', '741 Ash Street Schaumburg IL', 42, 'Premium', '2021-07-12', 'Active'),
(11, 'Michelle Martinez', 'Female', 'm.martinez@gmail.com', '-1677', '852 Pine Street Rockford IL', 35, 'Standard', '2022-04-25', 'Active'),
(12, 'Kevin Wilson', 'Male', 'k.wilson@hotmail.com', '-1788', '963 Oak Avenue Peoria IL', 27, 'Standard', '2023-03-18', 'Active'),
(13, 'Rachel Green', 'Female', 'r.green@yahoo.com', '-1899', '159 Maple Lane Joliet IL', 30, 'Premium', '2021-09-08', 'Active'),
(14, 'Daniel White', 'Male', 'd.white@outlook.com', '-2010', '357 Cedar Drive Waukegan IL', 33, 'Standard', '2022-01-30', 'Active'),
(15, 'Amy Taylor', 'Female', 'a.taylor@email.com', '-2121', '468 Elm Avenue Schaumburg IL', 25, 'Student', '2023-05-12', 'Active'),
(16, 'Jonathan Harris', 'Male', 'j.harris@gmail.com', '-2232', '579 Birch Street Springfield IL', 41, 'Premium', '2020-11-20', 'Active'),
(17, 'Nicole Clark', 'Female', 'n.clark@hotmail.com', '-2343', '681 Willow Avenue Chicago IL', 29, 'Standard', '2022-07-03', 'Active'),
(18, 'Matthew Lewis', 'Male', 'm.lewis@yahoo.com', '-2444', '792 Spruce Street Evanston IL', 36, 'Standard', '2021-12-15', 'Active'),
(19, 'Ashley Robinson', 'Female', 'a.robinson@outlook.com', '-2455', '814 Poplar Avenue Naperville IL', 32, 'Premium', '2022-02-28', 'Active'),
(20, 'Ryan Walker', 'Male', 'r.walker@email.com', '-2566', '925 Ash Street Aurora IL', 28, 'Standard', '2023-04-05', 'Active');


INSERT INTO Books 
(BookID, Title, AuthorID, Genre, DateOfPublication, Publisher, ISBN, Language, AvailableCopies, AgeRating)
VALUES
(1, 'The Handmaid''s Tale', 1, 'Dystopian Fiction', '1985-08-01', 'McClelland & Stewart', '9780771008795', 'English', 3, '16+'),
(2, 'Cat''s Eye', 1, 'Literary Fiction', '1988-09-01', 'McClelland & Stewart', '9780771008801', 'English', 2, '16+'),
(3, 'The Blind Assassin', 1, 'Literary Fiction', '2000-09-01', 'McClelland & Stewart', '9780771008818', 'English', 1, '18+'),
(4, 'Norwegian Wood', 2, 'Literary Fiction', '1987-09-04', 'Kodansha', '9784062748687', 'English', 2, '18+'),
(5, 'Kafka on the Shore', 2, 'Magical Realism', '2002-09-12', 'Shinchosha', '9784101001548', 'English', 3, '16+'),
(6, '1Q84', 2, 'Science Fiction', '2009-05-29', 'Shinchosha', '9784103534235', 'English', 2, '18+'),
(7, 'Americanah', 3, 'Literary Fiction', '2013-05-14', 'Knopf', '9780307271082', 'English', 4, '16+'),
(8, 'Half of a Yellow Sun', 3, 'Historical Fiction', '2006-09-12', 'Knopf', '9781400044160', 'English', 2, '18+'),
(9, 'Purple Hibiscus', 3, 'Literary Fiction', '2003-10-01', 'Algonquin Books', '9781565124271', 'English', 3, '16+'),
(10, 'My Brilliant Friend', 4, 'Literary Fiction', '2011-10-01', 'Europa Editions', '9781609450786', 'English', 2, '16+'),
(11, 'The Story of a New Name', 4, 'Literary Fiction', '2012-09-01', 'Europa Editions', '9781609451349', 'English', 1, '16+'),
(12, 'Those Who Leave and Those Who Stay', 4, 'Literary Fiction', '2013-09-01', 'Europa Editions', '9781609452339', 'English', 1, '16+'),
(13, 'Midnight''s Children', 5, 'Magical Realism', '1981-04-01', 'Jonathan Cape', '9780224020435', 'English', 1, '18+'),
(14, 'The Satanic Verses', 5, 'Literary Fiction', '1988-09-26', 'Viking', '9780670825370', 'English', 2, '18+'),
(15, 'The Moor''s Last Sigh', 5, 'Literary Fiction', '1995-09-01', 'Jonathan Cape', '9780224042864', 'English', 1, '18+'),
(16, 'Beloved', 6, 'Historical Fiction', '1987-09-01', 'Knopf', '9780394535968', 'English', 3, '18+'),
(17, 'Song of Solomon', 6, 'Literary Fiction', '1977-09-01', 'Knopf', '9780394497051', 'English', 2, '16+'),
(18, 'The Bluest Eye', 6, 'Literary Fiction', '1970-06-01', 'Holt Rinehart Winston', '9780030840357', 'English', 2, '18+'),
(19, 'One Hundred Years of Solitude', 7, 'Magical Realism', '1967-05-30', 'Harper & Row', '9780060883287', 'English', 2, '16+'),
(20, 'Love in the Time of Cholera', 7, 'Romance', '1985-09-01', 'Editorial Oveja Negra', '9788439720632', 'English', 3, '18+');

INSERT INTO BorrowHistory (BorrowedID, BookID, MemberID, BorrowDate, ReturnDate)
VALUES
(1, 1, 1, date '2024-01-15', '2024-02-05'),
(2, 2, 3, date '2024-02-10', '2024-03-02'),
(3, 20, 2,date '2024-01-22', '2024-02-12'),
(4, 15, 9, date '2024-03-05', '2024-03-25'),
(5, 7, 4, date '2024-02-18', '2024-03-10'),
(6, 14, 5, date '2024-03-12', '2024-04-01'),
(7, 19, 1, date '2024-02-20', '2024-03-15'),
(8, 13, 8, date '2024-03-01', '2024-03-21'),
(9, 18, 7, date '2024-01-28', '2024-02-17'),
(10, 16, 10, date '2024-02-25', '2024-03-18'),
(11, 10, 2, date '2024-03-10', '2024-04-05'),
(12, 17, 3, date '2024-01-08', '2024-01-28'),
(13, 12, 4, date '2024-03-15', NULL),
(14, 8, 6, date '2024-02-01', NULL),
(15, 9, 7, date '2024-03-20', NULL),
(16, 11, 11, date '2024-01-12', '2024-02-02'),
(17, 6, 12, date '2024-02-14', '2024-03-06'),
(18, 5, 13, date '2024-03-08', '2024-03-28'),
(19, 4, 14, date '2024-01-25', '2024-02-15');

INSERT INTO BookOrders (OrderID, OrderDate,BookID,Cost,Quantity,SupplyDate,FulfillmentStatus,SupplierName) VALUES
(1, date '2024-01-10',1,12.99,5, date '2024-01-18','Fulfilled','Baker & Taylor'),
(2, date '2024-01-15',20,15.95,8, date '2024-01-25','Fulfilled','Ingram Book Group'),
(3, date '2024-02-05',15,8.99,10, date '2024-02-15','Fulfilled','Scholastic'),
(4, date '2024-02-12',7,14.50,6, date '2024-02-22','Fulfilled','Random House'),
(5, date '2024-02-20',19,13.75,4, date '2024-03-02','Fulfilled','HarperCollins'),
(6, date '2024-03-01',4,16.20,3, date '2024-03-12','Fulfilled','Penguin Random House'),
(7, date '2024-03-05',15,11.99,5, date '2024-03-18','Fulfilled','Agatha Christie Ltd'),
(8, date '2024-03-10',11,10.95,7, date '2024-03-22','Pending','HarperCollins'),
(9, date '2024-03-15',10,13.99,4, date '2024-03-28','Pending','Europa Editions'),
(10, date '2024-03-20',14,12.50,6, date '2024-04-05','Pending','Doubleday'),
(11, date '2024-03-22',16,14.95,5, date '2024-04-08','Processing','Vintage Books'),
(12, date '2024-03-25',13,13.25,4, date '2024-04-10','Processing','Riverhead Books'),
(13, date '2024-01-12',12,16.75,3, date '2024-01-22','Fulfilled','Heinemann'),
(14, date '2024-01-18',17,18.99,12, date '2024-01-28','Fulfilled','Random House'),
(15, date '2024-01-25',18,17.50,8, date '2024-02-05','Fulfilled','Little Brown'),
(16, date '2024-02-01',8,22.95,6, date '2024-02-12','Fulfilled','DC Comics'),
(17, date '2024-02-08',9,19.99,10, date '2024-02-18','Fulfilled','Bantam Spectra'),
(18, date '2024-02-15',2,14.25,5, date '2024-02-25','Fulfilled','McClelland & Stewart'),
(19, date '2024-02-22',5,15.75,4, date '2024-03-05','Fulfilled','Faber & Faber'),
(20, date '2024-02-28',3,21.50,3, date '2024-03-10','Fulfilled','Knopf');

INSERT INTO Departments (DeptID, DepartmentName, ManagerName)
VALUES
(1, 'Administration', 'Jennifer Walsh'),
(2, 'Children & Youth Services', 'Rebecca Foster'),
(3, 'Reference & Research', 'Thomas Anderson'),
(4, 'Circulation', 'Maria Gonzalez'),
(5, 'Technical Services', 'Kevin O''Brien'),
(6, 'Information Technology', 'Daniel Rodriguez'),
(7, 'Security & Facilities', 'James Brown'),
(8, 'Community Programs', 'Linda Garcia');

ALTER TABLE LibraryStaff
ALTER ManagerID DROP NOT NULL;

INSERT INTO LibraryStaff (
    StaffID, Name, JobTitle, DepartmentID, Gender, Address, PhoneNumber, HireDate, ManagerID
)
VALUES
(1, 'Jennifer Walsh', 'Head Librarian', 1, 'Female', '892 Library Lane Springfield IL', '-2555', '2018-01-15', NULL),
(2, 'Mark Patterson', 'Assistant Librarian', 1, 'Male', '445 Book Street Chicago IL', '-2556', '2019-03-10', 1),
(3, 'Rebecca Foster', 'Children''s Librarian', 2, 'Female', '678 Story Avenue Evanston IL', '-2557', '2020-06-22', 1),
(4, 'Thomas Anderson', 'Reference Librarian', 3, 'Male', '234 Research Drive Naperville IL', '-2558', '2021-01-08', 1),
(5, 'Maria Gonzalez', 'Circulation Manager', 4, 'Female', '567 Checkout Lane Aurora IL', '-2559', '2019-09-15', 1),
(6, 'Kevin O''Brien', 'Technical Services Manager', 5, 'Male', '123 Catalog Street Rockford IL', '-2560', '2020-11-03', 1),
(7, 'Laura Mitchell', 'Youth Services Coordinator', 2, 'Female', '789 Teen Avenue Peoria IL', '-2561', '2021-04-18', 3),
(8, 'Daniel Rodriguez', 'IT Support Specialist', 6, 'Male', '456 Technology Road Joliet IL', '-2562', '2022-02-01', 1),
(9, 'Carol Williams', 'Acquisitions Librarian', 5, 'Female', '321 Purchase Street Waukegan IL', '-2563', '2019-07-12', 6),
(10, 'Paul Johnson', 'Security Guard', 7, 'Male', '654 Safety Lane Schaumburg IL', '-2564', '2021-08-25', 1),
(11, 'Susan Miller', 'Branch Manager', 1, 'Female', '987 Branch Road Springfield IL', '-2565', '2017-05-10', 1),
(12, 'Robert Davis', 'Interlibrary Loan Coordinator', 3, 'Male', '147 Exchange Street Chicago IL', '-2566', '2020-03-14', 4),
(13, 'Patricia Wilson', 'Adult Programming Librarian', 8, 'Female', '258 Event Avenue Evanston IL', '-2567', '2021-09-07', 1),
(14, 'James Brown', 'Maintenance Supervisor', 7, 'Male', '369 Repair Drive Naperville IL', '-2568', '2018-12-20', 1),
(15, 'Linda Garcia', 'Community Outreach Coordinator', 8, 'Female', '741 Public Lane Aurora IL', '-2569', '2020-08-11', 1),
(16, 'Michael Martinez', 'Digital Services Librarian', 6, 'Male', '852 Digital Street Rockford IL', '-2570', '2022-01-25', 8),
(17, 'Barbara Taylor', 'Collection Development Specialist', 5, 'Female', '963 Selection Avenue Peoria IL', '-2571', '2019-11-18', 6),
(18, 'William Anderson', 'Evening Supervisor', 4, 'Male', '159 Night Street Joliet IL', '-2572', '2021-06-03', 5),
(19, 'Elizabeth Thomas', 'Senior Reference Librarian', 3, 'Female', '357 Knowledge Drive Waukegan IL', '-2573', '2018-04-16', 4),
(20, 'David Jackson', 'Systems Administrator', 6, 'Male', '468 Network Lane Schaumburg IL', '-2574', '2020-10-29', 8),
(21, 'Mary White', 'Cataloging Librarian', 5, 'Female', '579 Index Street Springfield IL', '-2575', '2019-02-08', 6),
(22, 'Charles Harris', 'Part-time Librarian', 1, 'Male', '681 Flexible Avenue Chicago IL', '-2576', '2022-07-14', 2),
(23, 'Lisa Clark', 'Special Collections Librarian', 3, 'Female', '792 Archive Drive Evanston IL', '-2577', '2020-12-01', 4),
(24, 'Christopher Lewis', 'Custodial Supervisor', 7, 'Male', '814 Clean Street Naperville IL', '-2578', '2019-05-23', 14),
(25, 'Sarah Robinson', 'Volunteer Coordinator', 8, 'Female', '925 Service Lane Aurora IL', '-2579', '2021-03-17', 15);

