const axios = require('axios');
const fs = require('fs');

var api_keys = [
    "1353c157-a423-47fe-858e-0047659339a9", // avet
    "58e6fee9-acad-49bf-aaf2-a8a4683870ae", // avet89
    "1c8d9c7f-bd5e-4463-9299-442ff6e52a54", // azat
    "3b2a6bdb-82ac-4929-b6b5-996502efb3a6", // dozen
    "eda17a41-c224-4f14-8dba-986ff6f360fc", // yahoo
    "850e7640-6e05-431e-a17f-d49bf84ac954", // ponch
    "adcc49c3-8fbb-44bf-a7b2-1127906fdeff", // stajor
    "adcc49c3-8fbb-44bf-a7b2-1127906fdeff", // stajor
    "5d504268-2b9e-4acb-986e-2ed2d4c05b32", // balayan
    "203118dd-875e-4591-aae9-16ef61d0cea7", // evolver
    "9a4d35d8-0845-4fef-a2cb-2ded60e05e9d", // proton
    "9104fc99-b6ed-403a-9bc4-45bedc2d860b", // dozenproton
    "6f64ea00-8b49-4e4a-bb4e-866f02776e08", // avet89prot
]
// "2b177986-faf6-4d0f-984a-0f4bc5ac6ac9", // edo

var exchanges_url = "https://api.coinalyze.net/v1/exchanges"
var future_market_url = "https://api.coinalyze.net/v1/future-markets"
var open_interest_url = "https://api.coinalyze.net/v1/open-interest"
// const redis = require('redis');

// Create a Redis client
// const redisClient = redis.createClient({
//   // Your Redis configuration here
// });
// Connect to Redis server
// const pubsub = redis.createClient({
//     // Your Redis configuration
// });
  
  // Subscribe to a channel
// pubsub.subscribe('my_channel');
  
//   // Handle incoming messages
// pubsub.on('message', (channel, message) => {
//     console.log(`Received message from ${channel}: ${message}`);
//     const futures_pairs = message.split(",");
function sliceIntoChunks(arr, chunkSize) {
    const chunks = [];
    for (let i = 0; i < arr.length; i += chunkSize) {
        const chunk = arr.slice(i, i + chunkSize);
        chunks.push(chunk);
    }
    return chunks;
}

const sample_data = [
    {
        symbol: 'ASTRA_USDT.Y',
        oi: [
            {value: 186528.4727, update: 1703682383969},
            {value: 186528.4727, update: 1703682383969},
            {value: 186528.4727, update: 1703682383969}
        ],
        price: [
            {value: 186528.4727, update: 1703682383969},
            {value: 186528.4727, update: 1703682383969}
        ],
        delta: [
            {value: 186528.4727, update: 1703682383969},
            {value: 186528.4727, update: 1703682383969}
        ]
    }
]


// });
// pubsub.on('error', (err) => {
//     console.log('Redis error: ', err);
// });

// Function to fetch data and publish to Redis
const fetchDataAndPublish = async () => {
  try {
    /********EXCHANGE********/
    // const exchanges = await axios.get(exchanges_url, { headers: { api_key }});
    // console.log("exchanges >>> ", exchanges.data);
    // Publish the result to a Redis channel
    // redisClient.publish('yourChannel', JSON.stringify(response.data));
    /********FUTURE MARKETS********/
    // const future_markets = await axios.get(future_market_url, { headers: { api_key }});
    // console.log("future_markets length >>> ", future_markets);
    // const gate_future_market = future_markets.data.filter(item => item.exchange === "Y")

    const jsonData = fs.readFileSync('future_markets.json', 'utf8');

    // Parse the JSON data
    const future_market = JSON.parse(jsonData);

    console.log("future_market.length >>> ", future_market.length)

    const gate_future_market = await future_market.filter((item) => {
        return (item.exchange === "Y") && (item.is_perpetual === true)
    }) // && (item.is_perpetual == true) // chunks
    console.log("gate_future_market.length >>> ", gate_future_market.length)
    const gate_oi_table = gate_future_market.map((item) => {
        return {
            symbol: item.symbol,
            oi: [],
            price: [],
            delta: []
        }
    })
    const chunks = sliceIntoChunks(gate_future_market, 30)
    console.log("chunks.length >>> ", chunks.length);
    const full_oi = []

    let i = 0;
    for (const chunk of chunks) {
        let oi_params = await chunk.reduce((accumulator, item) => { return accumulator + item.symbol + ',' }, '');
        oi_params = oi_params.slice(0, -1); // delete the last "," char
        console.log("oi_params >>> ", oi_params);
        // /********OPEN INTEREST********/
        const open_interest = await axios.get(open_interest_url, {
            headers: { api_key: api_keys[i] },
            params: { symbols: oi_params, convert_to_usd: "true"} // convert_to_usd: "true"
        }).catch(error => {
            if (error.response) {
                // The request was made and the server responded with a status code
                // that falls out of the range of 2xx
                if (error.response.data) console.error('Error Data:', error.response.data);
                if (error.response.status) {
                    console.error('Status:', error.response.status);
                    if(error.response.status == 401 ) console.log("invalid api key # ", i)
                }
            } else if (error.request) {
                // The request was made but no response was received
                if (error.request) console.error('No response:', error.request);
            } else {
                // Something happened in setting up the request that triggered an Error
                if (error.message) console.error('Error:', error.message);
            }
            if (error.message.config) console.error('Config:', error.config);
        });
        if(open_interest) {
            if(open_interest.data) {
                console.log("open_interest.data >>> ", open_interest.data);
                for(const oi of open_interest.data) {
                    const indexof_oi = gate_oi_table.findIndex(item => item.symbol === oi.symbol);
                    gate_oi_table[indexof_oi].oi.push({value: oi.value, update: oi.update});
                }
                full_oi.push(...open_interest.data)
            }
        }
        i++
    }



    // console.log("full_oi >>> ", full_oi);
    fs.writeFile('json_data/open_interest.json', JSON.stringify(full_oi, null, 2), (err) => {
        if (err) {
            console.error('Error writing file:', err);
        } else {
            console.log('Data successfully written to file');
        }
    });
    fs.writeFile('json_data/gate_oi_table.json', JSON.stringify(gate_oi_table, null, 2), (err) => {
        if (err) {
            console.error('Error writing file:', err);
        } else {
            console.log('Data successfully written to file');
        }
    });
    // Write the data to a JSON file
    // fs.writeFile('json_data/exchanges.json', JSON.stringify(exchanges.data, null, 2), (err) => {
    //     if (err) {
    //         console.error('Error writing file:', err);
    //     } else {
    //         console.log('Data successfully written to file');
    //     }
    // });
    // fs.writeFile('json_data/future_markets.json', JSON.stringify(future_markets.data, null, 2), (err) => {
    //     if (err) {
    //         console.error('Error writing file:', err);
    //     } else {
    //         console.log('Data successfully written to file');
    //     }
    // });
    // fs.writeFile('json_data/open_interest.json', JSON.stringify(open_interest.data, null, 2), (err) => {
    //     if (err) {
    //         console.error('Error writing file:', err);
    //     } else {
    //         console.log('Data successfully written to file');
    //     }
    // });
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

fetchDataAndPublish()
// Interval to run the function every 10 seconds
// setInterval(fetchDataAndPublish, 10000);