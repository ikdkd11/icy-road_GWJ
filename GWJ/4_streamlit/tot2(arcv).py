import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from PIL import Image
import streamlit as st

# 파일명과 해당 파일을 저장할 DataFrame 변수명 매핑
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EA%B4%91%EC%96%911%EC%B0%A8.csv"
)
url2 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EA%B4%91%EC%96%912%EC%B0%A8.csv"
    )
url3 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EA%B4%91%EC%96%913%EC%B0%A8.csv"
    )
url4 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EA%B4%91%EC%96%914%EC%B0%A8.csv"
    )

df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)
df3 = pd.read_csv(url3)
df4 = pd.read_csv(url4)
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
            line=dict(color=f'rgb{color}', width=1.5),  # 라인 색상 및 두께 설정
            connectgaps=True
        ))

    # 교량 표시를 위한 주석 추가들
    annotations = [
        ("2024-01-10 17:48:39", "초당 교차로<br>첫번째 위험구간", 5, 30),
        ("2024-01-10 17:54:22", "예당 교차로", 15, 55),
        ("2024-01-10 18:12:02", "벌교IC 교차로", 15, 55),
        ("2024-01-10 18:22:27", "구룡교", -15, 75),
        ("2024-01-10 18:06:10", "귀산교차로", -10, 85),
        ("2024-01-10 18:09:10", "옥전교<br> 둘째 위험구간", -5, 75),
        ("2024-01-10 18:16:08", "장양육교<br> 셋째 위험구간", -5, 75),
        ("2024-01-10 18:28:37", "쌍림1교 시작", -5, 75),
        ("2024-01-10 18:29:18", "쌍림2교 종료", 37, 65),
        ("2024-01-10 18:46:30", "연향육교", -17, 50),
        ("2024-01-10 18:50:31", "조례사거리(조례지하차도)", -17, 100),
        ("2024-01-10 19:04:32", "세풍교차로~초남1교<br> 넷째 위험구간", 0, 70),
        ("2024-01-10 19:15:27", "중군터널~마룡교<br> 다섯째 위험구간", 0, 90)
    ]

    for x, text, ax, ay in annotations:
        fig.add_annotation(
            x=x,
            y=df1.loc[df1['시간'] == x, '노면온도'].values[0],
            text=text,
            showarrow=True,
            ax=ax,
            ay=ay,
            arrowwidth=2,
            arrowsize=1.5,  
            bgcolor='rgb(0, 0, 0)',
            font=dict(color='white', size=13)
        )

    fig.update_layout(
        title=dict(text='1월10일 보성-광양 노면관측 그래프<br>일몰시각 <17:39>, 관측시간<17:47 ~ 19:16>', x=0, font=dict(size=23, color="black", family="Arial Black"), xanchor='left',),
        xaxis=dict(
            title='날짜와 시간',
            range=[df1['시간'].min(), df1['시간'].max()],
            tickformatstops=[
                dict(dtickrange=(None, 1000), value="%H:%M:%S.%L 밀리초"),
                dict(dtickrange=(1000, 60000), value="%H:%M:%S 초"),
                dict(dtickrange=(60000, 3600000), value="%H:%M 분"),
                dict(dtickrange=(3600000, 86400000), value="%H:%M 시"),
                dict(dtickrange=(86400000, 604800000), value="%e. %b 일"),
                dict(dtickrange=(604800000, "M1"), value="%e. %b 주"),
                dict(dtickrange=("M1", "M12"), value="%b '%y 월"),
                dict(dtickrange=("M12", None), value="%Y 년")
            ]
        ),
        yaxis=dict(title='온도(°C)'),
        hovermode="x"
    )
    fig.update_traces(hoverlabel=dict(font=dict(size=23)))

    return fig

# 함수 사용 예시
grp1 = create_graph(df1)

# plotly를 사용하여 그래프 그리기
def create_graph(df2):
    fig = go.Figure()
    for location, color in zip(['기온', '노면온도'], [(255, 99, 71), (30, 144, 255)]):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df2['시간'],
            y=df2[location],
            name=location,
            line=dict(color=f'rgb{color}', width=1.5),  # 라인 색상 및 두께 설정
            connectgaps=True
    ))

    # 교량 표시를 위한 주석 추가들
    annotations = [
            ("2024-01-11 06:51:00", '마룡교~중군터널<br> 다섯째 위험구간', 35, 30),
            ("2024-01-11 07:01:58", '초남1교~세풍교차로<br> 넷째 위험구간', 0, 40),
            ("2024-01-11 07:21:34", '연향육교', 0, 20),
            ("2024-01-11 07:29:58", '연동교', -20, 30),
            ("2024-01-11 07:35:25", '쌍림2교>사거리>쌍림1교', -20, 30),
            ("2024-01-11 07:42:13", '구룡교', -20, 30),
            ("2024-01-11 07:46:06", '장양육교<br>셋째 위험구간', -10, 30),
            ("2024-01-11 07:55:02", '옥전교<br>둘째 위험구간', -10, 40),
            ("2024-01-11 08:10:43", '초당 교차로<br>첫째 위험구간', -10, 40)
    ]

    for x, text, ax, ay in annotations:
        # 데이터프레임에서 해당 시간의 노면온도 데이터가 존재하는지 확인
            fig.add_annotation(
                x=x,
                y=df2.loc[df2['시간'] == x, '노면온도'].values[0],
                text=text,
                showarrow=True,
                ax=ax,
                ay=ay,
                arrowwidth=2,
                arrowsize=1.5,
                bgcolor='rgb(0, 0, 0)',
                font=dict(color='white', size=13)
            )    

    fig.update_layout(
            title=dict(text='1월11일 광양-보성 2차 노면관측 그래프<br>일출시각 <07:39>, 관측시간<06:50 ~ 08:11>', font=dict(size=23, color="black", family="Arial Black"), x=0),
            xaxis=dict(
                title='날짜와 시간',
                range=[df2['시간'].min(), df2['시간'].max()],
                tickformatstops=[
                    dict(dtickrange=(None, 1000), value="%H:%M:%S.%L 밀리초"),
                    dict(dtickrange=(1000, 60000), value="%H:%M:%S 초"),
                    dict(dtickrange=(60000, 3600000), value="%H:%M 분"),
                    dict(dtickrange=(3600000, 86400000), value="%H:%M 시"),
                    dict(dtickrange=(86400000, 604800000), value="%e. %b 일"),
                    dict(dtickrange=(604800000, "M1"), value="%e. %b 주"),
                    dict(dtickrange=("M1", "M12"), value="%b '%y 월"),
                    dict(dtickrange=("M12", None), value="%Y 년")
                ]
            ),    
            yaxis=dict(title='온도(°C)'),
            hovermode="x",
    )
    fig.update_traces(hoverlabel=dict(font=dict(size=23)))    

    return fig    

# 함수 사용하여 그래프 객체 생성 및 저장
grp2 = create_graph(df2)

#3차 관측
def create_graph(df3):
    fig = go.Figure()

    for location, color in zip(['기온', '노면온도'], [(255,69,0), (70,130,180)]):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df3['시간'],
            y=df3[location],
            name=location,
            line=dict(color=f'rgb{color}', width=1.5),
            connectgaps=True
        ))

    annotations = [
        ('2024-01-24 17:50:44', '초당 교차로<br>첫번째 위험구간', 15, 45),
        ('2024-01-24 17:56:57', '덕산제 인근', -15, 60),
        ('2024-01-24 18:04:03', '조성교~귀산교차로', -55, 75),
        ('2024-01-24 18:07:14', '옥전교<br>둘째 위험구간', -15, 55),
        ('2024-01-24 18:10:16', '벌교IC 교차로', 15, 55),
        ('2024-01-24 18:18:52', '장양육교<br>셋째 위험구간', -55, 40),
        ('2024-01-24 18:28:04', '쌍림1교 시작', -15, -55),
        ('2024-01-24 18:29:20', '쌍림2교 종료', 15, -55),
        ('2024-01-24 18:31:46', '순천만IC 교차로', -15, 55),
        ('2024-01-24 18:35:59', '연동교 교차로', -15, 55),
        ('2024-01-24 18:39:50', '순천만 국가정원 구간(시작)', 15, -45),
        ('2024-01-24 18:43:58', '순천만 국가정원 구간(끝)', 15, -45),
        ('2024-01-24 18:47:29', '연향육교', -35, 5),
        ('2024-01-24 18:50:38', '조례사거리(구간 시작)', 15, -45),
        ('2024-01-24 18:59:33', '신대교차로(구간 종료)', -85, 10),
        ('2024-01-24 19:02:25', '세풍교차로~초남1교<br>넷째 위험구간', -75, 30),
        ('2024-01-24 19:09:33', '중군터널~마룡교<br>다섯째 위험구간', 75, 30)
    ]

    for x, text, ax, ay in annotations:
        if not df3.loc[df3['시간'] == x, '노면온도'].empty:
            fig.add_annotation(
                x=x,
                y=df3.loc[df3['시간'] == x, '노면온도'].values[0],
                text=text,
                showarrow=True,
                ax=ax,
                ay=ay,
                arrowwidth=2,
                arrowsize=1.5,
                bgcolor='rgb(0, 0, 0)',
                font=dict(color='white', size=13)
            )

    fig.update_layout(
        title=dict(text='1월24일 보성-광양 3차 노면관측 그래프<br>일몰시각 <17:52>, 관측시간<17:49 ~ 19:16>', font=dict(size=23, color="black", family="Arial Black"), x=0),
        xaxis=dict(
            title='날짜와 시간',
            range=[df3['시간'].min(), df3['시간'].max()],
            tickformatstops=[
                dict(dtickrange=(None, 1000), value="%H:%M:%S.%L 밀리초"),
                dict(dtickrange=(1000, 60000), value="%H:%M:%S 초"),
                dict(dtickrange=(60000, 3600000), value="%H:%M 분"),
                dict(dtickrange=(3600000, 86400000), value="%H:%M 시"),
                dict(dtickrange=(86400000, 604800000), value="%e. %b 일"),
                dict(dtickrange=(604800000, "M1"), value="%e. %b 주"),
                dict(dtickrange=("M1", "M12"), value="%b '%y 월"),
                dict(dtickrange=("M12", None), value="%Y 년")
            ]
        ),
        yaxis=dict(title='온도(°C)'),
        hovermode="x",
    )
    fig.update_traces(hoverlabel=dict(font=dict(size=23)))

    return fig
grp3 = create_graph(df3)

#4차 관측
# df_cleaned가 아니라 df를 사용하는 것으로 가정합니다.
# 주석에서 df_cleaned 대신 df를 사용합니다.
def create_graph(df4):
    fig = go.Figure()
    for location, color in zip(['기온', '노면온도'], [(220, 20, 60), (100,149,237)]):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df4['시간'],
            y=df4[location],
            name=location,
            line=dict(color=f'rgb{color}', width=1.5),
            connectgaps=True
        ))

# 여기서부터 각 교량 및 특정 지점에 대한 주석 추가
    annotations = [
        ('2024-01-25 05:57:31', '마룡교~중군터널<br> 다섯째 위험구간', 35, 30),
        ('2024-01-25 06:09:15', '초남1교~세풍교차로<br> 넷째 위험구간', -20, 70),
        ('2024-01-25 06:13:42', '세승교', -10, 50),
        ('2024-01-25 06:16:03', '신대교차로(구간 시작)', -15, 105),
        ('2024-01-25 06:18:14', '조례사거리(구간 종료)', 15, 110),
        ('2024-01-25 06:25:43', '연향육교', -30, 0),
        ('2024-01-25 06:28:57', '순천만 국가정원 구간(시작)', -20, 30),
        ('2024-01-25 06:32:49', '순천만 국가정원 구간(끝)', 0, -60),
        ('2024-01-25 06:35:21', '연동교', -20, 30),
        ('2024-01-25 06:37:53', '순천만IC 교차로', -20, 30),
        ('2024-01-25 06:40:19', '쌍림2교>쌍림1교', -20, 30),
        ('2024-01-25 06:45:12', '구룡교', -20, 30),
        ('2024-01-25 06:46:56', '동막1~2교', -20, 30),
        ('2024-01-25 06:50:47', '장양육교<br>셋째 위험구간', -10, 30),
        ('2024-01-25 06:52:33', '벌교대교>장좌육교>무안육교>원동교', -10, -60),
        ('2024-01-25 06:59:57', '옥전교<br>둘째 위험구간', -10, 40),
        ('2024-01-25 07:04:53', '조성교', -10, 40),
        ('2024-01-25 07:12:51', '덕산제 인근', -30, 40),
        ('2024-01-25 07:17:15', '초당 교차로<br>첫째 위험구간', -10, 40)
    ]

    for x, text, ax, ay in annotations:
        fig.add_annotation(
            x=x,
            y=df4.loc[df4['시간'] == x, '노면온도'].values[0] if df4.loc[df4['시간'] == x, '노면온도'].values.size > 0 else None,
            text=text,
            showarrow=True,
            ax=ax,
            ay=ay,
            arrowwidth=2,
            arrowsize=1.5,
            bgcolor='rgb(0, 0, 0)',
            font=dict(color='white', size=13)
        )

    fig.update_layout(
        title=dict(text='1월25일 광양-보성 4차 노면관측 그래프<br>일출시각 <07:35>, 관측시간<05:56 ~ 07:17>', font=dict(size=23, color="black", family="Arial Black"), x=0),
        xaxis=dict(
            title='날짜와 시간',
            range=[df4['시간'].min(), df4['시간'].max()],
            tickformatstops=[
                dict(dtickrange=[None, 1000], value="%H:%M:%S.%L 밀리초"),
                dict(dtickrange=[1000, 60000], value="%H:%M:%S 초"),
                dict(dtickrange=[60000, 3600000], value="%H:%M 분"),
                dict(dtickrange=[3600000, 86400000], value="%H:%M 시"),
                dict(dtickrange=[86400000, 604800000], value="%e. %b 일"),
                dict(dtickrange=[604800000, "M1"], value="%e. %b 주"),
                dict(dtickrange=["M1", "M12"], value="%b '%y 월"),
                dict(dtickrange=["M12", None], value="%Y 년")
            ]
        ),
        yaxis=dict(title='온도(°C)'),
        hovermode="x",
    )
    fig.update_traces(hoverlabel=dict(font=dict(size=23)))
    return fig
grp4 = create_graph(df4)
