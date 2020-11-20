from db_connection import connection, cursor

def today_movies(title, description, rest_id):
    sql = "SELECT movies.name FROM shows INNER JOIN movies ON shows.movie_id = movies.id WHERE show_date = TODAY"
    cursor.execute(sql)
    connection.commit()


