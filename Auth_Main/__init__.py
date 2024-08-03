import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Parse the request body to JSON
        req_body = req.get_json()
    except ValueError:
        logging.info("Error in request body")
        pass  # Handle the case where there is no JSON body
    else:
        auth_token = req_body.get('token')

    # Execute your logic

    return func.HttpResponse("Trigger succesful")
        
