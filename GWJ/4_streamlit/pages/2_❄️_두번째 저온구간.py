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
import btot
import mapp1
import mapp2
import bmapp2
import bmapp1
import tta

sig_list = ['구간A)첨단지구(과기원)-극락교(송정)', '구간B)일곡사거리~조선대입구']
option = st.sidebar.selectbox("관측구간(A, B) 선택", sig_list)
sig_area = option
# Define the header text based on the selected route
if sig_area == '구간A)첨단지구(과기원)-극락교(송정)':
    st.header('저온구간 두번째 - 사암로', divider='rainbow')
    st.subheader('<사암로> 총 길이 1.3km')
    st.write('주소: 광주광역시 광산구 장덕동')  

    map2_1 = mapp1.map12
    map2_2 = mapp2.map22
    grph2 = tot3.grp22
    table2 = tta.average_temperatures2
    table22 = tta.grbp2
    box22 = plotbox.box2

    col1, col2 = st.columns([1,1])
    with col1:
        option = st.selectbox('표시 이미지 선택:',
                    ['저온구간2(사암로) 정면 사진',
                    '지도 시각화(1차 관측)',
                    '지도 시각화(2차 관측)'
                    ])
    image_url = (
        "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/streamlit_data/%EC%82%AC%EC%95%94%EB%A1%9C%20%EC%A0%84%EA%B2%BD.png"
    )               
    response = requests.get(image_url)
    image1 = Image.open(BytesIO(response.content))
    with col2:
        if option == '저온구간2(사암로) 정면 사진':
            st.image(image_url)  # 해당 이미지 파일의 경로
        elif option == '지도 시각화(1차 관측)':
            col2.plotly_chart(map2_1, height = 1080, use_container_width = True)
        elif option == '지도 시각화(2차 관측)':
            col2.plotly_chart(map2_2, height = 1080, use_container_width = True)
            # map1은 사전에 정의한 지도 객체
            # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
            #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시

    st.subheader('저온구간2(사암로) 관측회차 별 시계열 그래프 및 박스그림')        
    col1, col2 = st.columns([1,1])
    col1.plotly_chart(grph2, use_container_width = True)

    with col2:
        tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
        with tab1:
            st.subheader('사암로 저온구간 및 일반구간 노면온도 비교')
            st.table(table2.head(5))
        with tab2:
            st.plotly_chart(table22, use_container_width=True)
        with tab3:
            st.plotly_chart(box22, use_container_width=True)        
else:
    st.header('구간B) 첫번째 저온구간  -  국립광주박물관(서광주IC)', divider='rainbow')
    grbp22 = tta.grbp1

    #1차 위험지역 지도 시각화 자료 호출
    bmap2_1 = bmapp1.map12
    bmap2_2 = bmapp2.map22

    table2 = tta.average_temperatures1
    #1~5번째 위험지역 별 시계열 그래프
    bgrph = btot.grp22

    #1~5번째 위험지역 별 박스그림
    box11 = plotbox.box1

    col1, col2 = st.columns([1,1])
    with col1:
        option = st.selectbox('표시 이미지 선택:',
                    [
                    '최저 노면온도 관측구간 전경',
                    '지도 시각화(1차 관측)',
                    '지도 시각화(2차 관측)'
                    ])
    image_url2 = (
        "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%98%A5%EC%A0%84%EA%B5%90.png?raw=true"
    )   
    image_url3 = (
        "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/%EC%82%AC%EC%A7%841.png"
    )            
    response = requests.get(image_url3)
    image1 = Image.open(BytesIO(response.content))
    with col2:
        if option == '최저 노면온도 관측구간 전경':
            st.image(image_url3)  # 해당 이미지 파일의 경로
        elif option == '지도 시각화(1차 관측)':
            col2.plotly_chart(bmap2_1, height = 1080, use_container_width = True)
        elif option == '지도 시각화(2차 관측)':
            col2.plotly_chart(bmap2_2, height = 1080, use_container_width = True)
            # map1은 사전에 정의한 지도 객체
            # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
            #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
        st.subheader('구간B)첫번째 저온구간- 국립광주박물관(서광주IC) 관측회차 별 시계열 그래프 및 박스그림                                                                               ')
    col1, col2 = st.columns([1,1])
    col1.plotly_chart(bgrph, use_container_width = True)
    with col2:
        tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
        with tab1:
            st.subheader('저온구간 및 일반구간 노면온도 비교')
        st.table(table2.head(5))
        with tab2:
            st.plotly_chart(grbp22, use_container_width=True)
        with tab3:
            st.plotly_chart(box11, use_container_width=True)
