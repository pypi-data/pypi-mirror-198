from pathlib import Path
import sys
import threading
from types import CodeType, FrameType, ModuleType
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, cast

from reloadium.corium import ll1l1ll111l11ll1Il1l1, l11l1ll1l1l1l11lIl1l1, public, lllll1l1l11l1111Il1l1, l111lll111111lllIl1l1
from reloadium.corium.l1ll1llll11llll1Il1l1 import l11llllll1lll111Il1l1, ll11l11l11lll1llIl1l1
from reloadium.corium.l11l1ll1l1l1l11lIl1l1 import lllll11l1l1l111lIl1l1, llll11l11l11ll1lIl1l1
from reloadium.corium.lll111l11lllll11Il1l1 import l111l11111l11111Il1l1
from reloadium.corium.l1l11lll1llll111Il1l1 import l1l11lll1llll111Il1l1
from reloadium.corium.l111l1l1l1llllllIl1l1 import llll1lll11111l1lIl1l1
from reloadium.corium.lllll1lllllll1l1Il1l1 import llll1l11l1ll1lllIl1l1, llll1llll111l11lIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True

__all__ = ['llll1l11l1111l11Il1l1', 'l1l1lll111lll111Il1l1', 'l1l1lll11l11ll1lIl1l1']


lll1l111l1l1l111Il1l1 = l1l11lll1llll111Il1l1.l1111l1111111111Il1l1(__name__)


class llll1l11l1111l11Il1l1:
    @classmethod
    def lll1lll1l1l11111Il1l1(lll1ll1ll1l1111lIl1l1) -> Optional[FrameType]:
        lll1111ll111lll1Il1l1: FrameType = sys._getframe(2)
        llllll111111l111Il1l1 = next(l111lll111111lllIl1l1.lll1111ll111lll1Il1l1.lllll1ll1ll1111lIl1l1(lll1111ll111lll1Il1l1))
        return llllll111111l111Il1l1


class l1l1lll111lll111Il1l1(llll1l11l1111l11Il1l1):
    @classmethod
    def l111l111ll11ll1lIl1l1(ll1ll11l1111l11lIl1l1, l11111l11l111111Il1l1: List[Any], ll1lllll1l1ll11lIl1l1: Dict[str, Any], lll111l1lll1ll1lIl1l1: List[llll1l11l1ll1lllIl1l1]) -> Any:  # type: ignore
        with llll11l11l11ll1lIl1l1():
            assert l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.ll1ll1llll11111lIl1l1
            lll1111ll111lll1Il1l1 = l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.ll1ll1llll11111lIl1l1.l11111111111l11lIl1l1.l1ll11l1ll1ll1l1Il1l1()
            lll1111ll111lll1Il1l1.l1l1lll1l11ll1l1Il1l1()

            lll11l111l11l11lIl1l1 = l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.l1l1111ll1ll11llIl1l1.l11111l1ll1ll11lIl1l1(lll1111ll111lll1Il1l1.l1ll111l1l11lll1Il1l1, lll1111ll111lll1Il1l1.l1ll11ll1llll11lIl1l1.lll111llll1l11l1Il1l1())
            assert lll11l111l11l11lIl1l1
            l1l1l111l1ll11llIl1l1 = ll1ll11l1111l11lIl1l1.lll1lll1l1l11111Il1l1()

            for ll1ll1111l1l111lIl1l1 in lll111l1lll1ll1lIl1l1:
                ll1ll1111l1l111lIl1l1.lll1l11ll1l11lllIl1l1()

            for ll1ll1111l1l111lIl1l1 in lll111l1lll1ll1lIl1l1:
                ll1ll1111l1l111lIl1l1.llll1lll1llll111Il1l1()


        llllll111111l111Il1l1 = lll11l111l11l11lIl1l1(*l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1);        lll1111ll111lll1Il1l1.l111l111lll11l11Il1l1.additional_info.pydev_step_stop = l1l1l111l1ll11llIl1l1  # type: ignore

        return llllll111111l111Il1l1

    @classmethod
    async def ll11l1l1ll1l1l1lIl1l1(ll1ll11l1111l11lIl1l1, l11111l11l111111Il1l1: List[Any], ll1lllll1l1ll11lIl1l1: Dict[str, Any], lll111l1lll1ll1lIl1l1: List[llll1llll111l11lIl1l1]) -> Any:  # type: ignore
        with llll11l11l11ll1lIl1l1():
            assert l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.ll1ll1llll11111lIl1l1
            lll1111ll111lll1Il1l1 = l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.ll1ll1llll11111lIl1l1.l11111111111l11lIl1l1.l1ll11l1ll1ll1l1Il1l1()
            lll1111ll111lll1Il1l1.l1l1lll1l11ll1l1Il1l1()

            lll11l111l11l11lIl1l1 = l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.l1l1111ll1ll11llIl1l1.l11111l1ll1ll11lIl1l1(lll1111ll111lll1Il1l1.l1ll111l1l11lll1Il1l1, lll1111ll111lll1Il1l1.l1ll11ll1llll11lIl1l1.lll111llll1l11l1Il1l1())
            assert lll11l111l11l11lIl1l1
            l1l1l111l1ll11llIl1l1 = ll1ll11l1111l11lIl1l1.lll1lll1l1l11111Il1l1()

            for ll1ll1111l1l111lIl1l1 in lll111l1lll1ll1lIl1l1:
                await ll1ll1111l1l111lIl1l1.lll1l11ll1l11lllIl1l1()

            for ll1ll1111l1l111lIl1l1 in lll111l1lll1ll1lIl1l1:
                await ll1ll1111l1l111lIl1l1.llll1lll1llll111Il1l1()


        llllll111111l111Il1l1 = await lll11l111l11l11lIl1l1(*l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1);        lll1111ll111lll1Il1l1.l111l111lll11l11Il1l1.additional_info.pydev_step_stop = l1l1l111l1ll11llIl1l1  # type: ignore

        return llllll111111l111Il1l1


class l1l1lll11l11ll1lIl1l1(llll1l11l1111l11Il1l1):
    @classmethod
    def l111l111ll11ll1lIl1l1(ll1ll11l1111l11lIl1l1) -> Optional[ModuleType]:  # type: ignore
        with llll11l11l11ll1lIl1l1():
            assert l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.ll1ll1llll11111lIl1l1
            lll1111ll111lll1Il1l1 = l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.ll1ll1llll11111lIl1l1.l11111111111l11lIl1l1.l1ll11l1ll1ll1l1Il1l1()

            l1l1l11l1l11ll11Il1l1 = Path(lll1111ll111lll1Il1l1.llllllll11lll11lIl1l1.f_globals['__spec__'].origin).absolute()
            l1llllll1111llllIl1l1 = lll1111ll111lll1Il1l1.llllllll11lll11lIl1l1.f_globals['__name__']
            lll1111ll111lll1Il1l1.l1l1lll1l11ll1l1Il1l1()
            llll11l111l1ll1lIl1l1 = l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.lll11l11lll1lll1Il1l1.lll1111ll1l1ll11Il1l1(l1l1l11l1l11ll11Il1l1)

            if ( not llll11l111l1ll1lIl1l1):
                lll1l111l1l1l111Il1l1.lllll1llllll1l1lIl1l1('Could not retrieve src.', llll111l111111llIl1l1={'file': llll1lll11111l1lIl1l1.l1l1l1lll1llll1lIl1l1(l1l1l11l1l11ll11Il1l1), 
'fullname': llll1lll11111l1lIl1l1.l1llllll1111llllIl1l1(l1llllll1111llllIl1l1)})

            assert llll11l111l1ll1lIl1l1

        try:
            llll11l111l1ll1lIl1l1.l1111l1lll1l11l1Il1l1()
            llll11l111l1ll1lIl1l1.l11lll11lll11l11Il1l1(l1ll111l111l111lIl1l1=False)
            llll11l111l1ll1lIl1l1.ll11ll1llllll111Il1l1(l1ll111l111l111lIl1l1=False)
        except lllll11l1l1l111lIl1l1 as l1ll1l11llll1111Il1l1:
            lll1111ll111lll1Il1l1.l1l1l1ll1ll1llllIl1l1(l1ll1l11llll1111Il1l1)
            return None

        import importlib.util

        ll1llll1ll1l11llIl1l1 = lll1111ll111lll1Il1l1.llllllll11lll11lIl1l1.f_locals['__spec__']
        l111ll1l1111l1l1Il1l1 = importlib.util.module_from_spec(ll1llll1ll1l11llIl1l1)

        llll11l111l1ll1lIl1l1.l11l1ll1l1l1llllIl1l1(l111ll1l1111l1l1Il1l1)
        return l111ll1l1111l1l1Il1l1


ll11l11l11lll1llIl1l1.l1llll11lllllll1Il1l1(l11llllll1lll111Il1l1.llll11lll11ll1l1Il1l1, l1l1lll111lll111Il1l1.l111l111ll11ll1lIl1l1)
ll11l11l11lll1llIl1l1.l1llll11lllllll1Il1l1(l11llllll1lll111Il1l1.ll1lll1111ll1l1lIl1l1, l1l1lll111lll111Il1l1.ll11l1l1ll1l1l1lIl1l1)
ll11l11l11lll1llIl1l1.l1llll11lllllll1Il1l1(l11llllll1lll111Il1l1.l1lll11l111llll1Il1l1, l1l1lll11l11ll1lIl1l1.l111l111ll11ll1lIl1l1)
