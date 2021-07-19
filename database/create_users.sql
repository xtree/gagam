show databases;
use tnt;

create table tnt.users(
user_id INT AUTO_INCREMENT PRIMARY KEY,
user_name VARCHAR(255) NOT NULL,
password VARCHAR(200)
);
show tables;
insert into users (user_name,password) values ("victor","$5$rounds=535000$Js56pXwi0FpDv8Bp$tqhQsn7/RR3MWD.gQoG9k9tE.uQ9.YtakndMst/JoLC");
select * from users;