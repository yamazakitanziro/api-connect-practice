import streamlit as st
st.title("운동 루틴 추천 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"
response = requests.get(url)
#st.write(response.json())

for coin in response.json():
    st.write(f"{coin['market']}현재가=\{coin['trade_price']:,}")

try:
    while True:
        response = requests.get(url)
        현재가=response.json()[0]['trade_price']
        목표가 = 140_000_000
        if 현재가 <= 목표가:
            st.write("BTC 매수 타이밍! 🚨")
        time.sleep(5)
except KeyboardInterrupt:
    st.write("\n프로그램을 종료합니다.")
