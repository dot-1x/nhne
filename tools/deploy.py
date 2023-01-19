import asyncio
import math
from concurrent.futures import ThreadPoolExecutor
from itertools import chain, islice, permutations
from threading import Thread
from typing import List, Tuple

import pandas as pd

from .utils import check_connected, TDeploy, get_best, get_combos
from .data import MAX_NINJAS

__all__ = ["Deploy"]
TRESULT = List[Tuple[int, TDeploy]]


class Deploy:
    def __init__(self, ninjas: TDeploy, main_ninjas: TDeploy, ignore_dupe: bool = False) -> None:
        if len(ninjas + main_ninjas) != MAX_NINJAS:
            raise ValueError(f"Total Ninja Length must be {MAX_NINJAS}")

        dupes = [n for n in main_ninjas if n in ninjas]

        if not ignore_dupe and dupes:
            raise ValueError(f"Duplicate Ninja {dupes} Detected!")

        self.n = 1000
        self.permlen = math.perm(len(ninjas)) / self.n
        self.permutate = permutations(ninjas)

        conn, _ = check_connected(ninjas, main_ninjas)
        self.current_pipe = conn
        self.main = main_ninjas
        self.ninjas = ninjas
        self.rows = (ninjas[:5], (ninjas[5], *main_ninjas, ninjas[6]), ninjas[7:])

    def thread_fix(self, deep=False):
        jobs: List[Thread] = []
        res: TRESULT = []
        for x in range(self.n):
            job = Thread(
                target=get_best,
                args=[
                    res,
                    self.permutate if deep else islice(self.permutate, int(self.permlen * x), int(self.permlen * (x + 1))),
                    self.main,
                    self.current_pipe,
                    deep
                ],
            )
            jobs.append(job)
            job.start()

        for job in jobs:
            job.join()
        return max(res, key=lambda n: n[0])

    def get_combos(self):
        combs = set(list(chain.from_iterable(n.get_available_combos() for n in self.main + self.ninjas)))
        combos = tuple(get_combos(*list(c for c in combs)))
        for c in combos:
            for ninja in c.ninjas:
                if ninja not in self.ninjas + self.main:
                    break
            else:
                yield c

    def get_frame_combos(self):
        df = pd.DataFrame(tuple((*c[1:7], len(c.ninjas)) for c in self.get_combos()), columns=("name", "atk", "def", "hp", "agi", "trigger", "ninjas"))
        return df
