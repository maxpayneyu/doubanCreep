#SELECT * FROM world.t_usersindouban where pictrue_address like '%ºÓ%';
SELECT * FROM world.t_usersindouban order by cast(same as signed) desc;
#delete from world.t_usersindouban where 1=1
#select world.t_usersindouban.pictrue_address from world.t_usersindouban
select pictrue_address,count(pictrue_address) from world.t_usersindouban where same>50
group by pictrue_address order by count(pictrue_address) desc ;
select pictrue_address,count(pictrue_address) from world.t_usersindouban
group by pictrue_address order by count(pictrue_address) desc ;

#delete from world.t_usersindouban where world.t_usersindouban.id<150

select * FROM world.t_usersindouban 
#where same=50