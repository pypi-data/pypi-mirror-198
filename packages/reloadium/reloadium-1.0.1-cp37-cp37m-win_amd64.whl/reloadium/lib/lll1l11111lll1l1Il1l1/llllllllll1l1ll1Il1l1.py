from abc import ABC
from contextlib import contextmanager
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.l1l11lll1llll111Il1l1 import l1111l1l1l11lll1Il1l1, l1l11lll1llll111Il1l1
from reloadium.corium.ll11111l1111ll1lIl1l1 import llllllll1l1l1lllIl1l1, l1ll11l111l111llIl1l1
from reloadium.corium.lllll1lllllll1l1Il1l1 import llll1l11l1ll1lllIl1l1, llll1llll111l11lIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from reloadium.lib.lll1l11111lll1l1Il1l1.lll1l11l111lllllIl1l1 import l1lll1l11ll111llIl1l1
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class l11ll1ll11lllll1Il1l1:
    lll1l11l111lllllIl1l1: "l1lll1l11ll111llIl1l1"

    ll11ll1l1llll1l1Il1l1: ClassVar[str] = NotImplemented
    l1111llllll11ll1Il1l1: bool = field(init=False, default=False)

    l11lll11111l1111Il1l1: l1111l1l1l11lll1Il1l1 = field(init=False)

    def __post_init__(lll1ll1ll1l1111lIl1l1) -> None:
        lll1ll1ll1l1111lIl1l1.l11lll11111l1111Il1l1 = l1l11lll1llll111Il1l1.l1111l1111111111Il1l1(lll1ll1ll1l1111lIl1l1.ll11ll1l1llll1l1Il1l1)
        lll1ll1ll1l1111lIl1l1.l11lll11111l1111Il1l1.lll11l1llll111llIl1l1('Creating extension')
        lll1ll1ll1l1111lIl1l1.lll1l11l111lllllIl1l1.l11llll1lll1ll11Il1l1.l1ll1111l1ll11l1Il1l1.llll11llll111l1lIl1l1(lll1ll1ll1l1111lIl1l1.lll1l1llllll11llIl1l1())

    def lll1l1llllll11llIl1l1(lll1ll1ll1l1111lIl1l1) -> List[Type[l1ll11l111l111llIl1l1]]:
        llllll111111l111Il1l1 = []
        ll11111l1111ll1lIl1l1 = lll1ll1ll1l1111lIl1l1.ll11l1lllll111l1Il1l1()
        for llll1lll1111ll11Il1l1 in ll11111l1111ll1lIl1l1:
            llll1lll1111ll11Il1l1.l1111l1l1l1lll11Il1l1 = lll1ll1ll1l1111lIl1l1.ll11ll1l1llll1l1Il1l1

        llllll111111l111Il1l1.extend(ll11111l1111ll1lIl1l1)
        return llllll111111l111Il1l1

    def ll1l1ll11lll1l1lIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        lll1ll1ll1l1111lIl1l1.l1111llllll11ll1Il1l1 = True

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> None:
        pass

    @classmethod
    def l1l11lllll1l111lIl1l1(ll1ll11l1111l11lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> bool:
        if ( not hasattr(l111ll1l1111l1l1Il1l1, '__name__')):
            return False

        llllll111111l111Il1l1 = l111ll1l1111l1l1Il1l1.__name__.split('.')[0].lower() == ll1ll11l1111l11lIl1l1.ll11ll1l1llll1l1Il1l1.lower()
        return llllll111111l111Il1l1

    @contextmanager
    def ll11ll1ll11lll11Il1l1(lll1ll1ll1l1111lIl1l1) -> Generator[None, None, None]:
        yield 

    def ll1ll11l11l1l1llIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        pass

    def l1l1l1l11111l11lIl1l1(lll1ll1ll1l1111lIl1l1, lllll1111l1lll11Il1l1: Exception) -> None:
        pass

    def ll1111l1111lll1lIl1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional[llll1l11l1ll1lllIl1l1]:
        return None

    async def l11ll1l1l1l1lll1Il1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional[llll1llll111l11lIl1l1]:
        return None

    def ll1llll111111ll1Il1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional[llll1l11l1ll1lllIl1l1]:
        return None

    async def l1ll11l1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional[llll1llll111l11lIl1l1]:
        return None

    def ll1l1l1lll11llllIl1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path) -> None:
        pass

    def l1l111llll1lll1lIl1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path) -> None:
        pass

    def l1l11l1l1l1111l1Il1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path, lllll1l11ll11111Il1l1: List[llllllll1l1l1lllIl1l1]) -> None:
        pass

    def __eq__(lll1ll1ll1l1111lIl1l1, ll11111111ll11llIl1l1: Any) -> bool:
        return id(ll11111111ll11llIl1l1) == id(lll1ll1ll1l1111lIl1l1)

    def ll11l1lllll111l1Il1l1(lll1ll1ll1l1111lIl1l1) -> List[Type[l1ll11l111l111llIl1l1]]:
        return []

    def ll11l11ll11l111lIl1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType, lll11111l111llllIl1l1: str) -> bool:
        llllll111111l111Il1l1 = (hasattr(l111ll1l1111l1l1Il1l1, '__name__') and l111ll1l1111l1l1Il1l1.__name__ == lll11111l111llllIl1l1)
        return llllll111111l111Il1l1


@dataclass(repr=False)
class lll1l1ll11l111l1Il1l1(llll1l11l1ll1lllIl1l1):
    llllllllll1l1ll1Il1l1: l11ll1ll11lllll1Il1l1

    def __repr__(lll1ll1ll1l1111lIl1l1) -> str:
        return 'ExtensionMemento'


@dataclass(repr=False)
class l11ll1lll1lll11lIl1l1(llll1llll111l11lIl1l1):
    llllllllll1l1ll1Il1l1: l11ll1ll11lllll1Il1l1

    def __repr__(lll1ll1ll1l1111lIl1l1) -> str:
        return 'AsyncExtensionMemento'
