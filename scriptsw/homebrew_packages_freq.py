import requests
import json
import time


def get_most_freq_home_brew_packages():
    result = []
    response = requests.get("https://formulae.brew.sh/api/formula.json")
    response_json = response.json()

    for package in response_json:
        package_name = package['name']
        package_desc = package['desc']
        package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
        r_get = requests.get(package_url)
        package_json = r_get.json()
        install_30 = package_json['analytics']['install_on_request']['30d'][package_name]
        install_90 = package_json['analytics']['install_on_request']['90d'][package_name]
        install_365 = package_json['analytics']['install_on_request']['365d'][package_name]

        data = {
            "name": package_name,
            "desc": package_desc,
            "analytics": {
                "30d": install_30,
                "90d": install_90,
                "365d": install_365
            }
        }

        result.append(data)
        time.sleep(r_get.elapsed.total_seconds())

    with open('package.json','w') as file:
        json.dump(result,file,indent=2)
    # response_str = json.dumps(package_json, indent=2)


if __name__ == '__main__':
    print(get_most_freq_home_brew_packages())
