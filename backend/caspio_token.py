import os
from dotenv import load_dotenv
import requests as r
from oauthlib.oauth2 import WebApplicationClient
from requests.exceptions import HTTPError


def get_token():
    load_dotenv()

    account = os.getenv("ACCOUNT_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    token_url = 'https://' + account + \
                '.caspio.com/oauth/token'  # Swagger url to get the token
    # Pre-formatting the body of the api call:
    body = 'grant_type=client_credentials&client_id=' + \
           client_id + '&client_secret=' + client_secret
    # From oauth library, I can create client to assist with the requests:
    client = WebApplicationClient(client_id)

    try:
        # request library as r, post request:
        response = r.post(token_url, data=body)
        # getting response and checking the status of the call, printing any exceptions
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        # Using the oauth library to parse the response, and I'm getting the text (str) of the response
        client.parse_request_body_response(response.text)
        token_values = []
        for value in client.token.values():
            token_values.append(value)
        # print(token_values)
        return token_values[0]