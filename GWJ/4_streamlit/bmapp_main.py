#첨단 구간 전체 관측경로에 대한 노면온도 지도 생성 기능

import folium
import pandas as pd
import branca.colormap as cm
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
url1 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/b1stall.csv"
)
url2 = (
    "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/b2ndall.csv"
)

df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)


# 평균 위도와 경도 계산
avg_lat1 = df1["위도"].mean()
avg_lat2 = df2["위도"].mean()
avg_lon1 = df1["경도"].mean()
avg_lon2 = df2["경도"].mean()


# Plotly Graph Objects를 사용한 시각화
def create_graph(df1):
    fig = go.Figure(go.Scattermapbox(
        lat=df1["위도"],
        lon=df1["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df1["노면온도"],
            colorscale="Rainbow",
            cmin=df1["노면온도"].min(),
            cmax=df1["노면온도"].max(),
            showscale=True,
        ),
        text=df1["노면온도"],
    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=avg_lat1, lon=avg_lon1),
            zoom=9,
        ),
        showlegend=False,
    )
    return fig
mapm1 = create_graph(df1)

def create_graph(df2):
    fig = go.Figure(go.Scattermapbox(
        lat=df2["위도"],
        lon=df2["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df2["노면온도"],
            colorscale="Rainbow",
            cmin=df2["노면온도"].min(),
            cmax=df2["노면온도"].max(),
            showscale=True,
        ),
        text=df2["노면온도"],
    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=avg_lat2, lon=avg_lon2),
            zoom=9,
        ),
        showlegend=False,
    )
    return fig
mapm2 = create_graph(df2)
