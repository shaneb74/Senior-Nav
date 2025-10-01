import streamlit as st
from senior_nav.ui.components.chrome import inject_css, page_header
from senior_nav.domain.models import AppState
import json

inject_css()
page_header("Exports", "Download a JSON snapshot for your advisor.")

state: AppState = st.session_state["app_state"]
st.download_button("Download JSON snapshot", data=json.dumps(state.to_dict(), indent=2),
                   file_name="cca_snapshot.json", mime="application/json")
