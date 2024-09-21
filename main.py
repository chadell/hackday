import requests

def get_user_input():
    user_input = input("Enter some data: ")
    return user_input

def make_api_request(data):
    url = "https://api.example.com/data"
    response = requests.post(url, json={"data": data})
    return response.json()

def evaluate_response(response):
    if response.get("status") == "success":
        print("API request was successful!")
    else:
        print("API request failed.")

def main():
    user_data = get_user_input()
    api_response = make_api_request(user_data)
    evaluate_response(api_response)

if __name__ == "__main__":
    main()
