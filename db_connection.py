import mysql.connector as db
from config import DATABASE as DB_CONF

connection = db.connect(
    host=DB_CONF['HOST'],
    user=DB_CONF['USER'],
    passwd=DB_CONF['PASSWORD'],
    database=DB_CONF['DATABASE']
)

cursor = connection.cursor()
