import streamlit as st
st.title("운동 루틴 추천 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"

#관심코인 선택
st.write("비트:0,이더:1,리플:2 선택")
관심코인 = st.button("선택")
response = requests.get(url)
관심코인가격=\{response.json()[관심코인]['trade_price']:,}
st.write(f"현재가={관심코인가격}")
