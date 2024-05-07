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
import mapp
import tta

box11 = plotbox.box1
map1_1 = mapp.map11
map1_2 = mapp.map12
map1_3 = mapp.map13
map1_4 = mapp.map14
table1 = tta.average_temperatures1
grph1 = tot3.grp11
grbp11 = tta.grbp1

# CSS를 이용하여 우측 상단에 텍스트를 고정시키는 HTML 코드
css_style = """
<style>
.fixed-top-right {
    position: fixed;
    top: 10px;
    right: 10px;
    background-color: transparent;
    padding: 8px;
    z-index: 999;
}
</style>
<div class="fixed-top-right">광주지방기상청 관측과 제공</div>
"""

# 스트림릿 페이지에 HTML 컴포넌트 추가
html(css_style)
st.header('위험구간 첫번째 - 초당교차로', divider='rainbow')    
st.subheader('<초당교차로 - 초당교>')
st.write('주소: 전라남도 보성군 보성읍 옥평리 952-8')
col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간1(초당교) 위성사진',
                  '최저온도 기록구간 사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)',
                  '지도 시각화(3차 관측)',
                  '지도 시각화(4차 관측)'
                  ])
image_url1 = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EA%B5%AC%EA%B0%84%EC%A0%84%EC%B2%B4-%EC%88%98%EC%A0%95.png?raw=true"
)
image_url2 = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%A0%80%EC%98%A8%EA%B5%AC%EA%B0%841.png?raw=true"
)               
#response = requests.get(image_url)
#image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간1(초당교) 위성사진':
        st.image(image_url1)
    elif option == '최저온도 기록구간 사진':
        st.image(image_url2)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map1_1, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map1_2, height = 1080, use_container_width = True)
    elif option == '지도 시각화(3차 관측)':
        col2.plotly_chart(map1_3, height = 1080, use_container_width = True)
    elif option == '지도 시각화(4차 관측)':
        col2.plotly_chart(map1_4, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시

st.subheader('위험구간1(초당교차로-초당교 구간) 1~4차 관측회차 별 시계열 그래프 및 박스그림                                                                               ')
col1, col2 = st.columns([1,1])
with col1:
    st.plotly_chart(grph1, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('위험구간(초당교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 비교')
       st.table(table1.head(5))
    with tab2:
         st.plotly_chart(grbp11, use_container_width=True)
    with tab3:
        st.plotly_chart(box11, use_container_width=True)