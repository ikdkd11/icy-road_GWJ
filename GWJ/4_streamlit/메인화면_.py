import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
# import folium
import json
# import math
import tot2
import plotbox
import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime
from PIL import Image
from folium.plugins import DualMap
from branca.colormap import LinearColormap
import mapp_main

st.set_page_config(
    page_title="결빙관측 대시보드",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)#fd
st.header('2024년 광주광역시 첨단(과기원)~극락교(송정) 결빙관측 관측회차 별 분석정보', divider='rainbow') 
grpp1 = tot2.grp1
grpp2 = tot2.grp2
mmap1 = mapp_main.mapm1
mmap2 = mapp_main.mapm2

sig_list = ['첨단-극락교','북구-서구']
sig_area = st.sidebar.selectbox(
    "관측경로 선택"
)
tab1, tab2 = st.tabs(["1차 관측", "2차 관측"])
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

#5
#st_folium(mmap1, width=1000)
#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean_map1, use_container_width = True) 
#col2.plotly_chart(vis_trade_rent1, use_container_width = True)


#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean1, use_container_width = True)
#col2.plotly_chart(trade_count1, use_container_width = True)


