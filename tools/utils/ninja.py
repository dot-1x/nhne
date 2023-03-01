import re
from ..data import NINJAS
from ..models.ninjas import DeployNinja, NinjaAttr

__all__ = ["get_ninja", "get_ninjas", "get_upstats"]

attr_mapping = {
    "Merah": NinjaAttr.RED,
    "Hijau": NinjaAttr.GREEN,
    "Biru": NinjaAttr.BLUE,
    "Kuning": NinjaAttr.YELLOW,
}


def get_ninja(ninja: str):
    if ninja.isupper():
        found = [n for n in NINJAS if re.search(r"\w+ ".join(ninja), n.title())]
        ninja = found[0] or ninja
    ninja_ = NINJAS.get(ninja.lower())
    if ninja_ is None:
        raise ValueError(f"Invalid Ninja {ninja}")
    return DeployNinja(
        ninja_["id"],
        ninja.title(),
        *tuple(attr_mapping.get(a, NinjaAttr.RED) for a in ninja_["attribute"]),
    )


def get_ninjas(*ninjas: str):
    return tuple(get_ninja(n) for n in ninjas)


def get_upstats(
    current_quality: float, default: float, stars: int, dupes: int
):
    return (
        (current_quality - default) / (stars + dupes)
        if (stars + dupes)
        else (current_quality - default)
    )
