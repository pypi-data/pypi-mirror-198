import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type, Union, cast

from reloadium.lib.lll1l11111lll1l1Il1l1.llllllllll1l1ll1Il1l1 import l11ll1ll11lllll1Il1l1
from reloadium.lib import ll1l1ll1l11ll111Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class l11l111llll1111lIl1l1(l11ll1ll11lllll1Il1l1):
    ll11ll1l1llll1l1Il1l1 = 'Multiprocessing'

    def __post_init__(lll1ll1ll1l1111lIl1l1) -> None:
        super().__post_init__()

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> None:
        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(l111ll1l1111l1l1Il1l1, 'multiprocessing.popen_spawn_posix')):
            lll1ll1ll1l1111lIl1l1.ll11llll11ll11llIl1l1(l111ll1l1111l1l1Il1l1)

        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(l111ll1l1111l1l1Il1l1, 'multiprocessing.popen_spawn_win32')):
            lll1ll1ll1l1111lIl1l1.lll1ll1lll1lll11Il1l1(l111ll1l1111l1l1Il1l1)

    def ll11llll11ll11llIl1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_posix
        multiprocessing.popen_spawn_posix.Popen._launch = ll1l1ll1l11ll111Il1l1.l111l1111ll11l11Il1l1.ll1111l11ll1lll1Il1l1  # type: ignore

    def lll1ll1lll1lll11Il1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_win32
        multiprocessing.popen_spawn_win32.Popen.__init__ = ll1l1ll1l11ll111Il1l1.l111l1111ll11l11Il1l1.__init__  # type: ignore
