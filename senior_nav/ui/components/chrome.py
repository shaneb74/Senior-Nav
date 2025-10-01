import streamlit as st
from pathlib import Path

def inject_css():
    css_path = Path(__file__).resolve().parents[2] / "static" / "style.css"
    try:
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
    except Exception:
        pass

def page_header(title: str, subtitle: str | None = None):
    st.markdown(
        f"<div class='cca-container'><h1>{title}</h1>{f'<p class=\'text-600\'>{subtitle}</p>' if subtitle else ''}</div>",
        unsafe_allow_html=True
    )
