from typing import Generator
from ..data import COMBOS
from ..models.combos import DeployCombo
from .ninja import get_ninjas

__all__ = ["get_combo", "get_combos"]


def get_combo(combo: str):
    comb = COMBOS.get(combo)
    if not comb:
        return None
    return DeployCombo(
        id_=comb["id"],
        name=combo,
        attack=comb["attack"],
        defend=comb["defend"],
        agility=comb["agility"],
        hp=comb["hp"],
        trigger=comb["trigger"],
        ninjas=tuple(get_ninjas(*tuple(comb["ninjas"]))),
    )


def get_combos(*combos: str):
    for c in combos:
        combo = get_combo(c)
        if not combo:
            continue
        yield combo
