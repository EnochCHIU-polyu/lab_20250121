import random
from faker import Faker
import pandas as pd
import streamlit as st

fake = Faker()

# 定義電影屬性
attributes = ['title', 'year', 'genre', 'director', 'rating', 'votes', 'runtime', 'budget']

# 定義一些範例資料
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']
directors = [fake.name() for _ in range(10)]

# 生成隨機電影數據
movies = []
for _ in range(5):
    movie = {
        'title': fake.sentence(nb_words=3),
        'year': random.randint(1980, 2023),
        'genre': random.choice(genres),
        'director': random.choice(directors),
        'rating': round(random.uniform(1, 10), 1),
        'votes': random.randint(1000, 1000000),
        'runtime': random.randint(80, 180),
        'budget': random.randint(1, 300) * 1000000  # 以美元計算的預算
    }
    movies.append(movie)

# 將數據轉換為 DataFrame
df = pd.DataFrame(movies)

# Streamlit 應用
st.title('IMDB Movie Dataset Visualization')

# 顯示數據表
st.subheader('Movie Dataset')
st.dataframe(df)

# 選擇圖表類型
chart_type = st.sidebar.selectbox(
    'Select Chart Type',
    ['Scatter Chart', 'Bar Chart', 'Line Chart', 'Area Chart']
)

# 根據選擇的圖表類型顯示圖表
if chart_type == 'Scatter Chart':
    st.subheader('Scatter Chart: Movie Duration vs IMDb Rating')
    st.caption('This scatter chart shows the relationship between movie duration and IMDb rating. It helps to identify any correlation between the length of a movie and its rating.')
    st.scatter_chart(df[['runtime', 'rating']])

elif chart_type == 'Bar Chart':
    category = st.sidebar.selectbox('Select Category', ['genre', 'director'])
    value = st.sidebar.selectbox('Select Value', ['budget', 'votes'])
    st.subheader(f'Bar Chart: {category.capitalize()} vs {value.capitalize()}')
    st.caption(f'This bar chart compares the {value} across different {category}s. It helps to visualize the distribution and differences in {value} among various {category}s.')
    bar_data = df.groupby(category)[value].sum().reset_index()
    st.bar_chart(bar_data.set_index(category))

elif chart_type == 'Line Chart':
    value = st.sidebar.selectbox('Select Value', ['rating', 'budget'])
    st.subheader(f'Line Chart: Release Year vs {value.capitalize()}')
    st.caption(f'This line chart shows the trend of {value} over the years. It helps to observe how {value} has changed over time.')
    st.line_chart(df[['year', value]].set_index('year'))

elif chart_type == 'Area Chart':
    st.subheader('Area Chart: Release Year vs Box Office Gross')
    st.caption('This area chart shows the box office gross over the years. It helps to visualize the cumulative box office gross and its trend over time.')
    st.area_chart(df[['year', 'budget']].set_index('year'))