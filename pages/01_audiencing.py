import streamlit as st
from senior_nav.ui.components.chrome import inject_css, page_header
from senior_nav.domain.models import AppState

inject_css()
page_header("Who are you here for?", "We’ll tailor the experience.")

state: AppState = st.session_state["app_state"]
col1, col2 = st.columns(2)
with col1:
    state.audience_role = st.selectbox("Your role", ["Family Member","Resident","Advisor","Other"], index=0)
with col2:
    state.zipcode = st.text_input("ZIP code", value=state.zipcode or "")

st.success("Saved. Use the sidebar or the links to continue.")
