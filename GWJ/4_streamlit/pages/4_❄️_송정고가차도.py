import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
import json
import math
import plotbox
import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime
from PIL import Image
import requests
from io import BytesIO
import tot3
import mapp1
import mapp2
import tta

st.header('저온구간 네번째 - 송정고가차도', divider='rainbow')    
st.subheader('총 연장 : 1.2 km')
st.write('주소: 광주광역시 광산구 신촌동 1014-5')
map4_1 = mapp1.map14
map4_2 = mapp2.map24
box44 = plotbox.box4
table44 = tta.grbp4
table4 = tta.average_temperatures4
grph4 = tot3.grp44

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['저온구간4(송정고가차도) 전경',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)'
                  ])
image_url = (
    "https://github.com/ikdkd11/icy-road_GWJ/blob/main/GWJ/0_data/streamlit_data/%EC%86%A1%EC%A0%95%EA%B3%A0%EA%B0%80.png?raw=true"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '저온구간4(송정고가차도) 전경':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map4_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map4_2, height = 1080, use_container_width = True)

col1, col2 = st.columns([1,1])
col1.plotly_chart(grph4, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('송정고가차도 주변 도로 저온구간 및 일반구간 노면온도 비교')
       st.table(table4.head(5))
    with tab2:
         st.plotly_chart(table44, use_container_width=True)
    with tab3:
        st.plotly_chart(box44, use_container_width=True)