from playhouse.postgres_ext import *


class Project(Model):
    project_name = CharField(primary_key=True, null=True)

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


class Pattern(Model):
    # serial_number = CharField(primary_key=True)
    id = PrimaryKeyField(null=True)
    error = CharField(null=True)
    sensor = CharField(null=True)
    query = BinaryJSONField(null=True)
    project = ForeignKeyField(Project, backref='project', null=True)

    class Meta:
        database = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)
