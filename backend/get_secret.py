import os
import time
import requests as r
from requests.exceptions import HTTPError
from dotenv import load_dotenv
from caspio_token import get_token as get_new_token

load_dotenv()


def get_secret():
    """Check non-dispatch days to allow for next working day dispatches over 3 day weekends and whatnot"""
    table = "cm_tbl_users"
    params = "q.where=Login_status='true'"
    load_dotenv()
    account = os.getenv("ACCOUNT_ID")
    access_token = get_new_token()  # generate Caspio token for authentication
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json",
    }
    # runtime = time.time()
    print("Getting bad days from Caspio")
    import json

    err_no = 0
    while err_no < 3:
        try:
            resource_response = r.get(
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
