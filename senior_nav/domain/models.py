from dataclasses import dataclass, field, asdict
from typing import Optional, Dict, List
from datetime import datetime

@dataclass
class AppState:
    created_at: datetime = field(default_factory=datetime.utcnow)
    # (extend gradually; keep original UI untouched)
    def to_dict(self) -> Dict:
        return asdict(self)
