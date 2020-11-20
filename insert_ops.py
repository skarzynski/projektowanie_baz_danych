from db_connection import connection, cursor
from GenerateData import GenerateData
import datetime

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
    values = (str(number), str(branch_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_rooms(quantity):
    rooms_BranchesID = data_generator.GenerateUniqueRoomsBranchesIDList(quantity)
    for room_Branch_Id in rooms_BranchesID:
        insert_room(room_Branch_Id[0], room_Branch_Id[1])


def insert_row(number, room_id):
    sql = "INSERT INTO rows(number, room_id) VALUES(%s,%s)"
    values = (str(number)[:1], str(room_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_rows(quantity):
    rows_RoomsID = data_generator.GenerateUniqueRowsRoomsIDList(quantity)
    for row_Room_Id in rows_RoomsID:
        insert_row(row_Room_Id[0], row_Room_Id[1])


def insert_seat(number, vip, row_id):
    sql = "INSERT INTO seats(number, vip, rows_id) VALUES(%s,%s,%s)"
    values = (str(number), str(vip), str(row_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_seats(quantity):
    seats_RowID = data_generator.GenerateUniqueRowsRoomsIDList(quantity)
    vips = data_generator.GenerateBooleans(quantity)
    for seat_Row_Id, vip in zip(seats_RowID, vips):
        insert_seat(seat_Row_Id[0], vip, seat_Row_Id[1])


def insert_show(show_date, show_time, price, movie_id):
    sql = "INSERT INTO shows(show_date, show_time, price, movie_id) VALUES(%s,%s,%s,%s)"
    values = (str(show_date), str(show_time), str(price), str(movie_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_shows(quantity):
    dates = data_generator.GenerateDates(quantity)
    times = data_generator.GenerateTimes(quantity)
    prices = data_generator.GeneratePrices(quantity)
    movies_ids = data_generator.GenerateNotUniqueForeignKeysList("movies", quantity)
    for d, t, p, m_id in zip(dates, times, prices, movies_ids):
        insert_show(d, t, p, m_id)


def insert_room_show(room_id, show_id):
    sql = "INSERT INTO room_show(room_id, show_id) VALUES(%s,%s)"
    values = (str(room_id), str(show_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_room_shows(quantity):
    room_show_list = data_generator.GenerateUniqueRoomShowList(quantity)
    for room_show in room_show_list:
        insert_room_show(room_show[0], room_show[1])


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
    values = (title[:50], description, str(rest_id))
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


def insert_ticket(show_id, seat_id, modifier_id, account_id, email):
    sql = "INSERT INTO tickets(show_id, seat_id, modifier_id, account_id, email) VALUES(%s,%s,%s,%s,%s)"
    values = (str(show_id), str(seat_id), str(modifier_id), str(account_id), email)
    cursor.execute(sql, values)
    connection.commit()


def insert_tickets(quantity):
    shows_id_list = data_generator.GenerateNotUniqueForeignKeysList("shows", quantity)
    seats_id_list = data_generator.GenerateNotUniqueForeignKeysList("seats", quantity)
    modifiers_id_list = data_generator.GenerateNotUniqueForeignKeysList("modifiers", quantity)
    accounts_id_list = data_generator.GenerateNotUniqueForeignKeysList("accounts", quantity)
    emails_list = data_generator.GenerateEmails(quantity)
    data_generator.AddNullstoList(30, accounts_id_list)
    for sh, se, m, a, e in zip(shows_id_list, seats_id_list, modifiers_id_list, accounts_id_list, emails_list):
        if a is None:
            a = ""
        else:
            e = ""
        insert_ticket(sh, se, m, a, e)


def insert_discount(name, mod_id):
    sql = "INSERT INTO discounts(name, modifier_id) VALUES(%s,%s)"
    values = (name, str(mod_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_discounts(quantity):
    mod_id_list = data_generator.GenerateUniqueForeignKeysList("modifiers", quantity)
    last_disc_id = get_last_id("discounts")
    for mod_id in mod_id_list:
        last_disc_id += 1
        insert_discount("disc_" + str(last_disc_id), mod_id)


def insert_subscription(name, description, mod_id):
    sql = "INSERT INTO subscriptions(name, description, modifier_id) VALUES(%s,%s,%s)"
    values = (name, description, str(mod_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_subscriptions(quantity):
    last_sub_id = get_last_id("subscriptions")
    description = ""
    mod_id_list = data_generator.GenerateUniqueForeignKeysList("modifiers", quantity)
    for mod_id in mod_id_list:
        last_sub_id += 1
        insert_subscription("sub_" + str(last_sub_id), "", mod_id)


def insert_account_subscription(purchase_date, expire_date, account_id, subscription_id):
    sql = "INSERT INTO account_subscription(purchase_date, expire_date, account_id, subscription_id) VALUES(%s,%s,%s,%s)"
    values = (str(purchase_date), str(expire_date), str(account_id), str(subscription_id))
    cursor.execute(sql, values)
    connection.commit()


def insert_account_subscriptions(quantity):
    account_subscription_list = data_generator.GenerateUniqueAccountsSubscriptionIdList(quantity)
    purchase_date_list = data_generator.GenerateDates(quantity)
    for p_date, acc_sub in zip(purchase_date_list, account_subscription_list):
        e_date = datetime.datetime.strptime(p_date, "%Y-%m-%d").date()
        e_date += datetime.timedelta(days=31)
        insert_account_subscription(p_date, e_date, acc_sub[0], acc_sub[1])


if __name__ == "__main__":
    generate = GenerateData()
    insert_accounts(100)
    insert_branches(20)
    insert_genres()
    insert_modifiers(15)
    insert_discounts(15)
    insert_restrictions()
    insert_movies(100)
    insert_genre_movies(200)
    insert_rooms(50)
    insert_rows(50)
    insert_seats(10000)
    insert_shows(3000)
    insert_room_shows(3000)
    insert_subscriptions(5)
    insert_account_subscriptions(20)
    insert_tickets(10000)
