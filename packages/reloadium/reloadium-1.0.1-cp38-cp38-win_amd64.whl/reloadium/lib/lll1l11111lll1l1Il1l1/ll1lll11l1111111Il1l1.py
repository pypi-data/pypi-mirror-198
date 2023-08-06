from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, List

from reloadium.lib.lll1l11111lll1l1Il1l1.llllllllll1l1ll1Il1l1 import l11ll1ll11lllll1Il1l1
from reloadium.corium.ll11111l1111ll1lIl1l1 import llllllll1l1l1lllIl1l1
from reloadium.corium.l111lll111111lllIl1l1 import lll1l1lllll1l1llIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class l1l1lll11111111lIl1l1(l11ll1ll11lllll1Il1l1):
    ll11ll1l1llll1l1Il1l1 = 'PyGame'

    ll111111l1llllllIl1l1: bool = field(init=False, default=False)

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, lll111111lllll11Il1l1: types.ModuleType) -> None:
        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(lll111111lllll11Il1l1, 'pygame.base')):
            lll1ll1ll1l1111lIl1l1.l11lll1111l1l1l1Il1l1()

    def l11lll1111l1l1l1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        import pygame.display

        llll11l1l11l11l1Il1l1 = pygame.display.update

        def lll11l11l11ll1l1Il1l1(*l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> None:
            if (lll1ll1ll1l1111lIl1l1.ll111111l1llllllIl1l1):
                lll1l1lllll1l1llIl1l1.l11lll1l11l11l1lIl1l1(0.1)
                return None
            else:
                return llll11l1l11l11l1Il1l1(*l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1)

        pygame.display.update = lll11l11l11ll1l1Il1l1

    def l1l111llll1lll1lIl1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path) -> None:
        lll1ll1ll1l1111lIl1l1.ll111111l1llllllIl1l1 = True

    def l1l11l1l1l1111l1Il1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path, lllll1l11ll11111Il1l1: List[llllllll1l1l1lllIl1l1]) -> None:
        lll1ll1ll1l1111lIl1l1.ll111111l1llllllIl1l1 = False

    def l1l1l1l11111l11lIl1l1(lll1ll1ll1l1111lIl1l1, lllll1111l1lll11Il1l1: Exception) -> None:
        lll1ll1ll1l1111lIl1l1.ll111111l1llllllIl1l1 = False
