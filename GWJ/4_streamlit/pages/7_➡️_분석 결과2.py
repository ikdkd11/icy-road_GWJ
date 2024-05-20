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
import mapp4
import tta
import result1
url2p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%EB%83%89%EA%B0%81%EC%A4%91%EC%B2%A9.png'
url1p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%EB%83%89%EA%B0%81%EC%A4%91%EC%B2%A91.png'
url3p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%84%B8%ED%92%8D%EB%8C%80%EA%B5%90%20%EB%83%89%EA%B0%81.png'
url4p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%EC%B4%88%EB%82%A81%EA%B5%90%20%EB%83%89%EA%B0%81.png'

response1 = requests.get(url1p)
response2 = requests.get(url2p)
response3 = requests.get(url3p)
response4 = requests.get(url4p)

image1 = Image.open(BytesIO(response1.content))
image2 = Image.open(BytesIO(response2.content))
image3 = Image.open(BytesIO(response3.content))
image4 = Image.open(BytesIO(response4.content))

bar1r = result1.bar1
data1 = {
    "순서": ["첫 번째 위험구간", "두 번째 위험구간", "세 번째 위험구간-1", "세 번째 위험구간-2", "네 번째 위험구간", "다섯 번째 위험구간"],
    "구간 상세": ["초당교 ~ 심정리 버스정류장", "열가재 주유소 ~ 옥전교", "벌교대교", "장양육교", "세풍대교 ~ 초남1교 ~ 초남터널", "중군터널 ~ 마룡교"],
    "노면온도 감소량": ["3.5℃ 감소", "3.1℃ 감소","1.2℃ 감소","2.1℃ 감소","1.9℃ 감소" ,"6.3℃ 감소"],
    "주소": ["보성군 미력면 초당리 713-5", "보성군 벌교읍 칠동리 1115-1", "보성군 벌교읍 장좌리", "보성군 벌교읍 장양리515", "광양시 광양읍 초남리 산79-11", "광양시 옥곡면 신금리 6-1"],
    "구간 총 길이": ["1.4km", "1.3km", "0.4km", "0.7km", "3.3km","7.3km"]
}

df1 = pd.DataFrame(data1)

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

st.header('■ 분석 결과2 - 공통 위험구간 선정 및 특성', divider='rainbow')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
     공통 위험구간이란? 1~4차 관측에서 노면온도가 감소하는 정도가 크고 그 감소 양상이 일관되게 유지되는 구간들을 공통 위험구간으로 산출<br>
     공통 위험구간의 경우, 다리와 터널 혹은 다리와 다리가 연쇄적으로 이어져있는 구조로 이로 인해 노면온도가 연달아서 감소하여 다른 곳에 비해 결빙 가능성이 높음
    </div>
    """, unsafe_allow_html=True)
st.subheader(' ')
st.subheader('공통 위험구간 5곳 상세 정보')
st.table(df1)
st.markdown('')
st.subheader('공통 위험구간의 연쇄 노면 냉각')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
     > 연쇄 노면냉각이란? 다리, 터널 같이 노면온도를 감소시키는 구간이 연달아 이어지면서 냉각효과 역시 중첩되어 노면온도가 크게 낮아지고 구간을 벗어난 후에도 구간 이전에 비해 낮은 노면온도를 보이는 현상을 연쇄 노면 냉각이라 지정하였음<br>
     > 이러한 연쇄 노면냉각이 잘 드러난 사례를 아래쪽 표에 첨부함
    </div>
    """, unsafe_allow_html=True)
st.markdown(' ')
col1, col2 = st.columns([1,1])
with col1:
    option = st.selectbox('표시 이미지 선택:',
                 ['위성 사진으로 보는 네 번째 위험구간에서의 노면온도 감소 지점',
                  '노면온도 그래프로 보는 세풍대교와 초남1교에 의한 연쇄 냉각효과',
                  '세풍대교 사진',
                  '초남1교 사진'
                  ])
with col2:
    if option == '위성 사진으로 보는 네 번째 위험구간에서의 노면온도 감소 지점':
        st.image(image1)
    elif option == '노면온도 그래프로 보는 세풍대교와 초남1교에 의한 연쇄 냉각효과':
        st.image(image2)  # 해당 이미지 파일의 경로
    elif option == '세풍대교 사진':
        st.image(image3)  # 해당 이미지 파일의 경로
    elif option == '초남1교 사진':
        st.image(image4)  # 해당 이미지 파일의 경로'
st.markdown(" ")
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
     > 이러한 연쇄 노면냉각이 극대화 되는 지점이 다섯 번째 위험구간이었음<br>
     > 관측경로 상에서 가장 긴 터널인 중군터널로 인해 터널 출입구에서 노면온도가 크게 하락하였고 이어지는 교각들(신금1, 2, 3교, 수어천교, 마룡교)가 이어지는 구조임<br>
     > 이런 연유로 전체 관측 경로 상에서 노면온도가 가장 크게 감소하는 양상을 보였음 
    """, unsafe_allow_html=True)