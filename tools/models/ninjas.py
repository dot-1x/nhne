from enum import IntFlag, auto
from typing import List, NamedTuple, TypedDict

from ..data import COMBOS


class NinjaAttr(IntFlag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()


class DeployNinja(NamedTuple):
    id_: int
    name: str
    atas: NinjaAttr
    kanan: NinjaAttr
    bawah: NinjaAttr
    kiri: NinjaAttr

    @property
    def attrs(self):
        return f"Up: {self.atas} Down: {self.bawah} Right: {self.kanan} Left: {self.kiri}"

    def get_available_combos(self):
        return tuple(k for k, v in COMBOS.items() if self.name in v["ninjas"])

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class NinjaDict(TypedDict):
    id: int
    attribute: List[str]
