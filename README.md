# Senior Care Navigator (Fresh Start)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Structure
- `app.py` — main entry (Hub)
- `pages/` — multipage screens (Audiencing, GCP, Cost Planner, Exports)
- `senior_nav/` — engines, domain models, centralized CSS + UI components
- `.streamlit/config.toml` — theme settings
