from enum import IntFlag, auto
from typing import NamedTuple


class NinjaAttr(IntFlag):
    RED = auto()
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()


class Deploy(NamedTuple):
    id: int
    name: str
    atas: NinjaAttr
    kanan: NinjaAttr
    bawah: NinjaAttr
    kiri: NinjaAttr
