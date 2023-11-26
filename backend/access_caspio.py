import os
import requests
from requests.exceptions import HTTPError
import time
import json
from dotenv import load_dotenv
from caspio_token import get_token as get_new_token


def get_active_users():
    table = "Users"
    params = "q.where=active='True'"
    load_dotenv()

    account = os.getenv("ACCOUNT_ID")
    access_token = get_new_token()
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
    }
    print("Getting active users from Caspio")

    err_no = 0
    while err_no < 3:
        try:
            resource_response = requests.get(
                "https://"
                + account
                + f".caspio.com/rest/v2/tables/{table}/records?"
                + params,
                headers=headers,
            )
            resource_response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            time.sleep(5)
            err_no += 1
        except Exception as err:
            print(f"Other error occurred: {err}")
            time.sleep(5)
            err_no += 1
        else:
            record = json.loads(resource_response.text)
            record = record["Result"]
            return record
