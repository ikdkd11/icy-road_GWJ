import pandas as pd
import folium
from folium.plugins import DualMap
from branca.colormap import LinearColormap

# CSV 파일 읽기
url1 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/%EA%B4%91%EC%96%911%EC%B0%A8.csv"
df1 = pd.read_csv(url1)

# 2. 필요한 데이터 추출
lines = df1[["위도", "경도"]].values.tolist()
rtems = df1["노면온도"].tolist()
temps = df1["기온"].tolist()

# Colormap 생성
colormap = LinearColormap(
    colors=[
        "white", "black", "darkslateblue", "fuchsia", "orchid", "violet", "navy",
        "blue", "dodgerblue", "darkturquoise", "lightskyblue", "darkgreen",
        "limegreen", "lime", "lemonchiffon", "yellow", "lightsalmon", "coral",
        "tomato", "crimson", "red",
    ],
    index=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    vmin=-10, vmax=10
).to_step(n=21)

# 중심 지점 설정
center = [34.912012, 126.604137]

# DualMap 객체 생성
m = DualMap(location=center, zoom_start=10)

# 데이터를 기반으로 원 추가
for i, (point, rtemp, temp) in enumerate(zip(lines, rtems, temps)):
    diff = round(rtemp - temp, 1)
    try:
        # 노면온도에 대한 원
        folium.Circle(
            location=point,
            radius=10,
            fill=True,
            color=colormap(rtemp),
            fill_opacity=0.5,
            popup=folium.Popup(f"경도: {point[0]}<br>위도: {point[1]}<br>온도: {rtemp}", min_width=200, max_width=200)
        ).add_to(m.m1)

        # 온도 편차에 대한 원
        folium.Circle(
            location=point,
            radius=10,
            fill=True,
            color=colormap(diff),
            fill_opacity=0.5,
            popup=folium.Popup(f"경도: {point[0]}<br>위도: {point[1]}<br>온도 편차: {diff}", min_width=200, max_width=200)
        ).add_to(m.m2)
    except:
        continue

# colormap을 m.m2에 추가
m.m2.add_child(colormap)

# 결과를 map1 객체에 저장
map1 = m
# 이후 map1 객체를 다른 py 파일에서 사용할 수 있도록 저장하는 방법을 구현하세요.
# 예를 들어, pickle을 사용해 직렬화하거나 모듈로서 정의할 수 있습니다.
