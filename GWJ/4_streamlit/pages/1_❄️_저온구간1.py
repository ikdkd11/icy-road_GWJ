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

# 스트림릿 페이지에 HTML 컴포넌트 추가
sig_list = ['구간A)첨단(과기원)-극락교(송정)', '구간B)일곡사거리~조선대입구']

# Sidebar selection for the route
option = st.sidebar.selectbox("관측경로 선택", sig_list)
sig_area = option
# Define the header text based on the selected route
if sig_area == '구간A)첨단(과기원)-극락교(송정)':
    st.header('구간A) 첫번째 저온구간  - 하남교', divider='rainbow')
    st.subheader('<하남교> 총 길이 80m, 총 폭 39m, 높이 4.6m')
    st.write('주소: 광주광역시 광산구 장덕동, 도천동')    
    grbp22 = tta.grbp1

    #1차 위험지역 지도 시각화 자료 호출
    map1_1 = mapp1.map11
    map1_2 = mapp2.map21

    table2 = tta.average_temperatures1
    #1~5번째 위험지역 별 시계열 그래프
    grph = tot3.grp11

    #1~5번째 위험지역 별 박스그림
    box11 = plotbox.box1

    col1, col2 = st.columns([1,1])
    with col1:
        option = st.selectbox('표시 이미지 선택:',
                    [
                    '하남교 측면 사진',
                    '지도 시각화(1차 관측)',
                    '지도 시각화(2차 관측)'
                    ])
    image_url2 = (
        "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%98%A5%EC%A0%84%EA%B5%90.png?raw=true"
    )   
    image_url3 = (
        "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/streamlit_data/%ED%95%98%EB%82%A8%EA%B5%902.png"
    )            
    response = requests.get(image_url3)
    image1 = Image.open(BytesIO(response.content))
    with col2:
        if option == '하남교 측면 사진':
            st.image(image_url3)  # 해당 이미지 파일의 경로
        elif option == '지도 시각화(1차 관측)':
            col2.plotly_chart(map1_1, height = 1080, use_container_width = True)
        elif option == '지도 시각화(2차 관측)':
            col2.plotly_chart(map1_2, height = 1080, use_container_width = True)
            # map1은 사전에 정의한 지도 객체
            # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
            #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
        st.subheader('저온구간1(하남교) 관측회차 별 시계열 그래프 및 박스그림                                                                               ')
    col1, col2 = st.columns([1,1])
    col1.plotly_chart(grph, use_container_width = True)
    with col2:
        tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
        with tab1:
            st.subheader('하남교 저온구간 및 일반구간 노면온도 비교')
        st.table(table2.head(5))
        with tab2:
            st.plotly_chart(grbp22, use_container_width=True)
        with tab3:
            st.plotly_chart(box11, use_container_width=True)

else:
    st.header('구간B) 첫번째 저온구간  -  운암고가', divider='rainbow')