import requests
import json
import redis

# API keys and URLs
api_keys = [
    "1353c157-a423-47fe-858e-0047659339a9", # avet
    "58e6fee9-acad-49bf-aaf2-a8a4683870ae", # avet89
    "1c8d9c7f-bd5e-4463-9299-442ff6e52a54", # azat
    "3b2a6bdb-82ac-4929-b6b5-996502efb3a6", # dozen
    "eda17a41-c224-4f14-8dba-986ff6f360fc", # yahoo
    "850e7640-6e05-431e-a17f-d49bf84ac954", # ponch
    "adcc49c3-8fbb-44bf-a7b2-1127906fdeff", # stajor
    "5d504268-2b9e-4acb-986e-2ed2d4c05b32", # balayan
    "203118dd-875e-4591-aae9-16ef61d0cea7", # evolver
    "9a4d35d8-0845-4fef-a2cb-2ded60e05e9d", # proton
    "9104fc99-b6ed-403a-9bc4-45bedc2d860b", # dozenproton
    "6f64ea00-8b49-4e4a-bb4e-866f02776e08", # avet89prot
]
    # "2b177986-faf6-4d0f-984a-0f4bc5ac6ac9", # edo

exchanges_url = "https://api.coinalyze.net/v1/exchanges"
future_market_url = "https://api.coinalyze.net/v1/future-markets"
open_interest_url = "https://api.coinalyze.net/v1/open-interest"

# Redis client setup
redis_client = redis.Redis(
    host='localhost',  # Your Redis host
    port=6379,         # Your Redis port
    # db=0               # Your Redis db
)

def slice_into_chunks(arr, chunk_size):
    chunks=[]
    for i in range(0, len(arr), chunk_size):
        chunks.append(arr[i:i + chunk_size])
        
    return chunks

def fetch_data_and_publish():
    try:
        # Exchange data
        response = requests.get(exchanges_url, headers={'api_key': api_keys[0]})
        exchanges_data = response.json()
        # print("Exchanges:", exchanges_data)
        # redis_client.publish('yourChannel', json.dumps(exchanges_data))

        # Future markets data
        response = requests.get(future_market_url, headers={'api_key': api_keys[0]})
        future_markets_data = response.json()
        # print("Future Markets:", future_markets_data)

        # Filtering future markets data (you can adjust the filter criteria)
        gate_future_market = [item for item in future_markets_data if item['exchange'] == 'Y' and item['is_perpetual']]
        print("Filtered Future Markets:", len(gate_future_market))
        gate_oi_table = [
            {
                'symbol': item['symbol'],
                'oi': [],
                'price': [],
                'delta': []
            }
            for item in gate_future_market
        ]

        chunks = slice_into_chunks(gate_future_market, 30)
        print("chunks length >>> ", len(chunks))
        full_oi = []

    except requests.RequestException as error:
        print("Error fetching future_markets_data:", error)



    try:
        for i, chunk in enumerate(chunks):                
            oi_params = ''
            for item in chunk:
                oi_params = oi_params + item['symbol'] + ','

            oi_params = oi_params.rstrip(',')
            # oi_params = ','.join([item[index]['symbol'] for index, item in enumerate(chunk)])
            # print("oi_params >>> ", oi_params)
            response = requests.get(
                open_interest_url,
                headers={'api_key': api_keys[i]},
                params={'symbols': oi_params, 'convert_to_usd': 'true'}
                )
            open_interest = response.json()
            print("open_interest >>> ", open_interest)
            for oi in open_interest: # ['data']
                for gate_oi in gate_oi_table:
                    if gate_oi.get('symbol') == oi.get('symbol'):
                        gate_oi.get('oi').append({'value': oi.get('value'), 'update': oi.get('update')})

                # indexof_oi = next((i for i, item in enumerate(gate_oi_table) if item['symbol'] == oi['symbol']), None)
                # if indexof_oi is not None:
                #     gate_oi_table[indexof_oi]['oi'].append({'value': oi['value'], 'update': oi['update']})

            full_oi.extend(open_interest) # ['data']


    except requests.RequestException as error:
        print("Error fetching open interest data:", error)


    # try:
    #     with open('json_data/open_interest.json', 'w') as file:
    #         json.dump(full_oi, file, indent=2)
    #     print('Data successfully written to file')
    # except Exception as e:
    #     print('Error writing file:', e)
        
    # try:
    #     with open('json_data/gate_oi_table.json', 'w') as file:
    #         json.dump(gate_oi_table, file, indent=2)
    #     print('Data successfully written to file')
    # except Exception as e:
    #     print('Error writing file:', e)
#   alter property of object in the list where another property 'symbol' is equel to 'astra' 
        # More processing and file writing
        # ...


# Call the function
fetch_data_and_publish()

# To run the function periodically, you can use a scheduler like APScheduler
