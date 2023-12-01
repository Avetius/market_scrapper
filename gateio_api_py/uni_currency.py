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
api_instance = gate_api.EarnUniApi(api_client)

# Define a custom serialization function for UniCurrency objects
def serialize_uni_currency(obj):
    if isinstance(obj, gate_api.UniCurrency):
        # Convert UniCurrency object to a dictionary
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

try:
    # List currencies for lending
    list_uni_currencies = api_instance.list_uni_currencies()
    # Convert the api_response to a JSON-formatted string
    json_string = json.dumps(list_uni_currencies, indent=2, default=serialize_uni_currency)

    # Save the JSON string to a file
    with open('list_uni_currencies.json', 'w') as json_file:
        json_file.write(json_string)

    print("list_uni_currencies saved to list_uni_currencies.json")
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnUniApi->list_uni_currencies: %s\n" % e)