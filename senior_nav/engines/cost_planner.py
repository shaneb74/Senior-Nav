from __future__ import annotations
from senior_nav.domain.models import AppState

def compute_costs(state: AppState) -> AppState:
    state.costs.monthly_costs = {"care_services": 0.0, "housing": 0.0, "benefits_offset": 0.0}
    state.costs.runway_months = None
    return state
