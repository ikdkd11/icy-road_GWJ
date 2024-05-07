import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 데이터 불러오기
url1 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/1_1.csv"
df11_cleaned = pd.read_csv(url1)

def create_graph(df):
    # '노면온도'와 '기온' 차이 계산
    df['온도차'] = df['노면온도'] - df['기온']
    
    # Plotly 산점도 그래프 생성을 위한 설정
    fig = go.Figure()
    
    # 노면온도 시각화
    fig.add_trace(go.Scattergeo(
        lon = df['경도'],
        lat = df['위도'],
        text = df['노면온도'],
        mode = 'markers',
        marker = dict(
            size = 8,
            color = df['노면온도'],
            colorscale = 'Viridis',
            showscale = True,
            colorbar=dict(title="노면온도")
        )
    ))
    
    # 기온과의 차이 시각화 (새 창에 표시하려면, 새 Figure 객체를 생성하고 비슷한 방식으로 추가하세요)
    fig.add_trace(go.Scattergeo(
        lon = df['경도'],
        lat = df['위도'],
        text = df['온도차'],
        mode = 'markers',
        marker = dict(
            size = 8,
            color = df['온도차'],
            colorscale = 'RdBu',
            showscale = True,
            colorbar=dict(title="기온과의 온도차")
        ),
        subplot = 'mapbox2' # 두 번째 지도에 온도차를 표시하기 위해 subplot 사용
    ))
    
    # 지도 및 그래프 설정
    fig.update_layout(
        geo=dict(
            scope='asia',
            projection_type='mercator',
            landcolor='rgb(243, 243, 243)'
        ),
        title_text = '노면온도 및 기온과의 온도차 시각화'
    )
    
    return fig

# 그래프 생성 및 표시
grp11 = create_graph(df11_cleaned)
grp11.show()
