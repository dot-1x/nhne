from enum import IntFlag, auto
from typing import NamedTuple, TypedDict

from ..data import COMBOS


class NinjaAttr(IntFlag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()


class DeployNinja(NamedTuple):
    id: int
    name: str
    atas: NinjaAttr
    kanan: NinjaAttr
    bawah: NinjaAttr
    kiri: NinjaAttr

    def get_available_combos(self):
        return [k for k, v in COMBOS.items() if self.name in v["ninjas"]]

    def __str__(self) -> str:
        return self.name


class Ninja(TypedDict):
    id: int
    attribute: list[str]
