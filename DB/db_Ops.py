
from copy import error
from operator import mod
from peewee import query_to_string
from playhouse.postgres_ext import *
from beautifultable import BeautifulTable
from data import ProductData, ErrorData
import json
from table import *


class DataBaseOps():
    def __init__(self) -> None:
        self.db = PostgresqlExtDatabase(
            'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)

    def connect_DB(self):
        if self.db.is_closed():
            self.db.connect()
            print("========== DB Connecting... ========== \n")

    def close_DB(self):
        if not self.db.is_closed():
            self.db.close()
            print("\n========== DB Closed ========== ")

    def show_DB(self):
        project_table = BeautifulTable()
        pattern_table = BeautifulTable()

        print("---------- Product Table ----------\n")
        project_table.rows.append(["project name"])
        for product in Project.select():
            project_table.rows.append(
                [product.project_name])
        print(project_table)
        print()
        print("---------- Pattern Table ----------\n")
        pattern_table.rows.append(
            ["id", "error", "sensor", 'query', 'project'])
        for pattern in Pattern.select():
            pattern_table.rows.append(
                [pattern.id, pattern.error, pattern.sensor, pattern.query, pattern.project])
        print(pattern_table)
        print()
        print("DB Tables: ", self.db.get_tables())

    def get_pattern(self, project=None, sensor=None, error=None):
        '''
        get_pattern(project='ambrose', sensor='fan', error='IERR')
        pattern_list is a bounch of pattern select objects with id, error, sensor, query, project..
        '''
        pattern_list = []
        # List all pattern
        if project == None and sensor == None and error == None:
            for pattern in Pattern.select():
                pattern_list.append(pattern)

        elif project:
            if sensor:
                if error:
                    for pattern in Pattern.select().where(Pattern.project == project, Pattern.sensor == sensor, Pattern.error == error):
                        pattern_list.append(pattern)
                else:
                    for pattern in Pattern.select().where(Pattern.project == project, Pattern.sensor == sensor):
                        pattern_list.append(pattern)
            elif error:
                for pattern in Pattern.select().where(Pattern.project == project, Pattern.error == error):
                    pattern_list.append(pattern)
            else:
                for pattern in Pattern.select().where(Pattern.project == project):
                    pattern_list.append(pattern)
        elif sensor:
            if error:
                for pattern in Pattern.select().where(Pattern.sensor == sensor, Pattern.error == error):
                    pattern_list.append(pattern)
            else:
                for pattern in Pattern.select().where(Pattern.sensor == sensor):
                    pattern_list.append(pattern)
        else:
            return "Invalid Input."
        return pattern_list

    def update_pattern(self, pattern, project=None, sensor=None, error=None, id=None):
        # Directly update by exist id
        id_exist = Pattern.get_or_none(id=id)
        if id_exist:
            query = Pattern.update(query=pattern).where(Pattern.id == id)
            query.execute()

        if (not pattern) or (not project) or (not sensor) or (not error):
            return "Incomplete input."

        project_exist = Project.get_or_none(project_name=project)
        error_exist = Pattern.get_or_none(
            project=project, sensor=sensor, error=error)

        if not project_exist:
            new_project = Project.get_or_create(
                project_name=project)

        if error_exist:
            query = Pattern.update(query=pattern).where(
                Pattern.project == project, Pattern.sensor == sensor, Pattern.error == error)
        else:
            new_pattern = Pattern.get_or_create(
                project=project, sensor=sensor, error=error, query=pattern)

        return "200"

    def delete_pattern(self, id=None):
        if id:
            del_pattern = Pattern.delete().where(Pattern.id == id)
            return
        return

    def restart_DB(self):
        print("Before drop: ", self.db.get_tables())
        self.db.drop_tables([Project, Pattern], cascade=True)
        print("Empty: ", self.db.get_tables())
        self.db.create_tables([Project, Pattern])
        print("Table restart: ", self.db.get_tables())

    def init_DB(self):
        errors = ErrorData()
        products = ProductData()

        for model_data in products.product_types:
            model = Project.get_or_create(project_name=model_data)
        for error_data, sensor_data, query_data in errors.error_data:
            for project in Project.select():
                pattern = Pattern.get_or_create(
                    error=error_data, sensor=sensor_data, query=query_data, project=project)
