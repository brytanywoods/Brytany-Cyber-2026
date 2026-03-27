# Importing the Request Library
import requests
try
    
    # Send a get Request to a API
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    # Convert the JSON Format to python data
    data = response.json()

    # Print the name of the first user
    print(data[0]['name'])


    # Print the name of the first user
    print(data[0]['name'])

    # Print the name of the first user
    print(data[0]['name'])

# Error Handling
except requests.exceptions.RequestException:
    print("APT error!!!")   