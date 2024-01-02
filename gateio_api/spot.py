from __future__ import print_function
import os
import json
import gate_api
from gate_api.exceptions import ApiException, GateApiException
from dotenv import load_dotenv
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = API_KEY,
    secret = API_SECRET
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)

def serialize_response(obj):
    if isinstance(obj, gate_api.Currency):
        # Convert UniCurrency object to a dictionary
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def list_spot_contracts():
    try:
        # Get a single contract
        api_response = api_instance.list_currencies()
        json_string = json.dumps(api_response, indent=2, default=serialize_response)
        list_spot_contracts=json.loads(json_string)
        # Write the JSON data to a file
        with open("list_spot_contracts.json", 'w') as file:
            json.dump(list_spot_contracts, file, indent=4)
        return list_spot_contracts
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->get_delivery_contract: %s\n" % e)


def list_currency_pairs():
    try:
    # List all currency pairs supported
        api_response = api_instance.list_currency_pairs()
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling SpotApi->list_currency_pairs: %s\n" % e)