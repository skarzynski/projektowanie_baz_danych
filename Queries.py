from db_connection import connection, cursor


def today_movies(date="2020-11-04"):
    sql = "SELECT movies.title FROM shows INNER JOIN movies ON shows.movie_id = movies.id WHERE shows.show_date = " + date
    cursor.execute(sql)
    return cursor.fetchall()


def today_played():
    sql = "SELECT show_date, show_time, price, movies.title FROM shows, movies WHERE DATE(show_date)=CURDATE() AND shows.movie_id=movies.id"
    cursor.execute(sql)
    return cursor.fetchall()


def most_often_played_movie_in_year():
    sql = """SELECT shows.movie_id, movies.title, shows.show_date,
                COUNT(shows.movie_id) AS times_played
                FROM shows, movies
                WHERE shows.movie_id = movies.id AND shows.show_date IN (
                    SELECT shows.show_date
                    FROM shows
                    WHERE DATE(show_date)>=DATE_SUB(NOW(),INTERVAL 1 YEAR)
                    )
                GROUP BY movie_id
                ORDER BY times_played DESC
                LIMIT 1;"""
    cursor.execute(sql)
    return cursor.fetchall()


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
    return cursor.fetchall()


def movie_with_highest_income():
    sql = "select movies.title, SUM(IF(modifiers.type = 0, modifiers.value * shows.price,shows.price -modifiers.value )) as earnings FROM tickets,modifiers,shows,movies WHERE tickets.modifier_id = modifiers.id and tickets.show_id = shows.id and shows.movie_id = movies.id"
    cursor.execute(sql)
    return cursor.fetchall()


def average_price_of_ticket_in_this_month():
    sql = """SELECT
    AVG(shows.price)
    AS
    "average price this month"
    FROM
    shows
    where
    shows.show_date
    IN(
        SELECT
    shows.show_date
    FROM
    shows
    WHERE
    DATE(show_date) >= DATE_SUB(NOW(), INTERVAL
    1
    MONTH)
    )"""
    cursor.execute(sql)
    return cursor.fetchall()


def account_with_highest_income_for_cinema():
    sql = """select
    accounts.login, SUM(IF(modifiers.type = 0, modifiers.value * shows.price, shows.price - modifiers.value )) as earnings FROM
    tickets, modifiers, shows, accounts
    WHERE
    tickets.modifier_id = modifiers.id and tickets.show_id = shows.id and tickets.account_id = accounts.id"""
    cursor.execute(sql)
    return cursor.fetchall()


def top3_genres_in_year(year = "2020"):
    sql = f"""SELECT GenresList.Genre, COUNT(GenresList.Genre) AS CountValue
    FROM ((
	    SELECT genres.name AS Genre, tickets.id, shows.show_date
	    FROM ((movies INNER JOIN (genres INNER JOIN genre_movie ON genres.id = genre_movie.genre_id) ON movies.id = genre_movie.movie_id) INNER JOIN shows ON movies.id = shows.movie_id) INNER JOIN tickets ON shows.id = tickets.show_id
	    GROUP BY genres.name, tickets.id, shows.show_date
	    HAVING (YEAR(shows.show_date)={ year })) AS GenresList
    )
    GROUP BY GenresList.Genre
    ORDER BY CountValue DESC
    LIMIT	3"""
    cursor.execute(sql)
    return cursor.fetchall()


def branches_with_highest_income_for_cinema():
    sql = """select
    branches.city, branches.address, SUM(
        IF(modifiers.type = 0, modifiers.value * shows.price, shows.price - modifiers.value )) as earnings FROM
    tickets, modifiers, shows, branches, rooms, room_show
    WHERE
    tickets.modifier_id = modifiers.id and tickets.show_id = shows.id and shows.id = room_show.show_id and room_show.room_id = rooms.id and rooms.branch_id = branches.id"""
    cursor.execute(sql)
    return cursor.fetchall()
