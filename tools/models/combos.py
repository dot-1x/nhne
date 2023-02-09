from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, List, NamedTuple, Tuple, TypedDict

if TYPE_CHECKING:
    from .ninjas import DeployNinja

__all__ = ("DeployCombo", "ComboDict", "ComboAttr")


class ComboAttr(Enum):
    NAME = "Name"
    HP = "HP"
    ATK = "ATK"
    DEF = "DEF"
    AGI = "AGI"
    TRIGGER = "Trigger"
    NINJAS = "Ninjas"

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value


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


class ComboDict(TypedDict):
    id: int
    attack: int
    defend: int
    hp: int
    agility: int
    trigger: bool
    ninjas: List[str]
