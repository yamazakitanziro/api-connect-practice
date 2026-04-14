import streamlit as st
st.title("운동 루틴 추천 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"

#관심코인 선택
관심코인 = st.selectbox("코인 선택", ["BTC", "ETH", "XRP"])
url2 = f"https://api.upbit.com/v1/ticker?markets=KRW-{관심코인}"
response2 = requests.get(url2)
관심코인가격=f"\{response2.json()[0]['trade_price']:,}"
st.write(f"현재가={관심코인가격}")
