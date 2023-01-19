from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING, List, NamedTuple, Tuple, TypedDict

if TYPE_CHECKING:
    from .ninjas import DeployNinja


class ComboAttr(Enum):
    HP = auto()
    ATK = auto()
    DEF = auto()
    AGI = auto()


class DeployCombo(NamedTuple):
    id_: int
    name: str
    attack: int
    defend: int
    hp: int
    agility: int
    trigger: bool
    ninjas: Tuple[DeployNinja]

    @property
    def attrs(self):
        return (self.attack, self.defend, self.hp, self.agility)


class Combo(TypedDict):
    id: int
    attack: int
    defend: int
    hp: int
    agility: int
    trigger: bool
    ninjas: List[str]
