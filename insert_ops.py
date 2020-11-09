from db_connection import connection, cursor
from GenerateData import GenerateData

data_generator = GenerateData()


def get_last_id(table_name):
    id_list = data_generator.GenerateForeignKeys(table_name)
    if len(id_list) > 0:
        return id_list[len(id_list) - 1]
    else:
        return 0


def insert_branch(city, address):
    sql = "INSERT INTO branches(city, address) VALUES(%s,%s)"
    values = (city, address)
    cursor.execute(sql, values)
    connection.commit()


def insert_branches(quantity):
    city_list = data_generator.GenerateCities(quantity)
    address_list = data_generator.GenerateAddresses(quantity)
    for index in range(0, quantity):
        insert_branch(city_list[index], address_list[index])

def insert_room(number, branch_id):
    sql = "INSERT INTO rooms(number, branch_id) VALUES(%s,%s)"
    values = (number, branch_id)
    cursor.execute(sql, values)
    connection.commit()

def insert_rooms(quantity):
    numbers_list = data_generator.GenerateCities(quantity)
    branches_id_list = data_generator.GenerateAddresses(quantity)
    for index in range(0, quantity):
        insert_branch(numbers_list[index], branches_id_list[index])



def insert_account(login, password, email):
    sql = "INSERT INTO accounts(login, password,email) VALUES(%s,%s,%s)"
    values = (login, password, email)
    cursor.execute(sql, values)
    connection.commit()


def insert_accounts(quantity):
    login_list = data_generator.GenerateLogins(quantity)
    password_list = data_generator.GeneratePasswords(quantity)
    email_list = data_generator.GenerateEmails(quantity)
    for l, p, e in zip(login_list, password_list, email_list):
        insert_account(l, p, e)


def insert_modifier(type, name, value):
    sql = "INSERT INTO modifiers(type, name, value) VALUES(%s,%s,%s)"
    values = (str(type), name, str(value))
    cursor.execute(sql, values)
    connection.commit()


# needs attention
# modifiers name is prefix 'mod_' with id number of given modifier
# value is 1% of randomly generated price
# might be changed according to type of modifier
def insert_modifiers(quantity):
    type_list = data_generator.GenerateBooleans(quantity)
    last_mod_id = get_last_id("modifiers")
    value_list = data_generator.GeneratePrices(quantity)
    for t, v in zip(type_list, value_list):
        last_mod_id += 1
        insert_modifier(t, "mod_" + str(last_mod_id), v * 0.01)


def insert_restriction(rest_name):
    sql = "INSERT INTO restrictions(name) VALUE(%s)"
    values = (rest_name,)
    cursor.execute(sql, values)
    connection.commit()


# restriction names source: https://en.wikipedia.org/wiki/Motion_picture_content_rating_system
def insert_restrictions():
    rest_list = ["G", "PG", "M", "R13", "R15", "R16", "R18", "RP13", "RP15", "RP18", "R"]
    for rest in rest_list:
        insert_restriction(rest)


def insert_genre(genre_name):
    sql = "INSERT INTO genres(name) VALUE(%s)"
    values = (genre_name,)
    cursor.execute(sql, values)
    connection.commit()


# data from http://files.grouplens.org/datasets/movielens/ml-latest-small-README.html
def insert_genres():
    genre_list = ["Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama",
                  "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War",
                  "Western"]
    for genre in genre_list:
        insert_genre(genre)


def insert_movie(title, description, rest_id):
    sql = "INSERT INTO movies(title, description, restriction_id) VALUES(%s,%s,%s)"
    values = (title, description, str(rest_id))
    cursor.execute(sql, values)
    connection.commit()


# for now without description
def insert_movies(quantity):
    title_list = data_generator.GenerateMovies(quantity)
    description_list = []
    rest_id_list = data_generator.GenerateNotUniqueForeignKeysList("restrictions", quantity)
    for t, r_id in zip(title_list, rest_id_list):
        insert_movie(t, "", r_id)


def insert_genre_movie(movie_id, genre_id):
    sql = "INSERT INTO genre_movie(movie_id, genre_id) VALUES(%s,%s)"
    values = (str(movie_id), str(genre_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_genre_movies(quantity):
    genre_movie_list = data_generator.GenerateUniqueGenreMovieList(quantity)
    for genre_movie in genre_movie_list:
        insert_genre_movie(genre_movie[0], genre_movie[1])
