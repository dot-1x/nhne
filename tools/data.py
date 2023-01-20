from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models.combos import Combo
    from .models.ninjas import Ninja

__all__ = ["COMBOS", "NINJAS", "MAX_NINJAS", "MAIN_NINJAS", "DEPLOY_NINJAS"]

TOOLS_PATH = Path("/".join(__file__.replace("/","\\").split("\\")[:-1]))

NINJAS: dict[str, Ninja]
COMBOS: dict[str, Combo]

COMBOS, NINJAS = [{k.lower():v for k,v in json.loads(p.read_text()).items()} for p in TOOLS_PATH.glob("*.json")]
MAX_NINJAS = 15
MAIN_NINJAS = 3
DEPLOY_NINJAS = 12
DEFAULT_TIMES = 7
