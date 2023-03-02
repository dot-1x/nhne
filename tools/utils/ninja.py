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
    splitted = list(ninja) if ninja.isupper() else ninja.split()
    found = NINJAS.get(ninja.lower())  # checks the passed string first
    if found is None:  # if not found then provide regex search
        pattern = "".join(
            "".join(rf"{isupper}\w+ " for isupper in word)
            if word.isupper()
            else f"{word} "
            for word in splitted
        )
        for key in NINJAS:
            if re.search(pattern.strip(), key.title()):
                found = NINJAS.get(key)  # if found then we break the loop
                ninja = key
                break
    if not found:  # double check the result, mypy won't recognize for . else statement
        raise ValueError(f"Invalid ninja {ninja}")
    return DeployNinja(
        found["id"],
        ninja.title(),
        *tuple(attr_mapping.get(a, NinjaAttr.RED) for a in found["attribute"]),
    )


def get_ninjas(*ninjas: str):
    return tuple(get_ninja(n) for n in ninjas)


def get_upstats(current_quality: float, default: float, stars: int, dupes: int):
    return (
        (current_quality - default) / (stars + dupes)
        if (stars + dupes)
        else (current_quality - default)
    )


def get_quality(default: float, upstats: float, stars: int = 0, dupe: int = 0):
    return default + (upstats * (stars + dupe))
