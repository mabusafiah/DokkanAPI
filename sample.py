import requests

def main():
    url = 'https://jsonplaceholder.typicode.com/posts/1'  # Example API endpoint

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        print("Received JSON data:")
        print(data)
    else:
        print(f"Request failed with status code: {response.status_code}")

if __name__ == "__main__":
    main()
