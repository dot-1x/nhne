from ..data import COMBOS
from ..models.combos import DeployCombo
from .ninja import get_ninjas

__all__ = [
    "get_combo",
    "get_combos"
]

def get_combo(combo: str):
    comb = COMBOS.get(combo.title())
    if not comb:
        return None
    return DeployCombo(
        id=comb["id"],
        name=combo,
        attack=comb["attack"],
        defend=comb["defend"],
        agility=comb["agility"],
        hp=comb["hp"],
        trigger=comb["trigger"],
        ninjas=get_ninjas(*list(comb["ninjas"])),
    )


def get_combos(*combos: str):
    return tuple(get_combo(c) for c in combos if c in COMBOS)
