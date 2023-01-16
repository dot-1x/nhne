from ..data import NINJAS
from ..models.ninjas import DeployNinja, NinjaAttr

__all__ = [
    "get_ninja",
    "get_ninjas"
]

attr_mapping = {
    "Merah": NinjaAttr.RED,
    "Hijau": NinjaAttr.GREEN,
    "Biru": NinjaAttr.BLUE,
    "Kuning": NinjaAttr.YELLOW,
}


def get_ninja(ninja: str):
    if not ninja.title() in NINJAS:
        return None
    return DeployNinja(
        NINJAS.get(ninja.title())["id"],
        ninja.title(),
        *tuple(attr_mapping.get(a) for a in NINJAS.get(ninja.title())["attribute"])
    )


def get_ninjas(*ninjas: str):
    return tuple(get_ninja(n) for n in ninjas if n.title() in NINJAS)
