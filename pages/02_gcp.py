import streamlit as st
from senior_nav.ui.components.chrome import inject_css, page_header
from senior_nav.domain.models import AppState
from senior_nav.engines.gcp import score_gcp

inject_css()
page_header("Guided Care Plan", "Answer a few questions; we’ll suggest a next step.")

state: AppState = st.session_state["app_state"]

with st.form("gcp_form"):
    isolation = st.select_slider("How isolated is the person day-to-day?", options=["low","medium","high"])
    st.session_state["app_state"].gcp.flags.isolation_level = isolation
    submitted = st.form_submit_button("Get Recommendation")
    if submitted:
        st.session_state["app_state"] = score_gcp(state)

if state.gcp.care_type:
    st.markdown(f"<div class='cca-card'><h3>Suggested care type: {state.gcp.care_type}</h3></div>", unsafe_allow_html=True)
    with st.expander("Why this?"):
        st.write(state.gcp.decision_trace)
