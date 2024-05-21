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

st.header('위험구간 세번째 - 벌교대교', divider='rainbow')    
st.subheader('<벌교대교 - 장양육교>')
st.write('주소: 전남 보성군 벌교읍 장좌리 벌교대교, 전라남도 보성군 벌교읍 장양리 장양육교')  

map2_1 = mapp1.map12
map2_2 = mapp2.map22
grph2 = tot3.grp22
table2 = tta.average_temperatures2
table22 = tta.grbp2
box22 = plotbox.box2

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간3(벌교대교-장양육교) 위성사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)'
                  ])
image_url = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EB%B2%8C%EA%B5%90%EB%8C%80%EA%B5%90.png?raw=true"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간3(벌교대교-장양육교) 위성사진':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map2_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map2_2, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시

st.subheader('위험구간3(벌교대교-장양육교) 1~4차 관측회차 별 시계열 그래프 및 박스그림                                                                               ')        
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph2, use_container_width = True)

with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('위험구간(벌교대교) 중 최저 노면온도 기록구간 별 노면온도 비교')
       st.table(table2.head(5))
    with tab2:
         st.plotly_chart(table22, use_container_width=True)
    with tab3:
        st.plotly_chart(box22, use_container_width=True)        