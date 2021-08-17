from copy import error
from db_Ops import DataBaseOps
from playhouse.postgres_ext import *
from query_sender import QuerySender
from table import *
from error_reporter import ErrorReporter
db = PostgresqlExtDatabase(
    'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


# ======== Main function ========
Ops = DataBaseOps()
Ops.connect_DB()
# db.create_tables([Product, Pattern])
# Ops.restart_DB()
# Ops.init_DB()
# Ops.delete_pattern()

pattern_list = Ops.get_pattern(project="ambrose")
sender = QuerySender(pattern_list)
sender.conditional_filter(PN="ambrose")
sender.multi_error_query()
response = sender.send_query()
reporter = ErrorReporter(response, pattern_list)
reporter.error_recorder()
reporter.show_error()


# Ops.show_DB()
Ops.close_DB()
# ======== Method usage ========
# db.drop_tables([Query])
