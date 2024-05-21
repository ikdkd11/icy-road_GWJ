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

st.header('위험구간 다섯번째 - 수어천교', divider='rainbow')    
st.subheader('<중군터널 - 신금1,2교 - 수어천교 - 마룡교>')
st.write('주소: 전라남도 광양시 옥곡면 신금리')
map5_1 = mapp1.map15
map5_2 = mapp2.map25
box55 = plotbox.box5
table55 = tta.grbp5
table5 = tta.average_temperatures5
grph5 = tot3.grp55

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간5(중군터널-신금1,2교-수어천교-마룡교) 위성사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)'
                  ])
image_url = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%88%98%EC%96%B4%EC%B2%9C%EA%B5%90.png?raw=true"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간5(중군터널-신금1,2교-수어천교-마룡교) 위성사진':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map5_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map5_2, height = 1080, use_container_width = True)

col1, col2 = st.columns([1,1])
col1.plotly_chart(table5, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('위험구간(옥전교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 비교')
       st.table(table5.head(5))
    with tab2:
         st.plotly_chart(table55, use_container_width=True)
    with tab3:
        st.plotly_chart(box55, use_container_width=True)