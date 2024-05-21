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

# CSS를 이용하여 우측 상단에 텍스트를 고정시키는 HTML 코드

st.header('저온구간 다섯번째 - 극락교', divider='rainbow')    
st.subheader('총 길이 380m, 총 너비 35m, 교량높이 8m')
st.write('주소: 광주광역시 광산구 신촌동')
map5_1 = mapp1.map15
map5_2 = mapp2.map25
box55 = plotbox.box5
table55 = tta.grbp5
table5 = tta.average_temperatures5
grph5 = tot3.grp55

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['저온구간5(극락교) 전경',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)'
                  ])
image_url = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/streamlit_data/%EA%B7%B9%EB%9D%BD%EA%B5%90.png"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '저온구간5(극락교) 전경':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map5_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map5_2, height = 1080, use_container_width = True)

col1, col2 = st.columns([1,1])
col1.plotly_chart(grph5, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('극락교 주변 도로 저온구간 및 일반구간 노면온도 비교')
       st.table(table5.head(5))
    with tab2:
         st.plotly_chart(table55, use_container_width=True)
    with tab3:
        st.plotly_chart(box55, use_container_width=True)