from __future__ import annotations
from senior_nav.domain.models import AppState, GCPResult

def score_gcp(state: AppState) -> AppState:
    result = state.gcp or GCPResult()
    # Simple placeholder logic; replace with real scoring
    scores = {"in_home": 0.5, "assisted": 0.5}
    result.scores = scores
    if getattr(result.flags, "isolation_level", None) == "high":
        result.care_type = "Assisted Living"
        result.decision_trace = ["baseline tie", "isolation high → Assisted Living"]
    else:
        result.care_type = "In-Home Care"
        result.decision_trace = ["baseline tie", "no high isolation → In-Home Care"]
    state.gcp = result
    return state
