from copy import error
from db_Ops import DataBaseOps
from playhouse.postgres_ext import *
from table import *
db = PostgresqlExtDatabase(
    'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


# ======== Main function ========
Ops = DataBaseOps()
Ops.connect_DB()
# db.create_tables([Product, Pattern])
# Ops.restart_DB()
# Ops.init_DB()
# print(db.get_tables())
# a = Ops.update_pattern(pattern={"cool":"men"}, id = 45)
# print(a)
# Ops.delete_pattern()
Ops.show_DB()
Ops.close_DB()
# ======== Method usage ========
# db.drop_tables([Query])
