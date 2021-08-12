from playhouse.postgres_ext import *


class Model(Model):

    Model_name = CharField(primary_key=True, null=True)

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


class Pattern(Model):
    # serial_number = CharField(primary_key=True)
    id = PrimaryKeyField(null=True)
    error = CharField(null=True)
    sensor = CharField(null=True)
    query = BinaryJSONField(null=True)
    product = ForeignKeyField(Model, backref='product', null=True)

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)
