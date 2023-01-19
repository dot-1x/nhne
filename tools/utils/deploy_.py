from typing import Tuple, Iterator
from itertools import islice

from ..models import DeployNinja

TDeploy = Tuple[DeployNinja, ...]


def check_connected(ninjas: TDeploy, main_ninjas: TDeploy) -> Tuple[int, Tuple[TDeploy, TDeploy, TDeploy]]:
    row1, row2, row3 = (ninjas[:5], (ninjas[5], *main_ninjas, ninjas[6]), ninjas[7:])
    upmid = sum(r1.bawah == r2.atas for r1, r2 in zip(row1, row2))
    downmid = sum(r2.bawah == r3.atas for r2, r3 in zip(row2, row3))
    righthand1 = sum(n1.kanan == n2.kiri for n1, n2 in zip(row1[:-1], row1[1:]))
    righthand2 = sum(n1.kanan == n2.kiri for n1, n2 in zip(row2[:-1], row2[1:]))
    righthand3 = sum(n1.kanan == n2.kiri for n1, n2 in zip(row3[:-1], row3[1:]))

    total = upmid + downmid + righthand1 + righthand2 + righthand3

    return total, (row1, row2, row3)


def get_best(
    data: list,
    perms: Iterator[TDeploy],
    main_ninjas: TDeploy,
    connected: int,
    deep: bool = False
):
    if not deep:
        try:
            total, rows = max((check_connected(d, main_ninjas) for d in perms), key=lambda k: k[0])
        except ValueError:
            return 0, None
        else:
            data.append((total, rows))
        return total, rows
    while True:
        res = next(perms, None)
        if res is None:
            return 0, None
        total, rows = check_connected(res, main_ninjas)
        if total > connected:
            break
    data.append((total, rows))
    return total, rows
