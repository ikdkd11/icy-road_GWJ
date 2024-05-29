import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
import json
import tot2
import plotbox
import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime
from PIL import Image
from folium.plugins import DualMap
from branca.colormap import LinearColormap
import mapp_main
import bmapp_main
import btot2
st.set_page_config(
    page_title="결빙관측 대시보드",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the route options
sig_list = ['구간A)첨단지구(과기원)-극락교(송정)', '구간B)일곡사거리~조선대입구']

# Sidebar selection for the route
sig_area = st.sidebar.selectbox("관측구간(A, B) 선택", sig_list)

# Define the header text based on the selected route
if sig_area == '구간A)첨단지구(과기원)-극락교(송정)':
    header_text = """
                <h2>
                <광주 A구간> 첨단지구(과기원)~극락교(송정) 결빙관측<br>
                관측회차 별 분석정보
                </h2>
                """
    st.markdown(header_text, unsafe_allow_html=True)
else:
    header_text = """
    <h2>
    <광주 B구간> 일곡사거리(일곡지구)~조선대입구(동구청) 결빙관측<br> 
    관측회차 별 분석정보
    </h2>
    """
    st.markdown(header_text, unsafe_allow_html=True)

# Display the header
#st.header(header_text, divider='rainbow')

# Your existing code for grp1, grp2, mapm1, mapm2
#송정 관측 시각화
grpp1 = tot2.grp1
grpp2 = tot2.grp2
mmap1 = mapp_main.mapm1
mmap2 = mapp_main.mapm2

#북구 관측 시각화
bmmap1 = bmapp_main.bmapm1
bmmap2 = bmapp_main.bmapm2
bgrpp1 = btot2.grp1
bgrpp2 = btot2.grp2


# The rest of your Streamlit code goes here

tab1, tab2 = st.tabs(["1차 관측", "2차 관측"])
if sig_area == '구간A)첨단지구(과기원)-극락교(송정)':
    with tab1:
    # 첫 번째 차트
        st.subheader('1월 28일 17시 발표 : 예보 중점 사항')
        st.markdown(
            '''
            1. 모레까지 아침 기온 낮아 춥겠음, 낮/밤의 기온차 큼
            2.  :blue[빙판길]과 :red[도로 살얼음] 주의
            ''')
        st.subheader("1월 29일 광주ASOS 기상관측 정보(06시/07시)")
        st.markdown(
            '''
            1. 06시 : 1. 기온 -1.4 °C, 2. 습도 89%, 3. 운량 하층운 9할, 4. 지면온도 -1.2 °C, 풍속 0.7m/s 
            2. 07시 : 1. 기온 -0.9 °C, 2. 습도 82%, 3. 운량 하층운 9할, 4. 지면온도 -1.0 °C, 풍속 1.1m/s 
            3. 전일(28일) 총 일사/ 평균 일조율 : 11.22 MJ/m^2, 64.4%
            '''
        )
        st.plotly_chart(grpp1, use_container_width=True)
        st.subheader('첨단(과기원)~극락교(송정)구간 1차 관측 노면온도 지도 시각화') 
        st.plotly_chart(mmap1, use_container_width=True)
    with tab2:
    # 두 번째 차트
        st.subheader('2월 6일 17시 발표 : 예보 중점 사항')
        st.markdown(
            '''
            1. 오늘(6일) 밤까지 빗방울 또는 눈 날림. :red[도로 살얼음] 주의
            ''')
        st.subheader("2월 7일 광주ASOS 기상관측 정보(06시/07시)")
        st.markdown(
            '''
            1. 06시 : 1. 기온 1.0 °C, 2. 습도 80%, 3. 운량 하층운 7할, 4. 지면온도 0.5 °C, 풍속 1.3m/s 
            2. 07시 : 1. 기온 0.6 °C, 2. 습도 76%, 3. 운량 하층운 2할, 4. 지면온도 0.3 °C, 풍속 1.7m/s 
            3. 전일(6일) 총 일사/ 평균 일조율 : 4.88 MJ/m^2, 0.0%
            '''
        )
        st.plotly_chart(grpp2, use_container_width=True)
        st.subheader('첨단(과기원)~극락교(송정)구간 2차 관측 노면온도 지도 시각화')
        st.plotly_chart(mmap2, use_container_width=True)   
else:
    with tab1:
    # 첫 번째 차트
        st.subheader('2월 25일 17시 발표 : 예보 중점 사항')
        st.markdown(
            '''
            1. 모레까지 아침 기온 낮아 춥겠음, 낮/밤의 기온차 큼
            2.  :blue[빙판길]과 :red[도로 살얼음] 주의
            ''')
        st.subheader("2월 26일 광주ASOS 기상관측 정보(06시/07시)")
        st.markdown(
            '''
            1. 06시 : 1. 기온 -1.4 °C, 2. 습도 89%, 3. 운량 하층운 9할, 4. 지면온도 -1.2 °C, 풍속 0.7m/s 
            2. 07시 : 1. 기온 -0.9 °C, 2. 습도 82%, 3. 운량 하층운 9할, 4. 지면온도 -1.0 °C, 풍속 1.1m/s 
            3. 전일(28일) 총 일사/ 평균 일조율 : 11.22 MJ/m^2, 64.4%
            '''
        )
        st.plotly_chart(bgrpp1, use_container_width=True)
        st.subheader('일곡사거리(일곡지구)~조선대입구(동구청)구간 1차 관측 노면온도 지도 시각화') 
        st.plotly_chart(bmmap1, use_container_width=True)
    with tab2:
    # 두 번째 차트
        st.subheader('2월 26일 17시 발표 : 예보 중점 사항')
        st.markdown(
            '''
            1. 오늘(6일) 밤까지 빗방울 또는 눈 날림. :red[도로 살얼음] 주의
            ''')
        st.subheader("2월 27일 광주ASOS 기상관측 정보(06시/07시)")
        st.markdown(
            '''
            1. 06시 : 1. 기온 1.0 °C, 2. 습도 80%, 3. 운량 하층운 7할, 4. 지면온도 0.5 °C, 풍속 1.3m/s 
            2. 07시 : 1. 기온 0.6 °C, 2. 습도 76%, 3. 운량 하층운 2할, 4. 지면온도 0.3 °C, 풍속 1.7m/s 
            3. 전일(6일) 총 일사/ 평균 일조율 : 4.88 MJ/m^2, 0.0%
            '''
        )
        st.plotly_chart(bgrpp2, use_container_width=True)
        st.subheader('일곡사거리(일곡지구)~조선대입구(동구청)구간 2차 관측 노면온도 지도 시각화')
        st.plotly_chart(bmmap2, use_container_width=True)   
#5
#st_folium(mmap1, width=1000)
#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean_map1, use_container_width = True) 
#col2.plotly_chart(vis_trade_rent1, use_container_width = True)


#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean1, use_container_width = True)
#col2.plotly_chart(trade_count1, use_container_width = True)


