import streamlit as st
from senior_nav.ui.components.chrome import inject_css
from senior_nav.domain.models import AppState

st.set_page_config(page_title="Senior Care Navigator", page_icon="🧭", layout="wide")
inject_css()

if "app_state" not in st.session_state:
    st.session_state["app_state"] = AppState()

st.markdown("<div class='cca-container cca-card'><h2>Decision Tools Hub</h2><p>Choose a tool to get started.</p></div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/01_audiencing.py", label="Audiencing", icon="🎯")
with col2:
    st.page_link("pages/02_gcp.py", label="Guided Care Plan", icon="🩺")
with col3:
    st.page_link("pages/03_cost_planner.py", label="Cost Planner", icon="💵")
with col4:
    st.page_link("pages/05_exports.py", label="Exports", icon="📤")
