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
contract = 'BTC_USDT' # str | Futures contract
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
last_id = '12345' # str | Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. Use `from` and `to` instead to limit time range (optional)
_from = 1546905600 # int | Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items. If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  (optional)
to = 1546935600 # int | Specify end time in Unix seconds, default to current time (optional)

try:
    # Futures trading history
    api_response = api_instance.list_delivery_trades(settle, contract, limit=limit, last_id=last_id, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_trades: %s\n" % e)