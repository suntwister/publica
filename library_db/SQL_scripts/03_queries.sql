-- Q1 List all books published after 2015 along with their authors' names.
SELECT
    title,
    EXTRACT(YEAR FROM dateofpublication) AS published_year
FROM books
WHERE EXTRACT(YEAR FROM dateofpublication) > 2015;

-- Q2 Find all members who joined in the last 2 years and have a 'Premium' membership.
SELECT
	memberid,
	name,
	typeofmembership,
	dateofmembership
FROM members
WHERE EXTRACT(YEAR FROM dateofmembership) >= 2023
	AND typeofmembership = 'Premium';

-- Q3 Display the total number of books written by each author, ordered by count (descending).
SELECT
    authorname,
    numberofbookswritten
FROM authors
ORDER BY numberofbookswritten DESC;


-- Q4 Show all currently borrowed books (books with no return date) along with the member's name and borrow date.
SELECT
    b.title AS book_title,
    m.name AS member_name,
    bh.borrowdate
FROM borrowhistory bh
JOIN books b ON bh.bookid = b.bookid
JOIN members m ON bh.memberid = m.memberid
WHERE bh.returndate IS NULL;

-- Q5 List all library staff members working in the 'Circulation' department.
SELECT
    s.staffid,
    s.name AS staff_name,
    s.jobtitle,
    d.departmentname
FROM librarystaff s
JOIN departments d 
    ON s.departmentid = d.deptid
WHERE d.departmentname = 'Circulation';


-- Q6 Calculate the total cost of all book orders placed in 2024, grouped by fulfillment status.
SELECT
    fulfillmentstatus,
    SUM(cost) AS total_cost_2024
FROM bookorders
WHERE EXTRACT(YEAR FROM orderdate) = 2024
GROUP BY fulfillmentstatus;

-- Q7 Find the top 5 most borrowed books along with the number of times each has been borrowed.
SELECT
    b.title,
    COUNT(bh.bookid) AS times_borrowed
FROM borrowhistory bh
JOIN books b ON bh.bookid = b.bookid
GROUP BY b.title
ORDER BY times_borrowed DESC
LIMIT 5;

-- Q8 Identify members who have never borrowed a book.
SELECT
    m.memberid,
    m.name,
    m.typeofmembership
FROM members m
LEFT JOIN borrowhistory bh 
    ON m.memberid = bh.memberid
WHERE bh.memberid IS NULL;

select * from bookorders;
-- Q9. Show the average number of available copies per genre
SELECT
    genre,
    ROUND(AVG(availablecopies), 2) AS avg_available_copies
FROM books
GROUP BY genre
ORDER BY avg_available_copies DESC;

-- Q10. List all books that are currently overdue (borrowed more than 30 days ago with no return date)
SELECT
    b.title,
    m.name AS member_name,
    bh.borrowdate
FROM borrowhistory bh
JOIN books b ON bh.bookid = b.bookid
JOIN members m ON bh.memberid = m.memberid
WHERE bh.returndate IS NULL
  AND bh.borrowdate < CURRENT_DATE - INTERVAL '30 days'
ORDER BY bh.borrowdate;

--  


