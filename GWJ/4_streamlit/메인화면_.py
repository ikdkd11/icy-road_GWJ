import pandas as pd
import os
import geopandas as gpd
import glob
import plotly.express as px
import plotly.graph_objects as go
import folium
# import folium
import json
# import math
import tot2
import plotbox
import streamlit as st
from streamlit.components.v1 import html
from datetime import datetime
from PIL import Image
from folium.plugins import DualMap
from branca.colormap import LinearColormap
import mapp5

st.set_page_config(
    page_title="결빙관측 대시보드",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded"
)#fd
st.header('2024년 2번국도(보성(초당교차로)~광양(마룡교)) 결빙관측 관측회차 별 분석정보', divider='rainbow') 
vis_trade_rent1 = tot2.grp2
trade_count1 = tot2.grp4
trade_mean1 = tot2.grp3            
trade_mean_map1 = tot2.grp1
mmap1 = mapp5.map61
mmap2 = mapp5.map62
mmap3 = mapp5.map63
mmap4 = mapp5.map64


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


tab1, tab2, tab3, tab4 = st.tabs(["1차 관측", "2차 관측", "3차 관측", "4차 관측"])
with tab1:
# 첫 번째 차트
    st.subheader('1월 10일 16시 발표 : 예보 중점 사항')
    st.markdown(
        '''
        1. 내일(11일) 새벽부터 오전 사이 내륙을 중심으로 :blue[짙은 안개]가 끼는 곳이 있겠습니다.
        2.  :blue[내린 비]가 얼어 :red[도로 살얼음]이 나타나는 곳이 있겠습니다.
        ''')
    st.subheader("1차 관측 시기 기상관측 정보(17시 ~ 19시)")
    st.markdown(
        '''
        1. 보성/순천/광양 평균 풍향풍속 : 보성 <WNW, 5.4m/s>, 순천 <NNW, 2.4m/s>, 광양 <N, 1.7m/s>.
        2. 관측구간 내 평균 습도 : 56%
        3. 1월 10일 총 일사량 : 8.74 MJ/m^2, 평균 일조율 : 0.43hr
        '''
    )
    st.plotly_chart(trade_mean_map1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 1차관측 노면온도 정보 지도 시각화') 
    st.plotly_chart(mmap1, use_container_width=True)
with tab2:
# 두 번째 차트
    st.subheader('1월 11일 04시 발표 : 예보 중점 사항')
    st.markdown(
        '''
        1. 오늘(11일) 아침(09시)까지 내륙을 중심으로 가시거리 200m 미만의 :blue[짙은 안개]가, 그 밖의 지역에도 가시거리 1km 미만의 :blue[안개]가 끼는 곳이 있겠습니다.
        2. 오늘(11일) :blue[안개]가 지면에서 얼어 붙어 :red[도로 살얼음]이 나타나는 곳이 있어 도로가 더욱 미끄럽겠으니, 보행자와 교통 안전에 각별히 유의하시기 바랍니다. 
        3. (하늘 상태) 오늘(11일)은 대체로 맑다가 오후부터 차차 흐려지겠습니다.
        4
        ''')
    st.subheader("2차 관측 시기 기상관측 정보(07시 ~ 08시)")
    st.markdown(
        '''
        1. 보성/순천/광양 평균 풍향풍속 : 보성 <NW, 4.7/s>, 순천 <WNW, 1.5m/s>, 광양 <WNW, 1.3m/s>.
        2. 관측구간 내 평균 습도 : 73%
        3. 1월 10일 총 일사량 : 8.74 MJ/m^2, 평균 일조율 : 0.43hr
        '''
    )
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 2차관측 노면온도 시계열 그래프')
    st.plotly_chart(vis_trade_rent1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 2차관측 노면온도 정보 지도 시각화')
    st.plotly_chart(mmap2, use_container_width=True)   
with tab3:
# 세 번째 차트
    st.subheader('1월 24일 16시 발표 : 특보 및 예보 중점 사항')
    st.markdown(
        '''
        1. 강풍주의보: 보성, 여수, 광양 순천 등/ 풍랑주의보: 남해서부 전해상
        2. 모레(26일) 아침까지 광주와 전남 대부분 지역에서 기온이 낮고, 바람도 강해 춥겠습니다.
        3. 최근 눈이 쌓인 지역에서는 :red[빙판길]과 :red[도로 살얼음]이 나타나는 곳도 있겠습니다.
        ''')
    st.subheader("3차 관측 시기 기상관측 정보(18시 ~ 19시)")
    st.markdown(
        '''
        1. 보성/순천/광양 평균 풍향풍속 : 보성 <NW, 5.5m/s>, 순천 <NW, 3.9m/s>, 광양 <WNW, 4.7m/s>.
        2. 관측구간 내 평균 습도 : 53%
        3. 1월 24일 총 일사량 : 13.86 MJ/m^2, 평균 일조율 : 0.86hr
        '''
    )
    st.plotly_chart(trade_mean1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 3차관측 노면온도 정보 지도 시각화')
    st.plotly_chart(mmap3, use_container_width=True)
with tab4:
# 네 번째 차트
    st.subheader('1월 25일 04시 발표 : 특보 및 예보 중점 사항')
    st.markdown(
        '''
        1. 강풍주의보(06시 해제): 보성, 여수, 광양, 순천 / 풍랑주의보(06시 해제): 남해서부 전해상
        2. 내일(26일) 아침까지 광주와 전남 대부분 지역에서 기온이 낮고, 바람도 강해 춥겠습니다.
        3. 최근 눈이 쌓인 지역에서는 :red[빙판길]과 :red[도로 살얼음]이 나타나는 곳도 있겠습니다.
        ''')
    st.subheader("4차 관측 시기 기상관측 정보(06시 ~ 07시)")
    st.markdown(
        '''
        1. 보성/순천/광양 평균 풍향풍속 : 보성 <WNW, 2.6m/s>, 순천 <SSE, 1.2m/s>, 광양 <NW, 3.1m/s>.
        2. 관측구간 내 평균 습도 : 60%
        3. 1월 24일 총 일사량 : 13.86 MJ/m^2, 평균 일조율 : 0.86hr
        '''
    )
    st.plotly_chart(trade_count1, use_container_width=True)
    st.subheader('2번국도(보성(초당교차로)~광양(마룡교)) 4차관측 노면온도 정보 지도 시각화')
    st.plotly_chart(mmap4, use_container_width=True)

#5
#st_folium(mmap1, width=1000)
#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean_map1, use_container_width = True) 
#col2.plotly_chart(vis_trade_rent1, use_container_width = True)


#col1, col2 = st.columns([1,1])
#col1.plotly_chart(trade_mean1, use_container_width = True)
#col2.plotly_chart(trade_count1, use_container_width = True)


