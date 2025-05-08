import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim

address = "폴리텍대학 광주캠퍼스"

# 주소 → 위도/경도
geolocator = Nominatim(user_agent="myGeocoder")
location = geolocator.geocode(address)

latitude = location.latitude
longitude = location.longitude

# 지도 생성
mymap = folium.Map(location=[latitude, longitude], zoom_start=16)

# 마커 추가
folium.Marker(
    [latitude, longitude],
    popup=address,
    icon=folium.Icon(icon='info-sign')  # 기본 아이콘 명시
).add_to(mymap)

# Streamlit에 지도 표시
st_folium(mymap, width=700, height=500)
