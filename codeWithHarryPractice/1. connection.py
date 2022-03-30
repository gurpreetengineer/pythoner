import pymongo
# from pymongo.objectid import ObjectId

# from bson import ObjectId


class MongoDb:
    def __init__(self):
        pass
        self.name_of_our_database = None
        self.name_of_our_collection = None
        self.collection = None
        self.collection_data = None

    def db_connection(self):
        try:
            print('we are in')
            DB_CLIENT = pymongo.MongoClient(
                'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false')
            self.name_of_our_database = 'codeWithHarryPractice'
            self.name_of_our_collection = 'sample_collection'
            print('---', self.name_of_our_database)
            print('---', self.name_of_our_collection)

            db = DB_CLIENT[self.name_of_our_database]
            self.collection = db[self.name_of_our_collection]
            print('try end', db, ' ====== ', self.collection)
        except Exception as ex:
            print('[EXCEPTION] ', ex)

    def insertion(self, document):
        print(type(document) is dict, type(document) is list)
        if type(document) is dict:
            print('I got a dictionary')
            self.collection.insert_one(document)
        elif type(document) is list:
            print('I got a list')
            self.collection.insert_many(document)

    def find_docs(self, condition={}, which_columns={}):
        self.collection_data = self.collection.find(condition, which_columns)
        self.print_data()

    def print_data(self):
        for data in self.collection_data:
            print(data)


if __name__ == '__main__':
    instance_one = MongoDb()
    my_dictionary = {'name': 'dummy user', 'age': 0,
                     'status': 'immortal', 'death': 'he is immortal 🤷'}
    wow_such_a_big_list = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"},
        {"name": "Betty", "address": "Green Grass 1"},
        {"name": "Richard", "address": "Sky st 331"},
        {"name": "Susan", "address": "One way 98"},
        {"name": "Vicky", "address": "Yellow Garden 2"},
        {"name": "Ben", "address": "Park Lane 38"},
        {"name": "William", "address": "Central st 954"},
        {"name": "Chuck", "address": "Main Road 989"},
        {"name": "Viola", "address": "Sideway 1633"}
    ]
    # print('===', instance_one)
    instance_one.db_connection()
    # instance_one.insertion(my_dictionary)
    # instance_one.insertion(wow_such_a_big_list)

    # on_the_basis_of = {'_id': ObjectId('62440a1060d3ec21200b23c6')}
    instance_one.find_docs()
