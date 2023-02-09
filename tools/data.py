from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import ComboDict, NinjaDict

__all__ = ["COMBOS", "NINJAS", "MAX_NINJAS", "MAIN_NINJAS", "DEPLOY_NINJAS"]

TOOLS_PATH = Path("/".join(__file__.replace("/", "\\").split("\\")[:-1]))

COMBOS: dict[str, ComboDict] = {
    k.lower(): v
    for k, v in json.loads(
        Path(str(TOOLS_PATH) + "/deploy_combos.json").read_text(encoding="utf-8")
    ).items()
}
NINJAS: dict[str, NinjaDict] = {
    k.lower(): v
    for k, v in json.loads(
        Path(str(TOOLS_PATH) + "/ninja_deploys.json").read_text(encoding="utf-8")
    ).items()
}
MAX_NINJAS = 15
MAIN_NINJAS = 3
DEPLOY_NINJAS = 12
DEFAULT_TIMES = 7.0
