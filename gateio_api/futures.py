from __future__ import print_function
import os
import json
from datetime import datetime
import gate_api
from gate_api.exceptions import ApiException, GateApiException
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.

def convert_to_unix_timestamp(input_date_time):
    # Check if the input is a datetime object
    if isinstance(input_date_time, datetime):
        timestamp = datetime.timestamp(input_date_time)
    # Check if the input is a string
    elif isinstance(input_date_time, str):
        try:
            date_time_obj = datetime.strptime(input_date_time, '%Y-%m-%d %H:%M:%S')
            timestamp = datetime.timestamp(date_time_obj)
        except ValueError:
            return "Invalid date-time string format. Please use 'YYYY-MM-DD HH:MM:SS'."
    else:
        return "Invalid input type. Please provide a datetime object or a string."

    return int(timestamp)

configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = API_KEY,
    secret = API_SECRET
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.FuturesApi(api_client)

def serialize_response(obj):
    if isinstance(obj, gate_api.Contract or 
                  gate_api.DeliveryContract or 
                  gate_api.UniCurrency):
        # Convert UniCurrency object to a dictionary
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def list_futures_contracts(settle='usdt'):
    try:
        # Get a single contract
        api_response = api_instance.list_futures_contracts(settle)
        json_string = json.dumps(api_response, indent=2, default=serialize_response)
        # list_futures_contracts=json.loads(json_string)
        # print(api_response)
        return json_string
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_futures_contract: %s\n" % e)

def get_futures_contract(settle='usdt',contract='BTC_USDT'):
    try:
        # Get a single contract
        api_response = api_instance.get_futures_contract(settle, contract)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_futures_contract: %s\n" % e)

def list_futures_order_book(settle='usdt',contract='BTC_USDT',interval='0',limit=10,with_id=False):
    try:
        # Futures order book
        api_response = api_instance.list_futures_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_order_book: %s\n" % e)

def list_futures_trades(_from=1546905600,to=1546935600,settle='usdt',contract='BTC_USDT',limit=100,offset=0,last_id=12345):
    try:
        # Futures trading history
        api_response = api_instance.list_futures_trades(settle, contract, limit=limit, offset=offset, last_id=last_id, _from=_from, to=to)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)

def list_futures_candlesticks(_from=1546905600,to=1546935600,settle='usdt',contract='BTC_USDT',limit=10,interval='5m'):
    try:
    # Get futures candlesticks
        api_response = api_instance.list_futures_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_candlesticks: %s\n" % e)

def list_futures_premium_index(_from=1546905600,to=1546935600,settle='usdt',contract='BTC_USDT',limit=10,interval='5m'):
    try:
        # Premium Index K-Line
        api_response = api_instance.list_futures_premium_index(settle, contract, _from=_from, to=to, limit=limit, interval=interval)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_premium_index: %s\n" % e)

def list_futures_tickers(settle='usdt',contract='BTC_USDT'):
    try:
        # List futures tickers
        api_response = api_instance.list_futures_tickers(settle, contract=contract)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_tickers: %s\n" % e)

def list_futures_funding_rate_history():
    try:
        # Funding rate history
        api_response = api_instance.list_futures_funding_rate_history(settle='usdt',contract='BTC_USDT',limit=100)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)

def list_futures_insurance_ledger(settle='usdt',limit=100):
    try:
        # Futures insurance balance history
        api_response = api_instance.list_futures_insurance_ledger(settle, limit=limit)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_insurance_ledger: %s\n" % e)

def list_contract_stats_alt(settle='usdt'):
    try:
        # List all futures contracts
        list_futures_contract = api_instance.list_futures_contracts(settle)
        json_string = json.dumps(list_futures_contract, indent=2, default=serialize_response)

        # Save the JSON string to a file
        with open('list_futures_contract.json', 'w') as json_file:
            json_file.write(json_string)

        data = json.loads(json_string)
        names = [item['name'] for item in data if "name" in item]
        print(len(names))
        return data
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_contract: %s\n" % e)

def list_contract_stats(settle='usdt',contract='BTC_USDT',_from=1604561000,interval='5m',limit=30):
    try:
        # Futures stats
        api_response = api_instance.list_contract_stats(settle, contract, _from=_from, interval=interval, limit=limit)
        print(api_response)
        return api_response
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_contract_stats: %s\n" % e)

def get_index_constituents(settle='usdt',index='BTC_USDT'):
    try:
        # Get index constituents
        api_response = api_instance.get_index_constituents(settle, index)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_index_constituents: %s\n" % e)

def list_liquidated_orders(settle='usdt',contract='BTC_USDT',_from=1547706332,to=1547706332,limit=100):
    try:
        # Retrieve liquidation history
        api_response = api_instance.list_liquidated_orders(settle, contract=contract, _from=_from, to=to, limit=limit)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_liquidated_orders: %s\n" % e)

def list_futures_accounts(settle='usdt'):
    try:
        # Query futures account
        api_response = api_instance.list_futures_accounts(settle)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)

def list_futures_account_book(settle='usdt',contract='BTC_USDT',_from=1604561000,to=1547706332,limit=100,type='dnw'): #deposit n withdraw, pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit & Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate - bonus_offset: bouns deduction (optional)
    try:
        # Query account book
        api_response = api_instance.list_futures_account_book(settle, contract=contract, limit=limit, _from=_from, to=to, type=type)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_account_book: %s\n" % e)

def list_positions(settle='usdt',holding=True):
    try:
        # List all positions of a user
        api_response = api_instance.list_positions(settle, holding=holding)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_positions: %s\n" % e)

def list_position(settle='usdt',holding=True):
    try:
        # List all positions of a user
        api_response = api_instance.list_positions(settle, holding=holding)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_positions: %s\n" % e)

def get_position(settle='usdt',contract='BTC_USDT'):
    try:
        # Get single position
        api_response = api_instance.get_position(settle, contract)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_position: %s\n" % e)

def list_futures_orders(settle='usdt',contract='BTC_USDT',status='open',limit=100,offset=0,last_id='12345'):
    try:
        # List futures orders
        api_response = api_instance.list_futures_orders(settle, status, contract=contract, limit=limit, offset=offset, last_id=last_id)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_futures_orders: %s\n" % e)

def create_futures_order(settle='usdt'):
    try:
        # Create a futures order
        futures_order = gate_api.FuturesOrder() # FuturesOrder | 
        api_response = api_instance.create_futures_order(settle, futures_order)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->create_futures_order: %s\n" % e)

def cancel_futures_orders(settle='usdt',contract='BTC_USDT',side='ask'):
    try:
        # Cancel all `open` orders matched
        api_response = api_instance.cancel_futures_orders(settle, contract, side=side)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->cancel_futures_orders: %s\n" % e)

def get_orders_with_time_range(settle='usdt',contract='BTC_USDT',_from=1604561000,to=1547706332,limit=100,offset=0):
    try:
        # List Futures Orders By Time Range
        api_response = api_instance.get_orders_with_time_range(settle, contract=contract, _from=_from, to=to, limit=limit, offset=offset)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_orders_with_time_range: %s\n" % e)

def create_batch_futures_order(settle='usdt'):
    try:
        futures_order = [gate_api.FuturesOrder()] # list[FuturesOrder] | 
        # Create a batch of futures orders
        api_response = api_instance.create_batch_futures_order(settle, futures_order)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->create_batch_futures_order: %s\n" % e)

def get_futures_order(settle='usdt',order_id='12345'):    
    try:
        # Get a single order
        api_response = api_instance.get_futures_order(settle, order_id)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_futures_order: %s\n" % e)

def amend_futures_order(settle='usdt',order_id='12345'):
    try:
        # Amend an order
        futures_order_amendment = gate_api.FuturesOrderAmendment() # FuturesOrderAmendment |
        api_response = api_instance.amend_futures_order(settle, order_id, futures_order_amendment)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->amend_futures_order: %s\n" % e)

def cancel_futures_order(settle='usdt',order_id='12345'):
    try:
        # Cancel a single order
        api_response = api_instance.cancel_futures_order(settle, order_id)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->cancel_futures_order: %s\n" % e)

def get_my_trades(settle='usdt',contract='BTC_USDT',order=12345,limit=100,offset=0,last_id='12345'):
    try:
        # List personal trading history
        api_response = api_instance.get_my_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)

def get_my_trades_with_time_range(settle='usdt',contract='BTC_USDT',_from=1604561000,to=1547706332,limit=100,offset=0,role='maker'): # Query role, maker or taker.
    try:
        # List personal trading history by time range
        api_response = api_instance.get_my_trades_with_time_range(settle, contract=contract, _from=_from, to=to, limit=limit, offset=offset, role=role)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->get_my_trades_with_time_range: %s\n" % e)

def list_position_close(settle='usdt',contract='BTC_USDT',_from=1604561000,to=1547706332,limit=100,offset=0,side='short',pnl='profit'): #Query profit or loss, Query side. long or short
    try:
        # List position close history
        api_response = api_instance.list_position_close(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to, side=side, pnl=pnl)
        print(api_response)
    except GateApiException as ex:
        print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
    except ApiException as e:
        print("Exception when calling FuturesApi->list_position_close: %s\n" % e)


    