from playhouse.postgres_ext import *

# =================== Model Class ======================


class Product(Model):  # SV300G3
    product_id = PrimaryKeyField(null=True)
    product_type = CharField(null=True)

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


class Sensor(Model):  # CPU, FAN ...
    sensor_id = PrimaryKeyField(null=True)
    sensor_type = CharField(null=True)

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


class Error(Model):
    error = CharField()
    sensor = ForeignKeyField(Sensor, backref='errors', null=True)
    product = ForeignKeyField(Product, backref='errors', null=True)
    query_string = JSONField(default='')

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)
