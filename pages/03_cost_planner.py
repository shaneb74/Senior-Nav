import streamlit as st
from senior_nav.ui.components.chrome import inject_css, page_header
from senior_nav.domain.models import AppState
from senior_nav.engines.cost_planner import compute_costs

inject_css()
page_header("Cost Planner", "Estimate monthly out-of-pocket and runway.")

state: AppState = st.session_state["app_state"]
if st.button("Recalculate"):
    st.session_state["app_state"] = compute_costs(state)

st.json(state.costs.monthly_costs)
