import streamlit as st
import folium
from folium.plugins import Draw
from streamlit_folium import st_folium
from data_api import save_location, load_locations


st.set_page_config(page_title="WFH Map Demo", page_icon=":world_map:️", layout="wide")
st.title("WFH Map")
m = folium.Map(location=[40.092518, -94.98745], zoom_start=4.3)
data = load_locations()

for d in data:
    folium.Marker(
        d['location'], popup=d['notes'], tooltip=d['name']
    ).add_to(m)

Draw(export=False, draw_options={
    'polyline': False, 'polygon': False, 'rectangle': False, 'circle': False, 'circlemarker': False, "marker": True
}).add_to(m)

output = st_folium(m, width=1024, height=500)
if output["all_drawings"]:
    st.session_state['marker'] = output['all_drawings'][0]['geometry']['coordinates'][::-1]

with st.sidebar.form("Create Pin Form"):
    st.write("location")
    if 'marker' in st.session_state:
        if len(output['all_drawings']) >= 2:
            st.error(f"You have created {len(output['all_drawings'])} markers. Please use 🗑️ icon on the map to remove excessive markers. ")
        if len(output['all_drawings']) == 1:
            st.success(f"You have created 1 marker at {st.session_state['marker']}")
    else:
        st.info("Click map pin to add your location on the map")
    name = st.text_input(label="Name")
    email = st.text_input(label="Email")
    notes = st.text_area(label="Notes")
    submitted = st.form_submit_button("Create Your Pin on the Map")
    if submitted:
        if 'marker' not in st.session_state:
             st.error("Please click map pin and create a marker on the map. ")
        else:
             save_location(name, email, notes, st.session_state['marker'])
             del st.session_state['marker']
             st.experimental_rerun()