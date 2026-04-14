import streamlit as st
st.title("운동 루틴 추천 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"

#현재가격 확인
response = requests.get(url)
for coin in response.json():
    print(f"{coin['market']}현재가=\{coin['trade_price']:,}")

#사용자 입력 감시기능
목표가 = st.text_input("입력하시오",key="input")

while True:
    response = requests.get(url)
    현재가=response.json()[0]['trade_price']
    if 현재가 <= 목표가:
        placeholder.write("BTC 매수 타이밍! 🚨")
    else:
        placeholder.write(f"현재가: {현재가}")
    time.sleep(5)
