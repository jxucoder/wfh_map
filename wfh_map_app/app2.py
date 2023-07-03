import streamlit as st
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium

# This will keep track of whether a marker has been drawn
marker_drawn = st.empty()

m = folium.Map()

if marker_drawn.text(''):
    draw = Draw(draw_options={'marker': True})
    m.add_child(draw)

st_folium(m)

if st.button('Marker drawn'):
    marker_drawn.text('Marker has been drawn. No more drawing allowed.')
