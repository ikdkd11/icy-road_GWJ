import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from PIL import Image
import streamlit as st

## 첨단교 1차 관측
#github로부터 관측데이터 불러오기(csv 파일로만 가능)
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/b1stall.csv"
)
url2 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/b2ndall.csv"
)
df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)
# NaN 값을 가진 행 제거
df1_cleaned = df1.dropna(subset=['기온','노면온도'])

# plotly를 사용하여 그래프 그리기
def create_graph(df1):
    fig = go.Figure()

    for location, color in zip(['기온', '노면온도'], [(255, 0, 0), (35, 35, 200)]):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df1['시간'],
            y=df1[location],
            name=location,
            line=dict(color=f'rgb{color}', width=1),  # 라인 색상 및 두께 설정
            connectgaps=True
        ))
    ## 교량 표시를 위한 주석 추가(과기원 앞 ~ 비아 지하차도)
    fig.add_annotation(
        x='2024-02-26 06:17:58',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:17:58', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '과학기술원 앞',
        showarrow=True,  # 화살표 표시 여부
        ax=5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=30,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    fig.add_annotation(
        x='2024-02-26 06:45:58',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:45:58', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '비아지하차도',
        showarrow=True,  # 화살표 표시 여부
        ax=15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=55,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(하남교IN)
    fig.add_annotation(
        x='2024-02-26 06:53:43',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:53:43', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '하남교IN',
        showarrow=True,  # 화살표 표시 여부
        ax=15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=55,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정


    ## 교량 표시를 위한 주석 추가(하남교OUT)
    fig.add_annotation(
        x='2024-02-26 06:56:04',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:56:04', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '하남교OUT',
        showarrow=True,  # 화살표 표시 여부
        ax=-15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(신단관리소 사거리)
    fig.add_annotation(
        x='2024-02-26 06:22:15',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:22:15', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '신단관리소 사거리',
        showarrow=True,  # 화살표 표시 여부
        ax=-10,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=85,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(흑석 사거리)
    fig.add_annotation(
        x='2024-02-26 06:27:52',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:27:52', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '흑석 사거리',
        showarrow=True,  # 화살표 표시 여부
        ax=-5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(원곡교IN)
    fig.add_annotation(
        x='2024-02-26 06:37:52',  # 주석을 달고 싶은 x축 좌표 위치
        y=df1_cleaned.loc[df1_cleaned['시간'] == '2024-02-26 06:37:52', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '원곡교 IN',
        showarrow=True,  # 화살표 표시 여부
        ax=-5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    fig.update_layout(
        title=dict(text='2월6일 일곡사거리~조선대입구 결빙rm 1차 관측 그래프<br>일몰시각 <07:34>, 관측시간<06:47 ~ 07:16>', x=0, font=dict(size=24, color="black", family="Arial Black"), xanchor='left',),
        xaxis=dict(
            title='날짜와 시간',
            range=[df1['시간'].min(), df1['시간'].max()],  # 데이터에서 최소 및 최대 시간으로 범위 설정
                tickformatstops = (
                        ## 1000밀리초까지의 tickformat
                        dict(dtickrange=(None,1000), value="%H:%M:%S.%L 밀리초"),
                        ## 1초 ~ 1분까지의 tickformat
                        dict(dtickrange=(1000, 60000), value="%H:%M:%S 초"),
                        ## 1분 ~ 1시간까지의 tickformat
                        dict(dtickrange=(60000, 3600000), value="%H:%M 분"),
                        ## 1시간 ~ 1일까지의 tickformat
                        dict(dtickrange=(3600000, 86400000), value="%H:%M 시"),
                        ## 1일 ~ 1주까지의 tickformat
                        dict(dtickrange=(86400000, 604800000), value="%e. %b 일"),
                        ## 1주 ~ 1월까지의 tickformat
                        dict(dtickrange=(604800000, "M1"), value="%e. %b 주"),
                        ## 1월 ~ 1년까지의 tickformat
                        dict(dtickrange=("M1", "M12"), value="%b '%y 월"),
                        ## 1년 이상의 tickformat
                        dict(dtickrange=("M12",None), value="%Y 년")
        )),
        yaxis=dict(title='온도(°C)'),
        hovermode="x",
    )
    fig.update_traces(hoverlabel=dict(font=dict(size=23)))
    return fig
grp1 = create_graph(df1)

## 첨단교 2차 관측
# 파일로부터 데이터 불러오기
# NaN 값을 가진 행 제거
df2_cleaned = df2.dropna(subset=['기온','노면온도'])

# plotly를 사용하여 그래프 그리기
def create_graph(df2):
    fig = go.Figure()

    for location, color in zip(['기온', '노면온도'], [(255, 0, 0), (35, 35, 200)]):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df2['시간'],
            y=df2[location],
            name=location,
            line=dict(color=f'rgb{color}', width=1),  # 라인 색상 및 두께 설정
            connectgaps=True
        ))


    ## 교량 표시를 위한 주석 추가(과기원 앞 ~ 비아 지하차도)
    fig.add_annotation(
        x='2024-02-27 06:14:49',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:14:49', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '과학기술원 앞 ~ 비아지하차도',
        showarrow=True,  # 화살표 표시 여부
        ax=5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=30,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    fig.add_annotation(
        x='2024-02-27 06:20:43',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:20:43', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '하남교',
        showarrow=True,  # 화살표 표시 여부
        ax=15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=55,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(하남교IN)
    fig.add_annotation(
        x='2024-02-27 06:23:02',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:23:02', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '산단구간 시작(6번로)',
        showarrow=True,  # 화살표 표시 여부
        ax=15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=55,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

       ## 교량 표시를 위한 주석 추가(하남교OUT)
    fig.add_annotation(
        x='2024-02-27 06:26:47',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:26:47', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '산단구간 종료(흑석사거리)',
        showarrow=True,  # 화살표 표시 여부
        ax=-15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기31
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정
    
    ## 교량 표시를 위한 주석 추가(하남교OUT)
    fig.add_annotation(
        x='2024-02-27 06:28:35',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:28:35', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '원곡교',
        showarrow=True,  # 화살표 표시 여부
        ax=-15,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(신단관리소 사거리)
    fig.add_annotation(
        x='2024-02-27 06:29:56',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:29:56', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '광주여대 입구',
        showarrow=True,  # 화살표 표시 여부
        ax=-10,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=85,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(흑석 사거리)
    fig.add_annotation(
        x='2024-02-27 06:33:30',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:33:30', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '남성 저수지',
        showarrow=True,  # 화살표 표시 여부
        ax=-5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(원곡교IN)
    fig.add_annotation(
        x='2024-02-27 06:36:06',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:36:06', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '송정 고가차도',
        showarrow=True,  # 화살표 표시 여부
        ax=-5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정

    ## 교량 표시를 위한 주석 추가(원곡교OUT)
    fig.add_annotation(
        x='2024-02-27 06:40:28',  # 주석을 달고 싶은 x축 좌표 위치
        y=df2_cleaned.loc[df2_cleaned['시간'] == '2024-02-27 06:40:28', '노면온도'].values[0],  # 해당 시간의 노면온도
        text = '극락교',
        showarrow=True,  # 화살표 표시 여부
        ax=-5,  # 화살표의 x축 방향 길이 (음수 값 사용하여 반대 방향으로 설정)
        ay=75,  # 화살표의 y축 방향 길이 (음수 값 사용하여 반대 방향으로 설정 # 화살표 방향을 반대로 설정
        arrowwidth=2,  # 화살표 선 굵기
        arrowsize=1.5,  # 화살표 크기
        bgcolor='rgb(0, 0, 0)',  # 노면온도 선 그래프의 색상과 일치하는 배경색
        font=dict(color='white', size=12))  # 글자색을 흰색으로 설정


    fig.update_layout(
        title=dict(text='2월7일 첨단-극락교 구간 노면 2차관측 그래프<br>일몰시각 <07:27>, 관측시간<06:14 ~ 06:41>', x=0, font=dict(size=24, color="black", family="Arial Black"), xanchor='left',),
        xaxis=dict(
            title='날짜와 시간',
            range=[df2['시간'].min(), df2['시간'].max()],  # 데이터에서 최소 및 최대 시간으로 범위 설정
                tickformatstops = (
                        ## 1000밀리초까지의 tickformat
                        dict(dtickrange=(None,1000), value="%H:%M:%S.%L 밀리초"),
                        ## 1초 ~ 1분까지의 tickformat
                        dict(dtickrange=(1000, 60000), value="%H:%M:%S 초"),
                        ## 1분 ~ 1시간까지의 tickformat
                        dict(dtickrange=(60000, 3600000), value="%H:%M 분"),
                        ## 1시간 ~ 1일까지의 tickformat
                        dict(dtickrange=(3600000, 86400000), value="%H:%M 시"),
                        ## 1일 ~ 1주까지의 tickformat
                        dict(dtickrange=(86400000, 604800000), value="%e. %b 일"),
                        ## 1주 ~ 1월까지의 tickformat
                        dict(dtickrange=(604800000, "M1"), value="%e. %b 주"),
                        ## 1월 ~ 1년까지의 tickformat
                        dict(dtickrange=("M1", "M12"), value="%b '%y 월"),
                        ## 1년 이상의 tickformat
                        dict(dtickrange=("M12",None), value="%Y 년")
        )),
        yaxis=dict(title='온도(°C)'),
        hovermode="x",
    )
    fig.update_traces(hoverlabel=dict(font=dict(size=23)))
    return fig
grp2 = create_graph(df2)    
grp1.show()
grp2.show()