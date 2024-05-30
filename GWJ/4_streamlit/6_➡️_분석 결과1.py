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
url1p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%EB%8B%A4%EB%A6%AC%EC%9E%90%EB%A3%8C.png'
url2p = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/streamlit_data/%ED%84%B0%EB%84%90%EC%9E%90%EB%A3%8C.png'
response1 = requests.get(url1p)
response2 = requests.get(url2p)
image1 = Image.open(BytesIO(response1.content))
image2 = Image.open(BytesIO(response2.content))

bar1r = result1.bar1
data1 = {
    "분류": ["1차 관측", "2차 관측", "3차 관측", "4차 관측", "전체"],
    "육상교각": ["2.7℃ 감소", "2.4℃ 감소", "2.9℃ 감소", "2.6℃ 감소", "2.7℃ 감소"],
    "수상교각": ["2.0℃ 감소", "1.6℃ 감소", "2.4℃ 감소", "2.1℃ 감소", "2.1℃ 감소"],
    "터널": ["4.7℃ 감소", "7.8℃ 감소", "4.8℃ 감소", "7.5℃ 감소", "6.2℃ 감소"]
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
st.header('■ 분석 결과1 - 교각, 터널마다 다르게 나타나는 노면온도 하락 패턴', divider='rainbow')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
    1. 교각, 터널에서만 노면온도가 짧은 시간(수 초 이내)동안에 급락(1℃ 이상 하강)<br>
    2. 교각의 경우, 육상교각에서 수상교각보다 노면온도가 0.5~0.8℃ 가량 크게 감소<br>
    3. 터널의 경우, 터널의 길이가 길수록 터널 출입구 주변의 노면온도의 하락 폭이 커지는 것으로 나타남
    </div>
    """, unsafe_allow_html=True)
st.plotly_chart(bar1r, use_container_width=True)
st.table(df1)
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
    ○ 육상교각의 노면온도가 수상교각의 노면온도 감소량보다 0.5~0.8℃ 가량 더 크게 감소하였음(수상교각의 노면온도 감소량 대비 1.3~1.5배 큼)<br>
    ○ 노면온도가 더 크게 감소하는 특성과 더불어 주변 지리환경에 따라 커브, 내리막 등 운전 상의 난점이 존재하는 육상교각의 특성을 고려했을 때 육상교각의 결빙사고 위험성이 높다고 판단됨<br>
    ○ 터널의 경우, 노면온도 변화 양상이 교각의 경우와 다르게 나타나는 특징이 존재하여 교각의 경우보다 더 큰 노면온도 감소효과를 보암(하단 그래프 참조)<br>
    </div>
    """, unsafe_allow_html=True)
st.header(' ')
col1, col2 = st.columns(2)
with col1:
    st.subheader('교각의 온도변화 그래프')
    st.image(image1, use_column_width=True, caption= '노면온도가 감소 후 유지, 기온 변화없음')
with col2:
    st.subheader('터널의 온도변화 그래프')
    st.image(image2, use_column_width=True, caption= '노면온도가 감소 후 유지, 기온 변화없음')
st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    <div class="big-font">
    ○ 교각 : 구간 진입 시 노면온도 급격하게 감소, 유지되는 특징을 보인 후 구간 이탈 시 노면온도 상승, 기온은 일정하게 유지됨<br>
    ○ 터널 : 터널 입구에서 노면온도가 감소 후 터널 진입 후 기온과 노면온도가 모두 급상승 후 터널 출구에서 두 온도가 모두 급락하는 특성을 보임<br>
    ○ 터널의 이러한 특성은 터널 길이가 길수록 강화되는 것이 관측됨(터널 길이가 길수록 온도 상승 폭과 하강 폭이 모두 비례함(하단 그래프 참조)
    </div>
    """, unsafe_allow_html=True)