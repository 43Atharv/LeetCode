with cte as (select *, row_number() over(partition by actor_id, director_id) as r from actordirector)

select distinct actor_id, director_id from cte where r >= 3