import pandas as pd
import plotly.express as px

# CSV 파일을 읽어들입니다.
url1 = 'https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot11.csv'
url2 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot2.csv"
url3 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot3.csv"
url4 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot4.csv"
url5 = "https://raw.githubusercontent.com/ikdkd11/dashboard/main/python-for-realestate-data-main/0_data/plot5.csv"

data1 = pd.read_csv(url1)
data2 = pd.read_csv(url2)
data3 = pd.read_csv(url3)
data4 = pd.read_csv(url4)
data5 = pd.read_csv(url5)


# '차수'열에서 숫자만 추출합니다.
data1['차수'] = data1['차수'].str.extract('(\d+)').astype(int)
data2['차수'] = data2['차수'].str.extract('(\d+)').astype(int)
data3['차수'] = data3['차수'].str.extract('(\d+)').astype(int)
data4['차수'] = data4['차수'].str.extract('(\d+)').astype(int)
data5['차수'] = data5['차수'].str.extract('(\d+)').astype(int)

# '구분'별과 '차수'별로 그룹화하여 '온도'의 평균을 계산합니다.
average_temperatures1 = data1.groupby(['구분', '차수'])['온도'].mean().unstack()
average_temperatures2 = data2.groupby(['구분', '차수'])['온도'].mean().unstack()
average_temperatures3 = data3.groupby(['구분', '차수'])['온도'].mean().unstack()
average_temperatures4 = data4.groupby(['구분', '차수'])['온도'].mean().unstack()
average_temperatures5 = data5.groupby(['구분', '차수'])['온도'].mean().unstack()

# 구분 순서를 지정하고, 소수 첫째 자리까지 나오게 조정합니다.
custom_order = ['구간 전체', '진입 전', '급락구간']
custom_order3 = ['구간 전체', '벌교대교', '장양육교']
average_temperatures1 = average_temperatures1.reindex(custom_order).round(1)
average_temperatures2 = average_temperatures2.reindex(custom_order).round(1)
average_temperatures3 = average_temperatures3.reindex(custom_order3).round(1)
average_temperatures4 = average_temperatures4.reindex(custom_order).round(1)
average_temperatures5 = average_temperatures5.reindex(custom_order).round(1)


average_temperatures1.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']
average_temperatures2.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']
average_temperatures3.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']   
average_temperatures4.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']
average_temperatures5.columns = ['1차 관측', '2차 관측', '3차 관측', '4차 관측']


# Using plotly to generate the line graph
def create_graph(average_temperatures1):
    fig = px.line(average_temperatures1.reset_index(), x='구분', y=average_temperatures1.columns,
                title='위험구간(초당교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 그래프')

    # Updating layout for clarity
    fig.update_layout(
        xaxis=dict(
            title='구간 전체/저온구간 진입전/저온구간',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting x-axis title font size
        ),
        yaxis=dict(
            title='노면온도(°C)',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting y-axis title font size
        ),
        legend_title='관측차수',
        legend_title_font=dict(size=12),  # Adjusting legend title font size
        margin=dict(l=50, r=50, t=40, b=30)
    )

    # Adding markers to the line
    # Adjusting the marker size in the plotly graph
    # Adding data labels to the markers on the plotly graph with Celsius symbol
    # Adjusting the text size on the markers in the plotly graph
    for trace in fig.data:
        trace.mode = 'lines+markers+text'
        trace.text = [f"{y}°C" for y in trace.y]
        trace.textposition = "top left"
        trace.marker = dict(size=15)  # Keeping the marker size adjustment
        trace.textfont = dict(size=15, color='black')  # Adjusting text size
    return fig
    # Attempting to display the updated plot again
grbp1 = create_graph(average_temperatures1)

def create_graph(average_temperatures2):
    fig = px.line(average_temperatures2.reset_index(), x='구분', y=average_temperatures2.columns,
                title='위험구간(옥전교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 그래프')

    # Updating layout for clarity
    fig.update_layout(
        xaxis=dict(
            title='구간 전체/저온구간 진입전/저온구간',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting x-axis title font size
        ),
        yaxis=dict(
            title='노면온도(°C)',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting y-axis title font size
        ),
        legend_title='관측차수',
        legend_title_font=dict(size=12),  # Adjusting legend title font size
        margin=dict(l=50, r=50, t=40, b=30)
    )

    # Adding markers to the line
    # Adjusting the marker size in the plotly graph
    # Adding data labels to the markers on the plotly graph with Celsius symbol
    # Adjusting the text size on the markers in the plotly graph
    for trace in fig.data:
        trace.mode = 'lines+markers+text'
        trace.text = [f"{y}°C" for y in trace.y]
        trace.textposition = "top left"
        trace.marker = dict(size=15)  # Keeping the marker size adjustment
        trace.textfont = dict(size=15, color='black')  # Adjusting text size
    return fig
    # Attempting to display the updated plot again
grbp2 = create_graph(average_temperatures2)

def create_graph(average_temperatures3):
    fig = px.line(average_temperatures3.reset_index(), x='구분', y=average_temperatures3.columns,
                title='위험구간(옥전교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 그래프')

    # Updating layout for clarity
    fig.update_layout(
        xaxis=dict(
            title='구간 전체/벌교대교/장양육교',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting x-axis title font size
        ),
        yaxis=dict(
            title='노면온도(°C)',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting y-axis title font size
        ),
        legend_title='관측차수',
        legend_title_font=dict(size=12),  # Adjusting legend title font size
        margin=dict(l=50, r=50, t=40, b=30)
    )

    # Adding markers to the line
    # Adjusting the marker size in the plotly graph
    # Adding data labels to the markers on the plotly graph with Celsius symbol
    # Adjusting the text size on the markers in the plotly graph
    for trace in fig.data:
        trace.mode = 'lines+markers+text'
        trace.text = [f"{y}°C" for y in trace.y]
        trace.textposition = "top left"
        trace.marker = dict(size=15)  # Keeping the marker size adjustment
        trace.textfont = dict(size=15, color='black')  # Adjusting text size
    return fig
    # Attempting to display the updated plot again
grbp3 = create_graph(average_temperatures3)

def create_graph(average_temperatures4):
    fig = px.line(average_temperatures4.reset_index(), x='구분', y=average_temperatures4.columns,
                title='위험구간(옥전교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 그래프')

    # Updating layout for clarity
    fig.update_layout(
        xaxis=dict(
            title='구간 전체/저온구간 진입전/저온구간',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting x-axis title font size
        ),
        yaxis=dict(
            title='노면온도(°C)',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting y-axis title font size
        ),
        legend_title='관측차수',
        legend_title_font=dict(size=12),  # Adjusting legend title font size
        margin=dict(l=50, r=50, t=40, b=30)
    )

    # Adding markers to the line
    # Adjusting the marker size in the plotly graph
    # Adding data labels to the markers on the plotly graph with Celsius symbol
    # Adjusting the text size on the markers in the plotly graph
    for trace in fig.data:
        trace.mode = 'lines+markers+text'
        trace.text = [f"{y}°C" for y in trace.y]
        trace.textposition = "top left"
        trace.marker = dict(size=15)  # Keeping the marker size adjustment
        trace.textfont = dict(size=15, color='black')  # Adjusting text size
    return fig
    # Attempting to display the updated plot again
grbp4 = create_graph(average_temperatures4)

def create_graph(average_temperatures5):
    fig = px.line(average_temperatures5.reset_index(), x='구분', y=average_temperatures5.columns,
                title='위험구간(옥전교) 중 최저 노면온도 기록구간 진입 전/후 평균 노면온도 그래프')

    # Updating layout for clarity
    fig.update_layout(
        xaxis=dict(
            title='구간 전체/저온구간 진입전/저온구간',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting x-axis title font size
        ),
        yaxis=dict(
            title='노면온도(°C)',
            title_font=dict(size=20),
            tickfont=dict(size=20)  # Adjusting y-axis title font size
        ),
        legend_title='관측차수',
        legend_title_font=dict(size=12),  # Adjusting legend title font size
        margin=dict(l=50, r=50, t=40, b=30)
    )

    # Adding markers to the line
    # Adjusting the marker size in the plotly graph
    # Adding data labels to the markers on the plotly graph with Celsius symbol
    # Adjusting the text size on the markers in the plotly graph
    for trace in fig.data:
        trace.mode = 'lines+markers+text'
        trace.text = [f"{y}°C" for y in trace.y]
        trace.textposition = "top left"
        trace.marker = dict(size=15)  # Keeping the marker size adjustment
        trace.textfont = dict(size=15, color='black')  # Adjusting text size
    return fig
    # Attempting to display the updated plot again
grbp5 = create_graph(average_temperatures5)