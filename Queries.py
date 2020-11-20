from db_connection import connection, cursor

def today_movies():
    sql = "SELECT movies.name FROM shows INNER JOIN movies ON shows.movie_id = movies.id WHERE show_date = TODAY"
    cursor.execute(sql)
    connection.commit()

def today_played():
    sql = "SELECT show_date, show_time, price, movies.title FROM shows, movies WHERE DATE(show_date)=CURDATE() AND shows.movie_id=movies.id"
    cursor.execute(sql)
    connection.commit()

def most_often_played_movie_in_year():
    sql = """SELECT shows.movie_id, title, show_date,
COUNT(shows.movie_id) 
FROM shows, movies
WHERE shows.movie_id = movies.id AND shows.show_date IN (
	SELECT shows.show_date
	FROM shows
	WHERE DATE(show_date)>=DATE_SUB(NOW(),INTERVAL 1 YEAR)
	)
GROUP BY movie_id
ORDER BY movie_id DESC 
LIMIT 1"""
    cursor.execute(sql)
    connection.commit()

def taken_seats_on_show():
    sql = """    SELECT
    tickets.id
    AS
    'ticket', tickets.show_id, seats.number
    AS
    'taken seat', movies.title
    FROM
    tickets, seats, shows, movies
    # wszystkie zajęte na konkretny seans; bez ostatniego "and" wszystkie zajete miejsca na wszystkich seansach
    WHERE
    tickets.seat_id = seats.id
    and tickets.show_id = shows.id
    AND
    shows.movie_id = movies.id
    AND
    shows.id = 4
ORDER
BY
seats.id"""
    cursor.execute(sql)
    connection.commit()


