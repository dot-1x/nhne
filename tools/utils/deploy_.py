from typing import Tuple, Iterator
from time import perf_counter

from ..models import DeployNinja
from ..data import DEFAULT_TIMES


TDeploy = Tuple[DeployNinja, ...]
NODEPLOY = (0, None)


def check_connected(
    ninjas: TDeploy, main_ninjas: TDeploy
) -> Tuple[int, Tuple[TDeploy, TDeploy, TDeploy]]:
    row1, row2, row3 = (
        ninjas[:5],
        (ninjas[5], *main_ninjas, ninjas[6]),
        ninjas[7:],
    )
    upmid = sum(r1.bawah == r2.atas for r1, r2 in zip(row1, row2))
    downmid = sum(r2.bawah == r3.atas for r2, r3 in zip(row2, row3))

    righthand1 = sum(
        n1.kanan == n2.kiri for n1, n2 in zip(row1[:-1], row1[1:])
    )
    righthand2 = sum(
        n1.kanan == n2.kiri for n1, n2 in zip(row2[:-1], row2[1:])
    )
    righthand3 = sum(
        n1.kanan == n2.kiri for n1, n2 in zip(row3[:-1], row3[1:])
    )

    total = upmid + downmid + righthand1 + righthand2 + righthand3

    return total, (row1, row2, row3)


def get_best(
    data: list,
    perms: Iterator[TDeploy],
    main_ninjas: TDeploy,
    connected: int,
    deep: bool = False,
    starttime: float = 60 * DEFAULT_TIMES,
    times: float = DEFAULT_TIMES,
):
    if not deep:
        try:
            total, rows = max(
                (check_connected(d, main_ninjas) for d in perms),
                key=lambda k: k[0],
            )
        except ValueError:
            return NODEPLOY
        if total > connected:
            data.append((total, rows))
        return total, rows
    while True:
        if (perf_counter() - starttime) / 60 > times:
            return NODEPLOY
        res = next(perms, None)
        if res is None:
            return NODEPLOY
        total, rows = check_connected(res, main_ninjas)
        if total > connected:
            break
    data.append((total, rows))
    return total, rows
