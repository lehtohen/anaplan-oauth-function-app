**Anaplan OAuth Function App Example**

**Description:**

Azure Function App example for OAuth to Anaplan API. Will return an authentication token. 

Created by Henrikki Lehtola - henrikki.lehtola@gmail.com

**Descriptions for each function app:**

OAuth_Initiate:
Will contain the url that is used to trigger the function app.
Contains the HTML that will be used to create a more user friendly authentication view.

OAuth_Callback:
Callback function that will create the authentication token and trigger the Main script.
In function.json, set AuthLevel as Anonymous.

OAuth_Main:
Main logic that your script should execute.
Will be called by the OAuth_Callback function and takes the authentication token as a parameter.
