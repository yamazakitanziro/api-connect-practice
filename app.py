import streamlit as st
st.title("코인 앱 🏋️")

import requests
import time
url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC,KRW-ETH,KRW-XRP"

#관심코인 현제가 확인
관심코인 = st.selectbox("코인 선택", ["BTC", "ETH", "XRP"])
url2 = f"https://api.upbit.com/v1/ticker?markets=KRW-{관심코인}"
response2 = requests.get(url2)
현재가=response2.json()[0]['trade_price']
#문자열이라서 숫자와 비교는 불가 
st.write(f"현재가={현재가:,}")


if "가격기록" not in st.session_state:
    st.session_state.가격기록 = []
st.session_state.가격기록.append(현재가)
st.write(st.session_state.가격기록)
st.line_chart(st.session_state.가격기록)


#사용자 입력 감시기능
목표가 = st.text_input("감시 목표가 입력",key="input")
if "running" not in st.session_state:
    st.session_state.running = False
if st.button("시작"):
    st.session_state.running = True
if st.button("중지"):
    st.session_state.running = False

placeholder = st.empty()
if st.session_state.running:   
    if 현재가 <= int(목표가):
        placeholder.write("BTC 매수 타이밍! 🚨")
    else:
        placeholder.write("탐지중")
    time.sleep(2)
    st.rerun()
