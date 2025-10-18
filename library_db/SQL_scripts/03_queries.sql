-- Q1 List all books published after 2015 along with their authors' names.
SELECT 
	b.title,
	authorname,
	EXTRACT(YEAR FROM dateofpublication) AS PublishedYear
FROM books b
LEFT JOIN authors a ON b.authorid = a.authorid
WHERE EXTRACT(YEAR FROM dateofpublication) > 2015;

-- Q2 Find all members who joined in the last 2 years and have a 'Premium' membership.
SELECT
	name,
	typeofmembership,
	dateofmembership AS  DateJoined
FROM members
WHERE typeofmembership = 'Premium' 
	AND dateofmembership = CURRENT_DATE - INTERVAL '2 years';


-- Q3 Display the total number of books written by each author, ordered by count (descending).
SELECT
	COUNT(b.bookid) AS TotalNoOfBooks,
	a.authorname	
FROM books b
JOIN authors a ON b.authorid = a.authorid
GROUP BY a.authorname
ORDER BY COUNT(b.bookid) DESC;


--Q4 Show all currently borrowed books (books with no return date) along with the member's name and borrow date.
SELECT
	b.title,
	m.name,
	bh.borrowdate
FROM books b
JOIN borrowhistory bh ON b.bookid = bh.bookid
JOIN members m ON bh.memberid = m.memberid
WHERE bh.returndate IS NULL;


-- Q5 List all library staff members working in the 'Circulation' department.
SELECT
	ls.name,
	d.departmentname
FROM librarystaff ls
JOIN departments d ON ls.departmentid = d.deptid
WHERE d.departmentname = 'Circulation';

-- Q6 Calculate the total cost of all book orders placed in 2024, grouped by fulfillment status.
SELECT
	fulfillmentstatus,
	SUM(cost) AS total_cost
FROM bookorders
WHERE EXTRACT(YEAR FROM orderdate) = 2024
GROUP BY fulfillmentstatus;


-- Q7 Retrieve each member’s name, the total number of books they’ve borrowed, and show only those who borrowed more than 3 books.
SELECT 
	m.name,
	count(bh.borrowedid) AS Total_books_borrowed
FROM members m
JOIN borrowhistory bh ON m.memberid = bh.memberid
GROUP BY m.name
HAVING count(bh.borrowedid) > 3
ORDER BY Total_books_borrowed DESC;


--Q8 Identify members who have never borrowed a book.
SELECT 
	m.memberid,
	m.name
FROM members m
LEFT JOIN borrowhistory bh ON m.memberid = bh.memberid
WHERE bh.memberid IS NULL;


-- Q9: Show the average number of available copies per genre.
SELECT
	genre,
	ROUND(AVG(availablecopies),2) AS Avg_Copies_Available
FROM books
GROUP BY genre
ORDER BY Avg_Copies_Available DESC;
	

-- Q10: List all books that are currently overdue (borrowed more than 30 days ago and not yet returned).
SELECT
	b.title,
	m.name,
	bh.borrowdate
FROM books b
JOIN borrowhistory bh ON b.bookid = bh.bookid
JOIN members m ON bh.memberid = m.memberid
WHERE CURRENT_DATE - bh.borrowdate > 30 AND bh.returndate IS NULL


-- Q11. Create a query that shows each department’s staff count and the average tenure (years) of staff in that department.
SELECT 
	d.departmentname,
	COUNT(ls.departmentid) AS Total_staff,
	ROUND(AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE,ls.hiredate))),2) AS Avg_Staffs_Tenure
FROM departments d
JOIN librarystaff ls ON d.deptid = ls.departmentid
GROUP BY d.departmentname
ORDER BY d.departmentname


-- Q12: Monthly borrowing trends for the past year
SELECT
	TO_CHAR(bh.borrowdate, 'YYYY-MM') AS Month_Year,
	COUNT(bh.borrowedid) AS Total_Borrowed
FROM borrowhistory bh
GROUP BY TO_CHAR(bh.borrowdate, 'YYYY-MM')
ORDER BY Month_Year


-- Q13: Authors whose books have been borrowed more than 10 times in total, along with their most popular book.
SELECT
	a.authorname,
	b.title,
	count(bh.borrowedid) AS Total_borrowed
FROM authors a
JOIN books b ON a.authorid = b.authorid
JOIN borrowhistory bh ON b.bookid = bh.bookid
GROUP BY a.authorname, b.title
HAVING COUNT(bh.borrowedid) > 10
ORDER BY a.authorname, total_borrowed DESC;


-- Q14 Calculate the total revenue from book orders per supplier, showing only suppliers with orders exceeding $5,000.
SELECT 
    bo.suppliername,
    SUM(bo.quantity * bo.cost) AS total_revenue
FROM bookorders bo
GROUP BY bo.suppliername
HAVING SUM(bo.quantity * bo.cost) > 5000
ORDER BY total_revenue DESC;

-- Q15 Identifies "inactive" members (those who haven't borrowed a book in the last 6 months) who have a Premium membership.
SELECT 
    m.memberid,
    m.name,
    m.typeofmembership
FROM members m
LEFT JOIN borrowhistory bh 
    ON m.memberid = bh.memberid
GROUP BY m.memberid, m.name, m.typeofmembership
HAVING 
    MAX(bh.borrowdate) < (CURRENT_DATE - INTERVAL '6 months')
    OR MAX(bh.borrowdate) IS NULL
    AND m.typeofmembership = 'Premium';
