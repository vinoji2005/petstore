import requests

def get_endpoints(swagger_url):
    try:
        response = requests.get(swagger_url)
        if response.status_code == 200:
            swagger_data = response.json()
            paths = swagger_data.get('paths')
            if paths:
                return paths.keys()
            else:
                return []
        else:
            print(f"Failed to fetch Swagger data. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Swagger data: {e}")
        return []

if __name__ == "__main__":
    swagger_url = "http://petstore.swagger.io"
    endpoints = get_endpoints(swagger_url)
    for endpoint in endpoints:
        print(endpoint)

