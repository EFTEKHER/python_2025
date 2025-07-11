use uni;


-- create table student(
--     roll_no int primary key,
--     name varchar(50) not null,
--     marks int not null,
--     grade varchar(2) not null,
--     city varchar(50) not null
-- );

-- insert into student values
-- (6, 'John Doe', 85, 'A', 'New York'),
-- (7, 'Jane Smith', 90, 'A+', 'Los Angeles'),
-- (8, 'Alice Johnson', 78, 'B', 'Chicago'),
-- (9, 'Bob Brown', 88, 'A', 'Houston'),
-- (10, 'Charlie Davis', 92, 'A+', 'Phoenix');
-- create table department(
--     dept_id int primary key,
--     dept_name varchar(50) not null
  
-- );



-- create table teacher(
--     teacher_id int primary key,
--     name varchar(50) not null,
--     subject varchar(50) not null,
--     city varchar(50) not null,
--     dept_id int;
--     foreign key (dept_id) references department(dept_id)
-- );

-- create table eft(
--     id int primary key,
--     nam varchar(50) not null
-- );

create table x(
    id int primary key,
    nam varchar(50) not null,
    eft_id int,
    foreign key (eft_id) references eft(id)
);