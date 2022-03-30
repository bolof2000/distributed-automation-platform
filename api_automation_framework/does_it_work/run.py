import pytest
from api_automation_framework.utils.data_readers import LoadTestData

data = LoadTestData.read_csv_data("api_automation_framework/payloads/csv_payload/customer-data.csv")

if __name__ == '__main__':
    print(data)
