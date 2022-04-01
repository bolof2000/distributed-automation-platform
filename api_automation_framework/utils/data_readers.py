import json
import csv
import random
import base64
from os.path import dirname, join


class LoadTestData:

    @staticmethod
    def read_json_data(path_to_file):
        try:
            with open(path_to_file, 'r') as json_data:
                return json.load(json_data)
        except IOError:
            print("file not found")

    @staticmethod
    def read_csv_data(path_to_file):
        try:
            with open(path_to_file, 'r') as file:
                reader = csv.DictReader(file)
                return random.choice(list(reader))
        except IOError as e:
            print(e)


