import random
from faker import Faker
class GenerateData:
    # fake = Faker('pl_PL')
    fake = Faker('')
    def GenerateIntegers(self, amountOfData, min = 0, max = 9999):
        listOfInteger = []
        for x in range(amountOfData):
            listOfInteger.append(random.randint(min,max))
        return listOfInteger

    def GeneratePrices(self, amountOfData, min = 0.0, max = 9999.99):
        listOfPrices = []
        for x in range(amountOfData):
            listOfPrices.append(random.uniform(min,max))
        return listOfPrices


    def GenerateBooleans(self, amountOfData):
        listOfBolleans = []
        for x in range(amountOfData):
            listOfInteger.append(random.randint(0,1))
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
            listOfPasswords.append(self.fake.password(random.randint(8,56), self.fake.boolean(), True, self.fake.boolean(), True))
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


if __name__ == "__main__":
    generate = GenerateData()
    print(generate.GenerateEmails(100))