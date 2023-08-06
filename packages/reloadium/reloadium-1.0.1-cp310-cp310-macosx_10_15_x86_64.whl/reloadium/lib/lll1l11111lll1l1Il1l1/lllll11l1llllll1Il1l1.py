import sys
from contextlib import contextmanager
from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type

from reloadium.corium.l111lll111111lllIl1l1 import lll1l1lllll1l1llIl1l1
from reloadium.lib.environ import env
from reloadium.corium.l11l1ll1l1l1l11lIl1l1 import llll11l11l11ll1lIl1l1
from reloadium.lib.lll1l11111lll1l1Il1l1.ll1l11l11ll1ll11Il1l1 import l11ll1l1l11l11llIl1l1
from reloadium.corium.ll11111l1111ll1lIl1l1 import l1llll1l11l111l1Il1l1, l1ll11l111l111llIl1l1, llllll1l11l1l11lIl1l1, l1l1111lll1lllllIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass
else:
    from reloadium.vendored.dataclasses import dataclass


__RELOADIUM__ = True


@dataclass
class l111l1ll1l1l11l1Il1l1(l11ll1l1l11l11llIl1l1):
    ll11ll1l1llll1l1Il1l1 = 'FastApi'

    l1111l1ll1111lllIl1l1 = 'uvicorn'

    @contextmanager
    def ll11ll1ll11lll11Il1l1(lll1ll1ll1l1111lIl1l1) -> Generator[None, None, None]:
        yield 

    def ll11l1lllll111l1Il1l1(lll1ll1ll1l1111lIl1l1) -> List[Type[l1ll11l111l111llIl1l1]]:
        return []

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, lll111111lllll11Il1l1: types.ModuleType) -> None:
        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(lll111111lllll11Il1l1, lll1ll1ll1l1111lIl1l1.l1111l1ll1111lllIl1l1)):
            lll1ll1ll1l1111lIl1l1.ll11l111111lllllIl1l1()

    @classmethod
    def l1l11lllll1l111lIl1l1(ll1ll11l1111l11lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> bool:
        llllll111111l111Il1l1 = super().l1l11lllll1l111lIl1l1(l111ll1l1111l1l1Il1l1)
        llllll111111l111Il1l1 |= l111ll1l1111l1l1Il1l1.__name__ == ll1ll11l1111l11lIl1l1.l1111l1ll1111lllIl1l1
        return llllll111111l111Il1l1

    def ll11l111111lllllIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        l11llll1111lll11Il1l1 = '--reload'
        if (l11llll1111lll11Il1l1 in sys.argv):
            sys.argv.remove('--reload')
