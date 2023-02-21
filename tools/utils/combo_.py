from ..data import COMBOS
from ..models.combos import DeployCombo
from .ninja import get_ninjas

__all__ = ["get_combo", "get_combos"]


def get_combo(combo: str):
    comb = COMBOS.get(combo.lower())
    if not comb:
        raise ValueError(f"Invalid Combo {combo}")
    return DeployCombo(
        id_=comb["id"],
        name=combo.title(),
        attack=comb["attack"],
        defend=comb["defend"],
        agility=comb["agility"],
        hp=comb["hp"],
        trigger=comb["trigger"],
        ninjas=get_ninjas(*tuple(comb["ninjas"])),
    )


def get_combos(*combos: str):
    return tuple(get_combo(n) for n in combos)
