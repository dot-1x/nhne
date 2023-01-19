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
    if ninja not in NINJAS:
        return None
    return DeployNinja(
        NINJAS.get(ninja)["id"], ninja.title(), *tuple(attr_mapping.get(a) for a in NINJAS.get(ninja)["attribute"])
    )


def get_ninjas(*ninjas: str):
    for n in ninjas:
        ninja = get_ninja(n)
        if not ninja:
            continue
        yield ninja
