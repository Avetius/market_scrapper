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
contract = 'PEPE2_USDT_20231130' # str | Futures contract
interval = '10' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 50 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)
with_id = False # bool | Whether the order book update ID will be returned. This ID increases by 1 on every order book update (optional) (default to False)

# Define a custom serialization function for UniCurrency objects
def serialize(obj):
    if isinstance(obj, gate_api.DeliveryContract or gate_api.UniCurrency):
        # Convert UniCurrency object to a dictionary
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

try:
    # Futures order book
    delivery_order_book = api_instance.list_delivery_order_book(settle=settle, contract=contract, interval=interval, limit=limit) # , with_id=with_id
    json_string = json.dumps(delivery_order_book, indent=2) # , default=serialize

    # Save the JSON string to a file
    with open('delivery_order_book.json', 'w') as json_file:
        json_file.write(json_string)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->delivery_order_book: %s\n" % e)