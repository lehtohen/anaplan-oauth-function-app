import logging
import azure.functions as func
import requests
import os
import Constants.SettingKeys

CLIENT_ID = os.environ[Constants.SettingKeys.SettingKeys.CLIENT_ID]
CLIENT_SECRET = os.environ[Constants.SettingKeys.SettingKeys.CLIENT_SECRET]
TOKEN_URL = os.environ[Constants.SettingKeys.SettingKeys.TOKEN_URL]
REDIRECT_URI = os.environ[Constants.SettingKeys.SettingKeys.REDIRECT_URI]
MAIN_URL = os.environ[Constants.SettingKeys.SettingKeys.MAIN_URL]

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    code = req.params.get('code')
    if not code:
        logging.info("Missing authorization code")
        return func.HttpResponse("Missing authorization code", status_code=400)
    
    logging.info(f"Authorization code received: {code}")

    # Exchange the authorization code for an access token
    token_response = requests.post(
        TOKEN_URL,
        headers={'Content-Type': 'application/json'},
        json={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
    )
    logging.info(f"Token_response: {token_response}")
    if token_response.status_code != 200:
        return func.HttpResponse(f"Error: {token_response.text}", status_code=token_response.status_code)
    
    response = token_response.json()
    access_token = response['access_token']
    token = "Bearer {}".format(access_token)
    logging.info(f"Here is your authentication token: {token}")

    url = MAIN_URL
    payload = {'token': token }  # Whatever payload your function expects
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Will raise an exception for HTTP errors

    return func.HttpResponse(f"Here is your authentication token: {token}.", status_code=200)
