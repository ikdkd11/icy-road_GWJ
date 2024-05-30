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


st.header('저온구간 세번째 - 남성저수지(용아로-금봉로)', divider='rainbow')    
st.subheader('<남성저수지(광주광역시 경찰청) 주변 도로')
st.write('주소: 광주광역시 용아로112(소촌동)')    

map3_1 = mapp1.map13
map3_2 = mapp2.map23
box33 = plotbox.box3
table33 = tta.grbp3
table3 = tta.average_temperatures3
grph3 = tot3.grp33

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['저온구간3 남성저수지 주변 도로 사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)'
                  ])
image_url = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/streamlit_data/%EB%82%A8%EC%84%B1%EC%A0%80%EC%88%98%EC%A7%80.png"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '저온구간3 남성저수지 주변 도로 사진':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map3_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map3_2, height = 1080, use_container_width = True)

st.subheader('저온구간3(남성저수지) 관측회차 별 시계열 그래프 및 박스그림')
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph3, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('남성저수지 주변 도로 저온구간 및 일반구간 노면온도 비교')
       st.table(table3.head(5))
    with tab2:
         st.plotly_chart(table33, use_container_width=True)
    with tab3:
        st.plotly_chart(box33, use_container_width=True)