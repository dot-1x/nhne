from __future__ import annotations

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
    def frame(self):
        return pd.DataFrame(
            tuple((*c[1:7], len(c.ninjas)) for c in self.combos),
            columns=COMBO_COLUMNS,
        )

    @property
    def total(self):
        return self.frame.sum().iloc[1:6]

    def get_pref(self, pref: TCOMB):
        """Will Drop All Tables Thas has no :pref:

        Args:
            pref (List[ComboAttr] | ComboAttr): List of preferences

        Returns:
            DataFrame: only containing preferenced combos
        """
        frame = self.frame.loc[
            self.frame.where(self.frame[pref] > 0).dropna(how="all").index
        ]
        return frame

    def get_filter(self, pref: TCOMB) -> Tuple[DeployCombo, ...]:
        return tuple(self.combos[i] for i in self.get_pref(pref).index)

    def filter(self, pref: TCOMB) -> Combo:
        """Return new Combo object with combos filtered

        Args:
            pref (TCOMB): preferences to keep

        Returns:
            Combo: new Combo with only preferenced combo
        """
        filtered = self.get_filter(pref)
        return Combo(filtered)

    def sort(self, *, by: TCOMB = ComboAttr.HP, asc=False) -> pd.DataFrame:
        return self.frame.sort_values(by=by, ascending=asc)

    def get_index(self, idx: List[int]):
        return tuple(self.combos[i] for i in idx)

    @classmethod
    def get_by(cls, pref: TCOMB) -> Combo:
        """Get all available combo and filter them by preferences

        Args:
            pref (TCOMB): preferences to keep

        Returns:
            Combo
        """
        comb = cls.get_all_combos()
        frame = comb.get_pref(pref)
        comb.combos = tuple(comb.combos[i] for i in frame.index)
        return comb

    @classmethod
    def get_all_combos(cls) -> Combo:
        """Get all current available combos

        Returns:
            Combo
        """
        return cls(get_combos(*tuple(COMBOS)))

    def __repr__(self):
        return f"Achieved Combo:\n{self.frame}\n\nTotal:\n{self.total}"
