import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
from PIL import Image
import streamlit as st

# 파일명과 해당 파일을 저장할 DataFrame 변수명 매핑
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EA%B4%91%EC%96%911%EC%B0%A8.csv"
)

df1 = pd.read_csv(url1)
# plotly를 사용하여 그래프 그리기
print(df1)
def create_graph(df1):
    fig = go.Figure()
    for location, color in zip(['기온', '노면온도'], [(255, 0, 0), (35, 35, 200)]):
        fig.add_trace(go.Scatter(
            mode='lines',
            x=df1['시간'],  
            y=df1[location],
            name=location,
            line=dict(color=f'rgb{color}', width=1.2),  # 라인 색상 및 두께 설정
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
        title=dict(text='1월10일 보성-광양 노면관측 그래프<br>일몰시각 <17:39>, 관측시간<17:47 ~ 19:16>', x=0, font=dict(size=15, color="black", family="Arial Black"), xanchor='left',),
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