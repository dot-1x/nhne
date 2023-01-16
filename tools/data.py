from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models.combos import Combo
    from .models.ninjas import Ninja

__all__ = [
    "COMBOS",
    "NINJAS"
]

TOOLS_PATH = Path("/".join(__file__.split("\\")[:-1]))

NINJAS: dict[str, Ninja]
COMBOS: dict[str, Combo]

COMBOS, NINJAS = [json.loads(p.read_text()) for p in TOOLS_PATH.glob("*.json")]
