import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

url1 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot11.csv"
)
url2 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot2.csv"
)
url3 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot3.csv"
)
url4 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot4.csv"
)
url5 = (
    "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot5.csv"
)
# Load the CSV file to examine its content
df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)
df3 = pd.read_csv(url3)
df4 = pd.read_csv(url4)
df5 = pd.read_csv(url5)

# 1st 위험구간(초당교차로) 박스플롯
def create_graph(df1):
    fig = px.box(df1, x="차수", y="온도", color="구분")
    # 예시: fig1에 대한 스타일 조정
    fig.update_layout(
        title_text='위험구간1: [초당교차로] - 관측 회차 별 온도 분포',
        title_font=dict(size=20, color='black', family="Arial Bold, sans-serif"),
        legend_title_font=dict(size=16, color='black', family="Arial Bold, sans-serif"),
        legend_font=dict(size=14, color='black', family="Arial, sans-serif")
    )
    fig.update_xaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    fig.update_yaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    return fig
box1 = create_graph(df1)
# 비슷한 방식으로 fig2부터 fig까지의 그래프에 대해서도 적용


# fig1.show()를 호출하여 변경사항 적용 후 그래프를 표시
# 이와 유사한 방식으로 fig2부터 fig까지의 그래프에 대해서도 적용할 수 있습니다.

# Save the figure as an HTML file to be shared

def create_graph(df2):
# 2nd 위험구간(옥전교) 박스플롯
    fig = px.box(df2, x="차수", y="온도", color="구분")
    # fig2: 옥전교 - 관측 회차 별 위험구간 온도 분포
    fig.update_layout(
        title_text='위험구간2: [옥전교] - 관측 회차 별 위험구간 온도 분포',
        title_font=dict(size=20, color='black', family="Arial Bold, sans-serif"),
        legend_title_font=dict(size=16, color='black', family="Arial Bold, sans-serif"),
        legend_font=dict(size=14, color='black', family="Arial, sans-serif")
    )
    fig.update_xaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    fig.update_yaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    return fig
box2 = create_graph(df2)
# Save the figure as an HTML file to be shared

#3rd 위험구간(벌교대교) 박스플롯
def create_graph(df3):
    fig = px.box(df3, x="차수", y="온도", color="구분")
# fig: 벌교대교<->장양육교 - 관측 회차 별 위험구간 온도 분포
    fig.update_layout(
        title_text='위험구간3: [벌교대교<->장양육교] - 관측 회차 별 위험구간 온도 분포',
        title_font=dict(size=20, color='black', family="Arial Bold, sans-serif"),
        legend_title_font=dict(size=16, color='black', family="Arial Bold, sans-serif"),
        legend_font=dict(size=14, color='black', family="Arial, sans-serif")
    )
    fig.update_xaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    fig.update_yaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    return fig
box3 = create_graph(df3)
# Save the figure as an HTML file to be shared

def create_graph(df4):
#4th 위험구간(장양육교) 박스플롯
    fig = px.box(df4, x="차수", y="온도", color="구분")
    # fig: 세풍대교<->초남1교 - 관측 회차 별 위험구간 온도 분포
    fig.update_layout(
        title_text='위험구간4: [세풍대교<->초남1교] - 관측 회차 별 위험구간 온도 분포',
        title_font=dict(size=20, color='black', family="Arial Bold, sans-serif"),
        legend_title_font=dict(size=16, color='black', family="Arial Bold, sans-serif"),
        legend_font=dict(size=14, color='black', family="Arial, sans-serif")
    )
    fig.update_xaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    fig.update_yaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    return fig
# Save the figure as an HTML file to be shared
box4 = create_graph(df4)

def create_graph(df5):
    #5th 위험구간(장양육교) 박스플롯
    fig = px.box(df5, x="차수", y="온도", color="구분")
    # fig: 중군터널<->수어천교 - 관측 회차 별 위험구간 온도 분포
    fig.update_layout(
        title_text='위험구간5: [중군터널<->수어천교 - 관측 회차 별 위험구간 온도 분포',
        title_font=dict(size=20, color='black', family="Arial Bold, sans-serif"),
        legend_title_font=dict(size=16, color='black', family="Arial Bold, sans-serif"),
        legend_font=dict(size=14, family="Arial, sans-serif")
    )
    fig.update_xaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    fig.update_yaxes(title_font=dict(size=18, color='black', family="Arial Bold, sans-serif"))
    return fig
# Save the figure as an HTML file to be shared
box5 = create_graph(df5)
