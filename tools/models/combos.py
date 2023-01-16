from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING, NamedTuple, TypedDict

if TYPE_CHECKING:
    from .ninjas import DeployNinja


class ComboAttr(Enum):
    HP = auto()
    ATK = auto()
    DEF = auto()
    AGI = auto()


class DeployCombo(NamedTuple):
    id: int
    name: str
    attack: int
    defend: int
    hp: int
    agility: int
    trigger: bool
    ninjas: tuple[DeployNinja]


class Combo(TypedDict):
    id: int
    attack: int
    defend: int
    hp: int
    agility: int
    trigger: bool
    ninjas: list[str]
