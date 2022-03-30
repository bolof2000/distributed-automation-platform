from locust import HttpUser, task, constant, SequentialTaskSet, log
from data_readers import LoadTestData
import logging
import pdb

class MySeqTask(SequentialTaskSet):

    @task
    def place_order(self):
        test_data = LoadTestData.read_csv_data("/Volumes/Development/study-guide/distributed-automation-platform/api_automation_framework/payloads/csv_payload/customer-data.csv")
        print(test_data)

        data = {
            "custname": test_data['name'],
            "custemail": test_data['email'],
            "size": test_data['size'],
            "topping": test_data['toppings'],
            "delivery": test_data['time'],
            "comments": test_data['instructions']
        }

        name = "Order for " + test_data['name']

        with self.client.post("/post", catch_response=True, name=name, data=data) as response:
            if response.status_code == 200 and test_data['name'] in response.text:
                response.success()
            else:
                response.failure("Failure in processing the order")


class MyLoadTest(HttpUser):
    host = "https://httpbin.org"
    tasks = [MySeqTask]
    wait_time = constant(1)
