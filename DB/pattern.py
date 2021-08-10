from table import Product, Sensor, Error
from db_Ops import DB_reinit, connect_DB, DB_init, close_DB, show_DB
from playhouse.postgres_ext import *
# from table_init import *
db = PostgresqlExtDatabase(
    'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


# ======== Main function ========
connect_DB()


DB_reinit()
# show_DB()

close_DB()

# ======== Method usage ========
# db.drop_tables([Query])
