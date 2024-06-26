import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import plotly.graph_objects as go
from PIL import Image
import streamlit as st

# 파일명과 해당 파일을 저장할 DataFrame 변수명 매핑
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/1stB.csv"
)
url2 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/2ndB.csv"
    )
url3 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/3rdB.csv"
    )
url4 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/4thB.csv"
    )
url5 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/5thB.csv"
)

df11 = pd.read_csv(url1)
df22 = pd.read_csv(url2)
df33 = pd.read_csv(url3)
df44 = pd.read_csv(url4)
df55 = pd.read_csv(url5)

# df22의 열 데이터 개수를 비교하여 솎아내는 함수
def balance_dataframe(df, col1, col2):
    len_col1 = df[col1].dropna().shape[0]
    len_col2 = df[col2].dropna().shape[0]

    if len_col1 > len_col2:
        diff = len_col1 - len_col2
        indices_to_remove = df[df[col1].notna()].index[::len_col1 // diff][:diff]
        df.loc[indices_to_remove, col1] = None
    elif len_col2 > len_col1:
        diff = len_col2 - len_col1
        indices_to_remove = df[df[col2].notna()].index[::len_col2 // diff][:diff]
        df.loc[indices_to_remove, col2] = None

    return df

# df22에서 '노면온도(1차)'와 '노면온도(2차)'의 데이터 개수를 맞추기
df22 = balance_dataframe(df22, '노면온도(1차)', '노면온도(2차)')

# plotly를 사용하여 그래프 그리기
def create_graph(df11):
    fig = go.Figure()

    # 기온 데이터 색상 (빨간색 계열)
    #temp_colors = ['rgb(255,0,0)', 'rgb(255,99,71)', 'rgb(255,69,0)', 'rgb(220,20,60)']
    # 노면온도 데이터 색상 (파란색 계열)
    road_temp_colors = [' rgb(204, 37, 41)', 'rgb(0, 158, 115)', 'rgb(255, 128, 0)', 'rgb(0, 114, 178)']

    #road_temp_colors = ['rgb(0,0,255)', 'rgb(30,144,255)', 'rgb(70,130,180)', 'rgb(100,149,237)']

    # 노면온도 데이터 추가
    for i in range(1, 3):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df11.index,  # 인덱스를 x축 데이터로 사용
            y=df11[f'노면온도({i}차)'],
            name=f'노면온도({i}차)',
            line=dict(color=road_temp_colors[i-1], width=2),
            connectgaps=True
        ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=dict(
            text='저온구간1: [하남교] - 관측 회차 별 노면온도 시계열 비교',
            font=dict(size=20, color="black")  # 볼드 폰트로 변경
        ),
        yaxis=dict(title='온도(°C)'),
        hovermode="x"
    )
    return fig
grp11 = create_graph(df11)

# NaN 값을 가진 행 제거

def create_graph(df22):
    fig = go.Figure()
    # 기온 데이터 색상 (빨간색 계열)
    #temp_colors = ['rgb(255,0,0)', 'rgb(255,99,71)', 'rgb(255,69,0)', 'rgb(220,20,60)']
    # 노면온도 데이터 색상 (파란색 계열)
    road_temp_colors = ['rgb(204, 37, 41)', 'rgb(0, 158, 115)']

    # 노면온도 데이터 추가
    for i in range(1, 3):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df22.index,  # 인덱스를 x축 데이터로 사용
            y=df22[f'노면온도({i}차)'],
            name=f'노면온도({i}차)',
            line=dict(color=road_temp_colors[i-1], width=2),
            connectgaps=True
        ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=dict(
            text='저온구간2: [사암로-하남산단] - 관측 회차 별 노면온도 시계열 비교',
            font=dict(size=20, color="black")  # 볼드 폰트로 변경
        ),
        
        yaxis=dict(title='온도(°C)'),
        hovermode="x"
    )
    return fig
grp22 = create_graph(df22)
grp22.show()

