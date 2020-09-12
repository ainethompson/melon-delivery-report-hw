# https://gist.github.com/seemaullal/fe8359de8e6ffc346f4478c65b065f6e
# Diagram: https://docs.google.com/drawings/d/12Toy2SaoP5I8DLk74Cr9FQSwg4mld_etrYLur2RK-JQ/edit

# - Who acted in Legally Blonde (2001)?
SELECT  Movie_table.movie_id,
        People.people_name

# Join 3 tables: https://www.w3schools.com/sql/sql_join_inner.asp
FROM ((movie_table 
    JOIN People_role_per_movie
      USING (movie_id))
        JOIN People
            USING (people_id)); 

WHERE movie_table.title IS 'Legally Blonde'



# - What are the 10 most recent movies that Meryl Strep starred in?

SELECT Movie_table.title

FROM Movie_table
    JOIN People_role_per_movie
        JOIN People

WHERE People.people_name IS 'Meryl Streep'