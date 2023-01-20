from ..data import NINJAS
from ..models.ninjas import DeployNinja, NinjaAttr

__all__ = ["get_ninja", "get_ninjas"]

attr_mapping = {
    "Merah": NinjaAttr.RED,
    "Hijau": NinjaAttr.GREEN,
    "Biru": NinjaAttr.BLUE,
    "Kuning": NinjaAttr.YELLOW,
}


def get_ninja(ninja: str):
    ninja_ = NINJAS.get(ninja.lower())
    if ninja_ is None:
        raise ValueError(f"Invalid Ninja {ninja}")
    return DeployNinja(
        ninja_["id"], ninja.title(), *tuple(attr_mapping.get(a) for a in ninja_["attribute"])
    )


def get_ninjas(*ninjas: str):
    return tuple(get_ninja(n) for n in ninjas)