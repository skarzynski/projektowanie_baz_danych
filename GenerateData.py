import random
from faker import Faker
from db_connection import cursor
import csv

class GenerateData:
    # fake = Faker('pl_PL')
    fake = Faker('')

    def GenerateIntegers(self, amountOfData, min=0, max=9999):
        listOfInteger = []
        for x in range(amountOfData):
            listOfInteger.append(random.randint(min, max))
        return listOfInteger

    def GeneratePrices(self, amountOfData, min=0.0, max=9999.99):
        listOfPrices = []
        for x in range(amountOfData):
            listOfPrices.append(random.uniform(min, max))
        return listOfPrices

    def GenerateBooleans(self, amountOfData):
        listOfBolleans = []
        for x in range(amountOfData):
            listOfBolleans.append(random.randint(0, 1))
        return listOfBolleans

    def GenerateCities(self, amountOfData):
        listOfCities = []
        for x in range(amountOfData):
            listOfCities.append(self.fake.city())
        return listOfCities

    def GenerateAddresses(self, amountOfData):
        listOfAddressses = []
        for x in range(amountOfData):
            listOfAddressses.append(self.fake.street_address())
        return listOfAddressses

    def GenerateDates(self, amountOfData):
        listOfDates = []
        for x in range(amountOfData):
            listOfDates.append(self.fake.date())
        return listOfDates

    def GenerateTimes(self, amountOfData):
        listOfTimes = []
        for x in range(amountOfData):
            listOfTimes.append(self.fake.time())
        return listOfTimes

    def GenerateDateTimes(self, amountOfData):
        listOfDateTimes = []
        for x in range(amountOfData):
            listOfDateTimes.append(self.fake.date_time())
        return listOfDateTimes

    def GenerateDateTimes(self, amountOfData):
        listOfDateTimes = []
        for x in range(amountOfData):
            listOfDateTimes.append(self.fake.date_time())
        return listOfDateTimes

    def GeneratePasswords(self, amountOfData):
        listOfPasswords = []
        for x in range(amountOfData):
            listOfPasswords.append(
                self.fake.password(random.randint(8, 56), self.fake.boolean(), True, self.fake.boolean(), True))
        return listOfPasswords

    def GenerateLogins(self, amountOfData):
        listOfLogins = set()
        while len(listOfLogins) < amountOfData:
            listOfLogins.add(self.fake.user_name())
        return listOfLogins

    def GenerateEmails(self, amountOfData):
        listOfEmails = set()
        while len(listOfEmails) < amountOfData:
            listOfEmails.add(self.fake.free_email())
        return listOfEmails

        def GenerateForeignKeys(self, table_name):
            sql = "SELECT id FROM " + table_name
            cursor.execute(sql)
            records = cursor.fetchall()
            id_list = []
            for string_val in records:
                id_list.append(int(string_val[0]))
            id_list.sort()
            return id_list

        def GenerateNotUniqueForeignKeysList(self, table_name, quantity):
            foreign_keys = self.GenerateForeignKeys(table_name)
            not_unique_foreign_keys_list = []
            while len(not_unique_foreign_keys_list) < quantity:
                not_unique_foreign_keys_list.append(foreign_keys[random.randint(0, len(foreign_keys) - 1)])
            return not_unique_foreign_keys_list

        def GenerateUniqueForeignKeysList(self, table_name, quantity):
            foreign_keys = self.GenerateForeignKeys(table_name)
            if len(foreign_keys) <= quantity:
                return set(foreign_keys)
            unique_foreign_keys = set()
            while len(unique_foreign_keys) < quantity:
                random_index = random.randint(0, len(foreign_keys) - 1)
                unique_foreign_keys.add(foreign_keys[random_index])
                foreign_keys.remove(foreign_keys[random_index])
            return unique_foreign_keys

        # its not random
        def GenerateMovies(self, quantity):
            movie_list = []
            with open('movies.csv') as movie_file:
                csv_reader = csv.reader(movie_file)
                for row, _ in zip(csv_reader, range(0, quantity)):
                    movie_list.append(row[1])
            return movie_list

        # risk of infinite loop
        def GenerateUniqueGenreMovieList(self, quantity):

            genre_movie = set()
            while len(genre_movie) < quantity:
                not_unique_movie_id_list = self.GenerateNotUniqueForeignKeysList("movies", quantity - len(genre_movie))
                not_unique_genre_id_list = self.GenerateNotUniqueForeignKeysList("genres", quantity - len(genre_movie))
                for movie_id, genre_id in zip(not_unique_movie_id_list, not_unique_genre_id_list):
                    genre_movie.add((movie_id, genre_id))
            return genre_movie

if __name__ == "__main__":
    generate = GenerateData()
