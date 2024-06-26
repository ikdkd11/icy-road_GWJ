#첨단-극락교 1차 관측 중 저온구간에 대한 노면온도 지도 생성 기능
import folium
import pandas as pd
import branca.colormap as cm
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
url1 = "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/1stB_1_Sheet1.csv"
url2 = "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/2ndB_1_Sheet1.csv"
url3 = "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/3rdB_1_Sheet1.csv"
url4 = "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/4thB_1_Sheet1.csv"
url5 = "https://raw.githubusercontent.com/ikdkd11/icy-road_GWJ/main/GWJ/0_data/bukgu/5thB_1_Sheet1.csv"

df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)
df3 = pd.read_csv(url3)
df4 = pd.read_csv(url4)
df5 = pd.read_csv(url5)

# 평균 위도와 경도 계산
avg_lat1 = df1["위도"].mean()
avg_lat2 = df2["위도"].mean()
avg_lat3 = df3["위도"].mean()
avg_lat4 = df4["위도"].mean()
avg_lat5 = df5["위도"].mean()
avg_lon1 = df1["경도"].mean()
avg_lon2 = df2["경도"].mean()
avg_lon3 = df3["경도"].mean()
avg_lon4 = df4["경도"].mean()
avg_lon5 = df5["경도"].mean()

# Plotly Graph Objects를 사용한 시각화
def create_graph(df1):
    fig = go.Figure(go.Scattermapbox(
        lat=df1["위도"],
        lon=df1["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df1["노면온도"],
            colorscale="Plasma",
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
            zoom=13,
        ),
        showlegend=False,
    )
    return fig
map11 = create_graph(df1)

def create_graph(df2):
    fig = go.Figure(go.Scattermapbox(
        lat=df2["위도"],
        lon=df2["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df2["노면온도"],
            colorscale="Plasma",
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
            zoom=13,
        ),
        showlegend=False,
    )
    return fig
map12 = create_graph(df2)

def create_graph(df3):
    fig = go.Figure(go.Scattermapbox(
        lat=df3["위도"],
        lon=df3["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df3["노면온도"],
            colorscale="Plasma",
            cmin=df3["노면온도"].min(),
            cmax=df3["노면온도"].max(),
            showscale=True,
        ),
        text=df3["노면온도"],
    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=avg_lat3, lon=avg_lon3),
            zoom=13,
        ),
        showlegend=False,
    )
    return fig
map13 = create_graph(df3)

def create_graph(df4):
    fig = go.Figure(go.Scattermapbox(
        lat=df4["위도"],
        lon=df4["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df4["노면온도"],
            colorscale="Plasma",
            cmin=df4["노면온도"].min(),
            cmax=df4["노면온도"].max(),
            showscale=True,
        ),
        text=df4["노면온도"],
    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=avg_lat4, lon=avg_lon4),
            zoom=13,
        ),
        showlegend=False,
    )
    return fig
map14 = create_graph(df4)

def create_graph(df5):
    fig = go.Figure(go.Scattermapbox(
        lat=df5["위도"],
        lon=df5["경도"],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=df5["노면온도"],
            colorscale="Plasma",
            cmin=df5["노면온도"].min(),
            cmax=df5["노면온도"].max(),
            showscale=True,
        ),
        text=df5["노면온도"],
    ))

    fig.update_layout(
        mapbox=dict(
            style="open-street-map",
            center=dict(lat=avg_lat5, lon=avg_lon5),
            zoom=13,
        ),
        showlegend=False,
    )
    return fig
map15 = create_graph(df5)
