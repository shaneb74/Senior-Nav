# Senior Care Navigator — Design-Locked Refactor
This package preserves the original UI and CSS exactly (app.py + static/style.css + guided_care_plan/).
We only add a `senior_nav/` namespace for future engines/domain without touching the current flow.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
