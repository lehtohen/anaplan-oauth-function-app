import logging
import azure.functions as func
import os
import Constants.SettingKeys

redirect_uri = os.environ[Constants.SettingKeys.SettingKeys.REDIRECT_URI]
response_type = "code"
client_id = os.environ[Constants.SettingKeys.SettingKeys.CLIENT_ID]
scope = "openid%20profile%20email%20offline_access"

def main(req: func.HttpRequest) -> func.HttpResponse:
    authorization_url = "https://us1a.app.anaplan.com/auth/authorize?response_type={}&redirect_uri={}&scope={}&client_id={}".format(response_type, redirect_uri, scope, client_id)
    logging.info(authorization_url)
    html_content = f"""
    <html>
    <head>
        <title>Spotlight Authorization</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 50px;
                text-align: center;
            }}
            .container {{
                display: flex;
                flex-direction: column;
                align-items: center;
            }}
            .button {{
                background-color: #4CAF50;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 20px 0;
                border: none;
                cursor: pointer;
                border-radius: 8px;
            }}
            .description {{
                margin-top: 20px;
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <a href="{authorization_url}" class="button">Click to Authorize</a>
            <div class="description">
                Please click the button above to authorize access. You will be redirected to the Anaplan login page to grant permissions (if not already signed in).
            </div>
        </div>
    </body>
    </html>
    """

    return func.HttpResponse(html_content, mimetype="text/html")
