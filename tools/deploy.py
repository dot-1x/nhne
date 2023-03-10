import math
from itertools import islice, permutations
from threading import Thread
from time import perf_counter
from typing import List, Tuple

from .utils import check_connected, TDeploy, get_best, get_combos
from .data import MAX_NINJAS, DEFAULT_TIMES
from .combo import Combo

__all__ = ["Deploy"]
TRESULT = List[Tuple[int, Tuple[TDeploy, TDeploy, TDeploy]]]


class Deploy:
    """Base class for deploy"""

    def __init__(
        self,
        ninjas: TDeploy,
        main_ninjas: TDeploy,
        ignore_dupe: bool = False,
    ) -> None:
        if len(ninjas + main_ninjas) != MAX_NINJAS:
            raise ValueError(f"Total Ninja Length must be {MAX_NINJAS}")

        dupes = [n for n in main_ninjas if n in ninjas]

        if not ignore_dupe and dupes:
            raise ValueError(f"Duplicate Ninja {dupes} Detected!")

        self.permlen = math.perm(len(ninjas))
        self.permutate = permutations(ninjas)

        self.current_pipe, rows = check_connected(ninjas, main_ninjas)
        self.main = main_ninjas
        self.ninjas = ninjas
        self.rows = rows

    def fix_pipe(self, deep=False, times=DEFAULT_TIMES) -> "Deploy":
        jobs: List[Thread] = []
        res: TRESULT = []
        divide = 1000
        permlen = self.permlen / divide

        start = perf_counter()
        for idx in range(divide):
            job = Thread(
                target=get_best,
                args=[
                    res,
                    self.permutate
                    if deep
                    else islice(
                        self.permutate,
                        int(permlen * idx),
                        int(permlen * (idx + 1)),
                    ),
                    self.main,
                    self.current_pipe,
                    deep,
                    start,
                    times,
                ],
            )
            jobs.append(job)
            job.start()

        for job in jobs:
            job.join()

        if not res:
            return self
        _, ninjas = max(res, key=lambda n: n[0])
        new_dep = Deploy(
            (*ninjas[0], ninjas[1][0], ninjas[1][-1], *ninjas[-1]),
            (ninjas[1][1:4]),
        )
        if deep and (perf_counter() - start) / 60 < times:
            return new_dep.fix_pipe(
                deep=True,
                times=times - ((perf_counter() - start) / 60),
            )

        return new_dep

    def get_combos(self):
        combs = set(
            c for n in self.main + self.ninjas for c in n.get_available_combos()
        )
        combos = get_combos(*combs)
        for combo in combos:
            for ninja in combo.ninjas:
                if ninja not in self.ninjas + self.main:
                    break
            else:
                yield combo

    @property
    def combo(self):
        return Combo(tuple(self.get_combos()))

    def __repr__(self):
        return f"Connected Pipes: {self.current_pipe}\n" + "\n".join(
            f"r{n}: {v}" for n, v in enumerate(self.rows, start=1)
        )
