import os
import json
import gate_api
from gate_api.exceptions import ApiException, GateApiException
from dotenv import load_dotenv

load_dotenv()

# Access environmental variables
RABBITMQ_URL = os.getenv("RABBITMQ_URL")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
# Use the variables as needed
print(f"RABBITMQ_URL: {RABBITMQ_URL}")
print(f"API_KEY: {API_KEY}")
print(f"API_SECRET: {API_SECRET}")

configuration = gate_api.Configuration(
    host = RABBITMQ_URL, # "https://api.gateio.ws/api/v4",
    key = API_KEY,
    secret = API_SECRET
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_futures_instance = gate_api.FuturesApi(api_client)
# Define a custom serialization function for UniCurrency objects
def serialize_response(obj):
        if isinstance(obj, gate_api.Contract or
                    gate_api.DeliveryContract or
                    gate_api.UniCurrency):
            # Convert UniCurrency object to a dictionary
            return obj.to_dict()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def listFuturesContracts(settle = 'usdt'):
    settle = 'usdt' # str | Settle currency

    try:
        # List all futures contracts
        list_futures_contract = api_futures_instance.list_futures_contracts(settle)
        json_string = json.dumps(list_futures_contract, indent=2, default=serialize_response)
        print('>>>>>>>>>>>>> futures contract list recieved! <<<<<<<<<<<')
        return json_string

        # Save the JSON string to a file
        # with open('list_futures_contract.json', 'w') as json_file:
        #     json_file.write(json_string)


    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_contract: %s\n" % e)

