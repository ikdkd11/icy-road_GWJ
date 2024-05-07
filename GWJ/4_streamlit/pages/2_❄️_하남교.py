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
import tta

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
st.header('위험구간 두번째 - 옥전교', divider='rainbow')
st.subheader('<옥전교(남해고속도로 고각하부 - 옥전교)>')
st.write('주소: 전남 보성군 벌교읍 칠동리 옥전교')    
grbp22 = tta.grbp2
#1차 위험지역 지도 시각화 자료 호출
map2_1 = mapp1.map21
map2_2 = mapp1.map22
map2_3 = mapp1.map23
map2_4 = mapp1.map24
table2 = tta.average_temperatures2
#1~5번째 위험지역 별 시계열 그래프
grph2 = tot3.grp22

#1~5번째 위험지역 별 박스그림
box11 = plotbox.box1
box22 = plotbox.box2

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간2(남해고속도로 교차점 - 옥전교) 위성사진',
                  '위험구간2(남해고속도로 교차점 - 옥전교) 도로교차지점 거리뷰',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)',
                  '지도 시각화(3차 관측)',
                  '지도 시각화(4차 관측)'
                  ])
image_url2 = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%98%A5%EC%A0%84%EA%B5%90.png?raw=true"
)   
image_url3 = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EA%B5%90%EA%B0%81%ED%95%98%EB%B6%80.png?raw=true"
)            
response = requests.get(image_url2)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간2(남해고속도로 교차점 - 옥전교) 위성사진':
        st.image(image_url2)  # 해당 이미지 파일의 경로
    elif option == '위험구간2(남해고속도로 교차점 - 옥전교) 도로교차지점 거리뷰':
        st.image(image_url3)
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map2_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map2_2, height = 1080, use_container_width = True)
    elif option == '지도 시각화(3차 관측)':
        col2.plotly_chart(map2_3, height = 1080, use_container_width = True)
    elif option == '지도 시각화(4차 관측)':
        col2.plotly_chart(map2_4, height = 1080, use_container_width = True)
        # map1은 사전에 정의한 지도 객체
        # 예: map1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles="Stamen Terrain")
        #st.map(map1)  # 'map1'을 미리 정의하고 해당 객체를 여기에 표시
st.subheader('위험구간2(남해고속도로 고각하부-옥전교) 1~4차 관측회차 별 시계열 그래프 및 박스그림                                                                               ')
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph2, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('위험구간(옥전교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 비교')
       st.table(table2.head(5))
    with tab2:
         st.plotly_chart(grbp22, use_container_width=True)
    with tab3:
        st.plotly_chart(box22, use_container_width=True)

