import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "277b561d99678f9dfff978ae65b8ce36",
    secret = "4f5fef188468aec17c36e7f46a319a5cc664fd0ab6681d3c8028ae2acb88dbbe"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
status = 'open' # str | Only list the orders with this status
contract = 'PEPE2_USDT_20231201' # str | Futures contract (optional)
limit = 10 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
last_id = '12345' # str | Specify list staring point using the `id` of last record in previous list-query results (optional)
count_total = 0 # int | Whether to return total number matched. Default to 0(no return) (optional) (default to 0)

try:
    # List futures orders
    api_response = api_instance.list_delivery_orders(settle, status) # , last_id=last_id, limit=limit, offset=offset, count_total=count_total, , contract=contract
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_orders: %s\n" % e)