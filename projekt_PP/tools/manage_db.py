def return_user_db():
    return None

def return_book_db():
    return None

def return_user(uid):
    return None

def return_book(id):
    return None

import json

test_data_path = '/mnt/data/test_data_biblioteka.json'
with open(test_data_path, 'w') as json_file:
    json.dump(test_data, json_file, indent=4)

test_data_path