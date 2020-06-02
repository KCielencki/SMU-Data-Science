SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
FROM
	employees e
JOIN
	salaries s on e.emp_no = s.emp_no

SELECT
	first_name,
	last_name,
	hire_date
FROM
	employees
WHERE
	hire_date > 31413

SELECT
	dm.dept_no,
	d.dept_name,
	dm.emp_no,
	e.first_name,
	e.last_name
FROM
	dept_manager dm
JOIN
	departments d on dm.dept_no = d.dept_no
	JOIN employees e on dm.emp_no = e.emp_no

SELECT
	e.emp_no,
	e.first_name,
	e.last_name,
	d.dept_name
FROM
	employees e
JOIN
	dept_emp de on e.emp_no = de.emp_no
	JOIN departments d on de.dept_no = d.dept_no

SELECT
	first_name,
	last_name,
	sex
FROM
	employees
WHERE
	first_name = 'Hercules'
AND
	last_name LIKE 'B%'

SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	employees e
JOIN
	dept_emp de on e.emp_no = de.emp_no
	JOIN departments d on de.dept_no = d.dept_no
WHERE
	de.dept_no = 'd001'

SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	employees e
JOIN
	dept_emp de on e.emp_no = de.emp_no
	JOIN departments d on de.dept_no = d.dept_no
WHERE
	de.dept_no = 'd001'
OR
	de.dept_no = 'd005'

SELECT
   last_name,
   COUNT(last_name) AS "name_count"
FROM
	employees
GROUP BY
	last_name
ORDER BY
	"name_count" DESC;