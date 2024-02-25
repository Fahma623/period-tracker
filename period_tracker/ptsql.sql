drop table if exists flow.user;

create table flow.user(id varchar(10) primary key,username varchar(25) not null,password varchar(25),age int,dateofbirth datetime);
insert into flow.user values(1,'Angel','Angel123',20,'2003-01-01 00:00:00');
insert into flow.user values(2,'Fiya','Fiya123',21,'2002-01-01 00:00:00');
select * from flow.user;
DROP TABLE IF EXISTS flow.period;

CREATE TABLE flow.period (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    start_date date,
    end_date date);
insert into flow.period (user_id, start_date, end_date)
values
    (1, '2023-01-01', '2023-01-10'),
    (2, '2023-02-15', '2023-02-25');

select * from flow.period;



