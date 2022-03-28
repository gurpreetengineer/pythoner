import pymongo


def mongoConnection():
    mongo_domain = 'mongodb://localhost:27017/'
    second_half = '&appname=MongoDB%20Compass&directConnection=true&ssl=false'
    mongo_connection = mongo_domain + '?readPreference=primary' + second_half
    print(mongo_connection)
    mongo_client = pymongo.MongoClient(mongo_connection)
    print(mongo_client)

    # below it will connect to existing DB but if db does not exist,
    # it will create one.
    my_db_to_be_upsert = "dbpython"
    my_database_to_add_collections = mongo_client[my_db_to_be_upsert]
    databases_list = mongo_client.list_database_names()
    print('=======', my_database_to_add_collections)
    print('=======', databases_list)
    if my_db_to_be_upsert in databases_list:
        print('This DB exists here')
    else:
        print('We got a new fella, yay!')
        my_collection = my_database_to_add_collections["newcollection"]
        print(mongo_client.list_database_names())

        my_dictionary = {'name': 'dummy user', 'age': 0,
                         'status': 'immortal', 'death': 'he is immortal 🤷'}
        print(my_database_to_add_collections.list_collection_names())

        new_row = my_collection.insert_one(my_dictionary)
        collection_of_rows = my_collection.insert_one(new_row)

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

        collection_of_rows = my_collection.insert_many(wow_such_a_big_list)

        print(collection_of_rows.inserted_ids)
    upsertRows(mongo_client, my_database_to_add_collections, my_collection)


def upsertRows(mongo_client, my_database_to_add_collections, my_collection):
    print(my_database_to_add_collections.list_collection_names())


if __name__ == '__main__':
    mongoConnection()
