import requests
import json
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

# 發送 GET 請求到天氣 API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# 檢查請求是否成功
if result.status_code != 200:
    st.error(f"Failed to fetch data: {result.status_code}")
    st.stop()

# 將 JSON 響應解析為字典對象
result_dict = json.loads(result.text)

# 打印 API 響應的結構
st.write(result_dict)

# 檢查是否包含溫度數據
if 'temperature' not in result_dict or 'data' not in result_dict['temperature']:
    st.error("Temperature data not found in the API response.")
    st.stop()

# 提取主要數據
main_data = []
for reading in result_dict['temperature']['data']:
    if 'place' in reading and 'value' in reading and 'latitude' in reading and 'longitude' in reading:
        main_data.append({
            'place': reading['place'],
            'temperature': reading['value'],
            'latitude': reading['latitude'],
            'longitude': reading['longitude']
        })

# 檢查是否成功提取數據
if not main_data:
    st.error("No valid temperature data found.")
    st.stop()

# 將主要數據轉換為 DataFrame
df = pd.DataFrame(main_data)

# Streamlit 應用
st.title('Hong Kong Weather Data Visualization')

# 顯示所有地點的溫度條形圖
st.subheader('Temperature of All Locations')
st.bar_chart(df.set_index('place'))

# 創建香港地圖
m = folium.Map(location=[22.3193, 114.1694], zoom_start=11)

# 在地圖上添加標記
for _, row in df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"{row['place']}: {row['temperature']} °C",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# 顯示地圖
folium_static(m)

# 用戶選擇地點
selected_place = st.sidebar.selectbox('Select a Location', df['place'])

# 顯示選定地點的溫度
st.subheader(f'Temperature at {selected_place}')
selected_temp = df[df['place'] == selected_place]['temperature'].values[0]
st.write(f'The temperature at {selected_place} is {selected_temp} °C')