
from playhouse.postgres_ext import *
from data import ProductData, SensorData, ErrorData
from table import *

db = PostgresqlExtDatabase(
    'diagnosisDB', user="postgres", password='postgres', host='127.0.0.1', port=5487)


def connect_DB():
    global db
    if db.is_closed():
        db.connect()
        print("========== DB Connecting... ========== \n")


def close_DB():
    global db
    if not db.is_closed():
        db.close()
        print("\n========== DB Closed ========== ")


def show_DB():
    print("---------- Product Table ----------\n")
    for product in Product.select():
        print(f'{product.product_id} | {product.product_type}')
    print()
    print("---------- Sensor Table ----------\n")
    for sensor in Sensor.select():
        print(f'{sensor.sensor_id} | {sensor.sensor_type}')
    print()
    print("---------- Error Table ----------\n")
    for error in Error.select():
        print(
            f'{error.error} | {error.sensor.sensor_type} | {error.product.product_type}')
    print()
    print("DB Tables: ", db.get_tables())


def DB_init():
    global db
    products = ProductData()
    sensors = SensorData()
    errors = ErrorData()

    for product_type in products.product_types:
        product = Product.get_or_create(product_type=product_type)

    for sensor_type in sensors.sensor_types:
        sensor = Sensor.get_or_create(sensor_type=sensor_type)

    for error_type, sensor_type, product_type in errors.error_types:
        sensor = Sensor.get_or_none(Sensor.sensor_type == sensor_type)

        if product_type == 'all':
            for product in Product.select():
                error = Error.get_or_create(
                    error=error_type, sensor=sensor, product=product)


def DB_reinit():
    global db
    db.drop_tables([Product, Sensor, Error])
    if db.get_tables() == []:
        print("DB Reset done.")
    db.create_tables([Product, Sensor, Error])
    DB_init()


def DB_show(table):
    pass
