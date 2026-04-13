import streamlit as st
st.title("운동 루틴 추천 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"
response = requests.get(url)
st.write(response.json())

for coin in response.json():
    st.write(f"{coin['market']}현재가=\{coin['trade_price']:,}")
