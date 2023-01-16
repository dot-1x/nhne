import asyncio
import math
from concurrent.futures import ProcessPoolExecutor
from itertools import islice, permutations
import re
from typing import Iterator, Tuple

from .models.ninjas import DeployNinja

__all__ = [
    "check_connected",
    "fix_pipe"

]
TDeploy = Tuple[DeployNinja, ...]

loop = asyncio.get_event_loop()


def check_connected(
    ninjas: TDeploy, main_ninjas: TDeploy
):
    row1, row2, row3 = (ninjas[:5], (ninjas[5], *main_ninjas, ninjas[6]), ninjas[7:])

    upmid = sum(r1.bawah == r2.atas for r1, r2 in zip(row1, row2))
    downmid = sum(r2.bawah == r3.atas for r2, r3 in zip(row2, row3))
    righthand1 = sum(n1.kanan == n2.kiri for n1, n2 in zip(row1[:-1], row1[1:]))
    righthand2 = sum(n1.kanan == n2.kiri for n1, n2 in zip(row2[:-1], row2[1:]))
    righthand3 = sum(n1.kanan == n2.kiri for n1, n2 in zip(row3[:-1], row3[1:]))

    total = upmid + downmid + righthand1 + righthand2 + righthand3

    return total, (row1, row2, row3)


def get_best(
    perms: Iterator[DeployNinja],
    main_ninjas: Tuple[DeployNinja],
    connected: int,
    start: int,
    stop: int,
):
    _perms = islice(perms, start, stop)
    while True:
        res = next(_perms, None)
        if not res:
            return None
        total, rows = check_connected(res, main_ninjas)
        if total > connected:
            break
    return total, rows


async def _fix_pipe(ninjas: TDeploy, main_ninjas: TDeploy):
    n = 1000
    permlen = math.perm(len(ninjas)) / n
    permutate = permutations(ninjas)
    conn, _ = check_connected(ninjas, main_ninjas)
    with ProcessPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(
                pool,
                get_best,
                permutate,
                main_ninjas,
                conn,
                int(permlen * x),
                int(permlen * (x + 1) if x != (n - 1) else permlen * n),
            )
            for x in range(n)
        ]
        asyncio.gather(*tasks)
    return permutate


def fix_pipe(ninjas: TDeploy, main_ninjas: TDeploy):
    if not loop.is_running():
        res = loop.run_until_complete(_fix_pipe(ninjas, main_ninjas))
    else:
        res = asyncio.create_task(_fix_pipe(ninjas, main_ninjas))
        while True:
            if res.done():
                return res.result()
