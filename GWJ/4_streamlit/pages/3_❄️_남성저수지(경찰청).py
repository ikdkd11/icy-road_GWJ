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


st.header('위험구간 네번째 - 세풍대교', divider='rainbow')    
st.subheader('<세풍대교 - 초남1교 - 초남터널>')
st.write('주소: 전라남도 광양시 광양읍 초남리')    

map3_1 = mapp1.map13
map3_2 = mapp2.map23
box33 = plotbox.box3
table33 = tta.grbp3
table3 = tta.average_temperatures3
grph3 = tot3.grp33

col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위험구간4(세풍대교-초남1교-초남터널) 위성사진',
                  '지도 시각화(1차 관측)',
                  '지도 시각화(2차 관측)'
                  ])
image_url = (
    "https://github.com/ikdkd11/dashboard/blob/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%84%B8%ED%92%8D%EB%8C%80%EA%B5%90.png?raw=true"
)               
response = requests.get(image_url)
image1 = Image.open(BytesIO(response.content))
with col2:
    if option == '위험구간4(세풍대교-초남1교-초남터널) 위성사진':
        st.image(image_url)  # 해당 이미지 파일의 경로
    elif option == '지도 시각화(1차 관측)':
        col2.plotly_chart(map3_1, height = 1080, use_container_width = True)
    elif option == '지도 시각화(2차 관측)':
        col2.plotly_chart(map3_2, height = 1080, use_container_width = True)

st.subheader('위험구간4(세풍대교-초남1교-초남터널) 1~4차 관측회차 별 시계열 그래프 및 박스그림                                                                               ')
col1, col2 = st.columns([1,1])
col1.plotly_chart(grph3, use_container_width = True)
with col2:
    tab1, tab2, tab3 = st.tabs(["Table", "Graph1", "Graph2"])
    with tab1:
       st.subheader('위험구간(세풍대교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 비교')
       st.table(table3.head(5))
    with tab2:
         st.plotly_chart(table33, use_container_width=True)
    with tab3:
        st.plotly_chart(box33, use_container_width=True)