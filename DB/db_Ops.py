
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
        product_table = BeautifulTable()
        pattern_table = BeautifulTable()

        print("---------- Product Table ----------\n")
        product_table.rows.append(["product_id", "product name"])
        for product in Product.select():
            product_table.rows.append(
                [product.product_id, product.product_name])
        print(product_table)
        print()
        print("---------- Pattern Table ----------\n")
        pattern_table.rows.append(
            ["id", "error", "sensor", 'query', 'product'])
        for pattern in Pattern.select():
            pattern_table.rows.append(
                [pattern.id, pattern.error, pattern.sensor, pattern.query, pattern.product])
        print(pattern_table)
        print()
        print("DB Tables: ", self.db.get_tables())

    # def get_pattern(self, model=None, sensor=None):
    #     pattern_list = []
    #     if model == None and sensor == None:
    #         for error in Error.select():
    #             pattern_list.append(error.query)
    #     elif sensor != None:
    #         for error in Error.select().where(Error.sensor == sensor.lower()):
    #             pattern_list.append(error.query)
    #     elif model != None:
    #         for model in Product.select().where(Product.model == model):
    #             pattern_list.append(model.error.query)
    #     return pattern_list

    # def update_pattern(self, pattern, error=None, sensor=None, model=None):
    #     error_exist = Error.get_or_none(error=error)
    #     model_exist = Product.get_or_none(model=model)
    #     # 純 Update
    #     if error_exist:
    #         query = Error.update(query=pattern).where(Error.error == error)
    #         query.execute()
    #     else:
    #         if sensor == None:
    #             return "Missing sensor field."
    #         error = Error.get_or_create(
    #             error=error, sensor=sensor, query=pattern)
    #     # if user input model
    #     if model != None:
    #         if error == None:
    #             return "Missing error field."
    #         error = Error.select().where(Error.error == error)
    #         if model_exist:  # Exist model
    #             query = Product.update(error=error).where(
    #                 Product.model == model)
    #             query.execute()
    #         else:  # New model
    #             Product.get_or_create(model=model, error=error)

        #     # Error not specify, sensor not specify
        # if error == None and sensor == None:
        #     error = Error.get_or_create(
        #         error=error, sensor=sensor, query=pattern)
        # if error_exist:
        #     query = Error.update(query=pattern).where(Error.error == error)
        #     query.execute()
        # if sensor_exist:
        #     query = Error.update(query=pattern).where(Error.sensor == sensor)
        #     query.execute()

        # if model_exist == None and error_exist != None:
        #     Product.create(model=model, error=error)
        # elif error_exist

        # error_exist = Error.get_or_none(error=error)
        # sensor_exist = Error.get_or_none(sensor=sensor)
        # model_exist = Product.get_or_none(model=model)

        # elif error != None:
        #     pass
        # elif sensor != None:
        #     pass
        # elif model != None:
        #     pass

        #     if error_exist != None:
        #         query = Error.update(query=pattern).where(Error.error == error)
        #         query.execute()
        #     else:
        #         Error.get_or_create(
        #             error=error, sensor=sensor, query=pattern)

    def restart_DB(self):
        print("Before drop: ", self.db.get_tables())
        self.db.drop_tables([Product, Pattern], cascade=True)
        print("Empty: ", self.db.get_tables())
        self.db.create_tables([Product, Pattern])
        print("Table restart: ", self.db.get_tables())

    def init_DB(self):
        errors = ErrorData()
        products = ProductData()

        for model_data in products.product_types:
            model = Product.get_or_create(product_name=model_data)
        for error_data, sensor_data, query_data in errors.error_data:
            for product in Product.select():
                pattern = Pattern.get_or_create(
                    error=error_data, sensor=sensor_data, query=query_data, product=product)