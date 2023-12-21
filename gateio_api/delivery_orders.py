from __future__ import print_function
import os
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
api_instance = gate_api.DeliveryApi(api_client)

def list_delivery_contracts(contract,settle='usdt'):
    try:
        # Get a single contract
        api_response = api_instance.get_delivery_contract(settle, contract)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->get_delivery_contract: %s\n" % e)

def get_delivery_contract(contract,settle='usdt'):
    try:
        # Get a single contract
        api_response = api_instance.get_delivery_contract(settle, contract)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->get_delivery_contract: %s\n" % e)


def list_delivery_order_book(contract,settle='usdt',interval='0',limit=10,with_id=False):
    try:
        # Futures order book
        api_response = api_instance.list_delivery_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_order_book: %s\n" % e)

def list_delivery_trades(contract,limit,_from,to,settle='usdt'):
    try:
        # Futures trading history
        api_response = api_instance.list_delivery_trades(settle, contract, limit=limit, _from=_from, to=to)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_trades: %s\n" % e)


def list_delivery_tickers(contract,settle='usdt'):
    try:
        # List futures tickers
        api_response = api_instance.list_delivery_tickers(settle, contract=contract)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_tickers: %s\n" % e)


def list_delivery_accounts(settle='usdt'):
    try:
        # Query futures account
        api_response = api_instance.list_delivery_accounts(settle)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_accounts: %s\n" % e)


def list_delivery_account_book(_from,to,limit=100,type='dnw',settle='usdt'): # Changing Type: - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit & Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate (optional)
    try:
        # Query account book
        api_response = api_instance.list_delivery_account_book(settle, limit=limit, _from=_from, to=to, type=type)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_account_book: %s\n" % e)


def delivery_orders(contract,settle='usdt',status='open',limit=10,offset=0,last_id='12345',count_total=0):
    try:
        # List futures orders
        api_response = api_instance.list_delivery_orders(settle, status, contract=contract, limit=limit, offset=offset, last_id=last_id, count_total=count_total)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling DeliveryApi->list_delivery_orders: %s\n" % e)

