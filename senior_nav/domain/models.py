from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Literal
from datetime import datetime

CareType = Literal["In-Home Care","Assisted Living","Memory Care","Skilled Nursing","Undecided"]

@dataclass
class Flags:
    fall_risk: Optional[Literal["low","medium","high"]] = None
    isolation_level: Optional[Literal["low","medium","high"]] = None
    cognition_level: Optional[Literal["intact","mild","moderate","advanced"]] = None
    mobility_level: Optional[Literal["independent","assisted","wheelchair","bedbound"]] = None
    home_safety: Optional[Literal["safe","concerns","unsafe"]] = None

@dataclass
class Derived:
    adl_bucket: Optional[Literal["low","medium","high"]] = None
    medication_complexity: Optional[Literal["low","medium","high"]] = None

@dataclass
class GCPResult:
    care_type: Optional[CareType] = None
    scores: Dict[str, float] = field(default_factory=dict)
    flags: Flags = field(default_factory=Flags)
    derived: Derived = field(default_factory=Derived)
    decision_trace: List[str] = field(default_factory=list)
    blurbs: List[str] = field(default_factory=list)

@dataclass
class CostOutputs:
    monthly_costs: Dict[str, float] = field(default_factory=dict)
    runway_months: Optional[float] = None
    activated_drawers: List[str] = field(default_factory=list)

@dataclass
class AppState:
    version: str = "0.1.0"
    person_id: Optional[str] = None
    audience_role: Optional[str] = None
    zipcode: Optional[str] = None
    gcp: GCPResult = field(default_factory=GCPResult)
    costs: CostOutputs = field(default_factory=CostOutputs)
    created_at: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict:
        return asdict(self)
