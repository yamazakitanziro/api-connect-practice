import streamlit as st
st.title("코인 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"

#관심코인 현제가 확인
관심코인 = st.selectbox("코인 선택", ["BTC", "ETH", "XRP"])
url2 = f"https://api.upbit.com/v1/ticker?markets=KRW-{관심코인}"
response2 = requests.get(url2)
관심코인가격=f"{response2.json()[0]['trade_price']:,}"
st.write(f"현재가={관심코인가격}")


#사용자 입력 감시기능
목표가 = st.text_input("목표가 입력",key="input")

while True:
    관심코인가격=f"\{response2.json()[0]['trade_price']:,}"
    if 관심코인가격 <= 목표가:
        placeholder.write("BTC 매수 타이밍! 🚨")
    else:
        placeholder.write("탐지중")
    time.sleep(15)
