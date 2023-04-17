import requests
import json
import csv

# Set the URL and credentials for the CER API
url = "https://<cer-publisher-ip>/cerapi/"
username = "<cer-username>"
password = "<cer-password>"

# Read the CSV file and loop through each row
with open('erls.csv', newline='') as csvfile:
    erls_reader = csv.DictReader(csvfile)
    for row in erls_reader:
        # Define the API request payload using the current row values
        payload = {
            "erl_name": row['erl_name'],
            "location_name": row['location_name'],
            "alias_1": row['alias_1'],
            "alias_2": row['alias_2'],
            "city": row['city'],
            "state": row['state'],
            "zip_code": row['zip_code'],
            "country": row['country'],
            "route_pattern": row['route_pattern'],
            "translation": row['translation']
        }

        # Send the API request to add the new ERL
        response = requests.post(url + "add_erl", data=json.dumps(payload), auth=(username, password), verify=False)

        # Check the response status code
        if response.status_code == 200:
            print(f"ERL '{row['erl_name']}' added successfully.")
        else:
            print(f"Failed to add ERL '{row['erl_name']}': " + response.text)
