import requests
import time
import json

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

import networkx as nx

arr = [
      'COMP_USDT.Y','FTM_USDT.Y','JASMY_USDT.Y','CHZ_USDT.Y','CELR_USDT.Y','YFII_USDT.Y','CTSI_USDT.Y','KAVA_USDT.Y','USTC_USDT.Y','MC_USDT.Y','ZEC_USDT.Y','CVC_USDT.Y',
      'NEAR_USDT.Y','NKN_USDT.Y','WOO_USDT.Y','EOS_USDT.Y','UNI_USDT.Y','KEY_USDT.Y','CYBER_USDT.Y','XEN_USDT.Y','VRA_USDT.Y','ID_USDT.Y','INJ_USDT.Y','IGU_USDT.Y','APE_USDT.Y',
      'ANT_USDT.Y','XLM_USDT.Y','LADYS_USDT.Y','ALGO_USDT.Y','IOST_USDT.Y','FLOKI_USDT.Y','PEOPLE_USDT.Y','C98_USDT.Y','MOVR_USDT.Y','RSR_USDT.Y','DYDX_USDT.Y','YFI_USDT.Y',
      'TOMO_USDT.Y','ICX_USDT.Y','BAT_USDT.Y','PEPE2_USDT.Y','OG_USDT.Y','GT_USDT.Y','AVAX_USDT.Y','ETC_USDT.Y','UNFI_USDT.Y','FITFI_USDT.Y','EDU_USDT.Y','BUSD_USDT.Y','PEPE_USDT.Y'
      ,'AUDIO_USDT.Y','SUSHI_USDT.Y','SXP_USDT.Y','LOOKS_USDT.Y','ICP_USDT.Y','TRX_USDT.Y','MAV_USDT.Y','ONT_USDT.Y','MTL_USDT.Y','GMT_USDT.Y','COTI_USDT.Y','ALICE_USDT.Y','QTUM_USDT.Y',
      'CSPR_USDT.Y','LIT_USDT.Y','BCH_USDT.Y','HFT_USDT.Y','RAD_USDT.Y','FLR_USDT.Y','APT_USDT.Y','BNB_USDT.Y','BLUR_USDT.Y','BICO_USDT.Y','ETHW_USDT.Y','DGB_USDT.Y','FTT_USDT.Y',
      'REN_USDT.Y','DASH_USDT.Y','WLD_USDT.Y','RARE_USDT.Y','MINA_USDT.Y','GAL_USDT.Y','ZEN_USDT.Y','RNDR_USDT.Y','LTC_USDT.Y','VMPX_USDT.Y','XRD_USDT.Y','WOJAK_USDT.Y','CVX_USDT.Y',
      'LDO_USDT.Y','SC_USDT.Y','DHX_USDT.Y','OKB_USDT.Y','LAI_USDT.Y','THETA_USDT.Y','SUI_USDT.Y','BEL_USDT.Y','AAVE_USDT.Y','OGN_USDT.Y','WIN_USDT.Y','VELO_USDT.Y','CRV_USDT.Y','OOKI_USDT.Y',
      'KDA_USDT.Y','STX_USDT.Y','ONG_USDT.Y','XTZ_USDT.Y','ORDI_USDT.Y','MDT_USDT.Y','LRC_USDT.Y','IMX_USDT.Y','ATOM_USDT.Y','TOMI_USDT.Y','SSV_USDT.Y','MAGIC_USDT.Y','BNT_USDT.Y','AXS_USDT.Y',
      'IOTX_USDT.Y','ROSE_USDT.Y','ANKR_USDT.Y','OCEAN_USDT.Y','CORE_USDT.Y','ASTRA_USDT.Y','OXT_USDT.Y','KSM_USDT.Y','GRT_USDT.Y','EGLD_USDT.Y','KNC_USDT.Y','STG_USDT.Y','LPT_USDT.Y',
      'GMX_USDT.Y','ZIL_USDT.Y','ARB_USDT.Y','POGAI_USDT.Y','MBABYDOGE_USDT.Y','CRO_USDT.Y','GALA_USDT.Y','LOKA_USDT.Y','SYN_USDT.Y','AGLD_USDT.Y','DODO_USDT.Y','QNT_USDT.Y',
      'VET_USDT.Y','CKB_USDT.Y','1INCH_USDT.Y','SHIB_USDT.Y','HBAR_USDT.Y','ENJ_USDT.Y','TRU_USDT.Y','VGX_USDT.Y','OP_USDT.Y','ASTR_USDT.Y','DOT_USDT.Y','ZRX_USDT.Y','STORJ_USDT.Y',
      'RDNT_USDT.Y','XEC_USDT.Y','LINK_USDT.Y','AKRO_USDT.Y','FET_USDT.Y','CAKE_USDT.Y','BSV_USDT.Y','FLUX_USDT.Y','BAND_USDT.Y','WAVES_USDT.Y','FIDA_USDT.Y','CELO_USDT.Y','JOE_USDT.Y',
      'HOOK_USDT.Y','XMR_USDT.Y','SKL_USDT.Y','REEF_USDT.Y','KAS_USDT.Y','LUNC_USDT.Y','MKR_USDT.Y','BTS_USDT.Y','RUNE_USDT.Y','ARKM_USDT.Y','SAND_USDT.Y','YGG_USDT.Y','FIL_USDT.Y',
      'LQTY_USDT.Y','ONE_USDT.Y','MANA_USDT.Y','SLP_USDT.Y','HIGH_USDT.Y','XRP_USDT.Y','MATIC_USDT.Y','ARPA_USDT.Y','BNX_USDT.Y','SRM_USDT.Y','SOL_USDT.Y','PHB_USDT.Y','AGIX_USDT.Y',
      'SNX_USDT.Y','FLM_USDT.Y','FLOW_USDT.Y','RPL_USDT.Y','ACA_USDT.Y','LINA_USDT.Y','ENS_USDT.Y','WEMIX_USDT.Y','BAIDOGE_USDT.Y','XCN_USDT.Y','GLMR_USDT.Y','BTC_USDT.Y','TON_USDT.Y',
      'USDC_USDT.Y','XCH_USDT.Y','GLM_USDT.Y','GFT_USDT.Y','XVG_USDT.Y','HT_USDT.Y','SEI_USDT.Y','PENDLE_USDT.Y','MASK_USDT.Y','TURBO_USDT.Y','ACH_USDT.Y','API3_USDT.Y','OMG_USDT.Y',
      'RAY_USDT.Y','ALPHA_USDT.Y','ADA_USDT.Y','ETH_USDT.Y','RVN_USDT.Y','HIFI_USDT.Y','BLZ_USDT.Y','LUNA_USDT.Y','AR_USDT.Y','DOGE_USDT.Y','KLAY_USDT.Y','CFX_USDT.Y','BAKE_USDT.Y']

apis = ['2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9',
        '2b177986-faf6-4d0f-984a-0f4bc5ac6ac9']

api = apis[0]
now = int(time.time())
before = now - 172800 #12 hour data in seconds


##################################################################

def getPrice(sym):

  url = 'https://api.coinalyze.net/v1/ohlcv-history?symbols='+sym+'&from='+str(before)+'&to='+str(now)+'&interval=15min&api_key='+api

  print(url)

  df = requests.get(url).json()
  dumps = json.dumps(df)
  loads = json.loads(dumps)

  jsonOk = False

  if len(loads) > 0:
    jsonOk = True
    ticker = loads[0]['symbol']

    df = pd.DataFrame(loads[0]['history'])

    # Convert unix timestamps to datetime
    df['datetime'] = pd.to_datetime(df['t'], unit='s')

    ################################

    # Get minimum value
    min_value = df[['o','h','l','c']].min().min()

    # Normalize to 0 baseline
    df['open'] = (df['o'] - min_value) / min_value
    df['high'] = (df['h'] - min_value) / min_value
    df['low'] = (df['l'] - min_value) / min_value
    df['close'] = (df['c'] - min_value) / min_value

    # Plot percentage candlestick
    fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])

    fig.update_yaxes(tickformat='.2%')
    fig.update_layout(
    title=ticker,
    xaxis_title='Date',
    yaxis_title='OI%')
    fig.show()

  else:
    print('JSON is empty')

##################################################################

def getOI(sym):

  url = 'https://api.coinalyze.net/v1/open-interest-history?symbols='+sym+'&from='+str(before)+'&to='+str(now)+'&interval=1min&convert_to_usd=false&api_key='+api

  #print(url)

  df = requests.get(url).json()
  dumps = json.dumps(df)
  loads = json.loads(dumps)

  jsonOk = False

  if len(loads) > 0:
    jsonOk = True
    ticker = loads[0]['symbol']

    df = pd.DataFrame(loads[0]['history'])

    # Convert unix timestamps to datetime
    df['datetime'] = pd.to_datetime(df['t'], unit='s')

    # Get minimum value
    min_value = df[['o','h','l','c']].min().min()

    # Normalize to 0 baseline
    df['open'] = (df['o'] - min_value) / min_value
    df['high'] = (df['h'] - min_value) / min_value
    df['low'] = (df['l'] - min_value) / min_value
    df['close'] = (df['c'] - min_value) / min_value

    # Plot percentage candlestick
    fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])])

    fig.update_yaxes(tickformat='.2%')
    fig.update_layout(
    title=ticker,
    xaxis_title='Date',
    yaxis_title='OI%')
    fig.show()

  else:
    print('JSON is empty')

##################################################################

def getDelta(sym):

  url = 'https://api.coinalyze.net/v1/ohlcv-history?symbols='+sym+'&from='+str(before)+'&to='+str(now)+'&interval=1min&api_key='+api

  print(url)

  df = requests.get(url).json()
  dumps = json.dumps(df)
  loads = json.loads(dumps)

  jsonOk = False

  if len(loads) > 0:
    jsonOk = True
    ticker = loads[0]['symbol']

    df = pd.DataFrame(loads[0]['history'])

    # Convert unix timestamps to datetime
    df['datetime'] = pd.to_datetime(df['t'], unit='s')

    ################################

    # Buy volume
    df['buy_vol'] = df['bv']

    # Sell volume
    df['sell_vol'] = df['v'] - df['bv']

    # Calculate delta
    df['delta'] = df['buy_vol'] - df['sell_vol']

    ################################

    # Plot delta over time
    fig = px.bar(df, x='datetime', y='delta')
    fig.show()
  else:
    print('JSON is empty')

##################################################################

def detectOI(sym):

  url = 'https://api.coinalyze.net/v1/open-interest-history?symbols='+sym+'&from='+str(before)+'&to='+str(now)+'&interval=15min&convert_to_usd=false&api_key='+api

  print(url)

  df = requests.get(url).json()
  dumps = json.dumps(df)
  loads = json.loads(dumps)

  if len(loads) > 0:
    ticker = loads[0]['symbol']

    df = pd.DataFrame(loads[0]['history'])

    # Convert unix timestamps to datetime
    df['datetime'] = pd.to_datetime(df['t'], unit='s')

    # Calculate percentage change
    df['change'] = (df['h'] - df['l']) / df['l'] * 100

    # Check if change exceeds 10%
    mask = df['change'] > 5

    # Perform action on subset where true
    df.loc[mask, 'alert'] = 1

    # Get starting o/h/l/c values
    start_o = df['o'].iloc[0]
    start_h = df['h'].iloc[0]
    start_l = df['l'].iloc[0]
    start_c = df['c'].iloc[0]

    # Calculate min value
    min_value = min(start_o, start_h, start_l, start_c)

    # Normalize columns
    df['open'] = (df['o'] - min_value) / min_value
    df['high'] = (df['h'] - min_value) / min_value
    df['low'] = (df['l'] - min_value) / min_value
    df['close'] = (df['c'] - min_value) / min_value

    # Create a candlestick chart using plotly
    candlestick = go.Candlestick(x=df['datetime'], open=df["open"], high=df["high"], low=df["low"], close=df["close"])

    # Create a layout object
    layout = go.Layout(title=ticker, yaxis_title="OI (%)", xaxis_rangeslider_visible=False)

    # Create a Figure object
    fig = go.Figure(data=[candlestick], layout=layout)

    # Show the chart
    fig.update_yaxes(tickformat='.2%')

    # Add spike annotations
    fig.add_trace(go.Scatter(
      x = df[df['alert']==1]['datetime'],
      y = df[df['alert']==1]['high'],
      mode = 'markers',
      marker = dict(color='black',size=10)
    ))
    fig.show()

  else:
    print('JSON is empty')

##################################################################

ticker = 'SRM_USDT.Y'
getPrice(ticker)
detectOI(ticker)
getDelta(ticker)
#getOI(ticker)