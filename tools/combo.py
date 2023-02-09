from typing import List, Tuple, Union

import pandas as pd

from .models import DeployCombo, ComboAttr
from .utils import get_combos
from .data import COMBOS

__all__ = ["Combo"]

COMBO_COLUMNS = (
    ComboAttr.NAME,
    ComboAttr.ATK,
    ComboAttr.DEF,
    ComboAttr.HP,
    ComboAttr.AGI,
    ComboAttr.TRIGGER,
    ComboAttr.NINJAS,
)

TCOMB = Union[List[ComboAttr], ComboAttr]


class Combo:
    def __init__(self, combos: Tuple[DeployCombo, ...]) -> None:
        self.combos = combos

    @property
    def frame_combos(self):
        return pd.DataFrame(
            tuple((*c[1:7], len(c.ninjas)) for c in self.combos), columns=COMBO_COLUMNS
        )

    @property
    def total(self):
        return self.frame_combos.sum().iloc[1:6]

    def get_pref(self, pref: List[ComboAttr]):
        """Will Drop All Tables Thas has no :pref:

        Args:
            pref (List[ComboAttr]): List of preferences

        Returns:
            DataFrame
        """
        frame = self.frame_combos.loc[
            self.frame_combos.where(self.frame_combos[pref] > 0).dropna(how="all").index
        ]
        return frame

    def get_filter(self, pref: TCOMB) -> Tuple[DeployCombo, ...]:
        return tuple(self.combos[i] for i in self.get_pref(pref).index)

    def sort(self, *, by: TCOMB = ComboAttr.HP, asc=False) -> pd.DataFrame:
        return self.frame_combos.sort_values(by=by, ascending=asc)

    def get_index(self, idx: List[int]):
        return tuple(self.combos[i] for i in idx)

    @classmethod
    def get_by(cls, pref: List[ComboAttr]):
        comb = cls.get_all_combos()
        frame = comb.get_pref(pref)
        comb.combos = tuple(comb.combos[i] for i in frame.index)
        return comb

    @classmethod
    def get_all_combos(cls):
        return cls(get_combos(*tuple(COMBOS)))
