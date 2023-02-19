from pymongo import MongoClient


class DataBase:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.client = self.connect()

    def connect(self):
        self.client = MongoClient(self.connection_string)
        return self.client

    def database_and_collection(self, DataBase_section_name):
        database_name = self.client['trado_qa']
        collection = database_name[DataBase_section_name]
        return collection


class Main(DataBase):
    CONNECTION_STRING = "mongodb+srv://qa_agency:veHt1JK5@cluster0.qnr3p.mongodb.net/trado_qa?retryWrites=true&w=majority"


def login_code_Generating_query(phone_number):
    string_connection = Main.CONNECTION_STRING
    user = DataBase(string_connection)
    collection = user.database_and_collection('users')
    query = collection.find_one({'phone': f'{phone_number}'})
    sms_code = query['loginCode']
    return sms_code


def query_for_products_details(col, product_name, key):
    string_connection = Main.CONNECTION_STRING
    user = DataBase(string_connection)
    collection = user.database_and_collection(f'{col}')
    query = collection.find_one({'name': f'{product_name}'})
    value = query[f'{key}']
    return str(value)


def query_for_products_with_2_keys(col, prod_name, key, key2):
    string_connection = Main.CONNECTION_STRING
    user = DataBase(string_connection)
    collection = user.database_and_collection(f'{col}')
    query = collection.find_one({'name': prod_name})
    value = query[key]
    return value[key2]
