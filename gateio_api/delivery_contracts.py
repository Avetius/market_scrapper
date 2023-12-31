import json
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency

# Define a custom serialization function for UniCurrency objects
def serialize_response(obj):
    if isinstance(obj, gate_api.Contract or 
                  gate_api.DeliveryContract or 
                  gate_api.UniCurrency):
        # Convert UniCurrency object to a dictionary
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


try:
    # List all futures contracts
    list_delivery_contracts = api_instance.list_delivery_contracts(settle)
    json_string = json.dumps(list_delivery_contracts, indent=2, default=serialize_response) # , default=serialize_delivery_contracts

    # Save the JSON string to a file
    with open('list_delivery_contracts.json', 'w') as json_file:
        json_file.write(json_string)

    delivery_contracts = json.loads(json_string)
    names = [item['name'] for item in delivery_contracts if "name" in item]
    print(len(names))


except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_contracts: %s\n" % e)