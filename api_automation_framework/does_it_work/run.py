import pytest
from api_automation_framework.utils.data_readers import LoadTestData

test_data = LoadTestData.read_csv_data("/Volumes/Development/study-guide/distributed-automation-platform"
                                  "/api_automation_framework/payloads/csv_payload/customer-data.csv")

data = {
    "custname": test_data['name'],
    "custemail": test_data['email'],
    "size": test_data['size'],
    "topping": test_data['toppings'],
    "delivery": test_data['time'],
    "comments": test_data['instructions']
}
name = "Order for " + test_data['name']


if __name__ == '__main__':
    print(data['custname'])
