import re
from contextlib import contextmanager
import os
import sys
import types
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Set, Tuple, Union

from reloadium.corium.l11l1ll1l1l1l11lIl1l1 import llll11l11l11ll1lIl1l1
from reloadium.lib.lll1l11111lll1l1Il1l1.llllllllll1l1ll1Il1l1 import l11ll1ll11lllll1Il1l1, lll1l1ll11l111l1Il1l1
from reloadium.corium.lllll1lllllll1l1Il1l1 import llll1l11l1ll1lllIl1l1
from reloadium.corium.l111lll111111lllIl1l1 import lll1l1lllll1l1llIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from sqlalchemy.engine.base import Engine, Transaction
    from sqlalchemy.orm.session import Session
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass(repr=False)
class l1ll111l1ll111l1Il1l1(lll1l1ll11l111l1Il1l1):
    llllllllll1l1ll1Il1l1: "ll1lll1ll1l111llIl1l1"
    ll111lll1ll1l11lIl1l1: List["Transaction"] = field(init=False, default_factory=list)

    def l1l111l1l11lll11Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        from sqlalchemy.orm.session import _sessions

        super().l1l111l1l11lll11Il1l1()

        lll1l1ll1lll111lIl1l1 = list(_sessions.values())

        for ll1ll11l111llll1Il1l1 in lll1l1ll1lll111lIl1l1:
            if ( not ll1ll11l111llll1Il1l1.is_active):
                continue

            lllll1l1l1111ll1Il1l1 = ll1ll11l111llll1Il1l1.begin_nested()
            lll1ll1ll1l1111lIl1l1.ll111lll1ll1l11lIl1l1.append(lllll1l1l1111ll1Il1l1)

    def __repr__(lll1ll1ll1l1111lIl1l1) -> str:
        return 'DbMemento'

    def lll1l11ll1l11lllIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().lll1l11ll1l11lllIl1l1()

        while lll1ll1ll1l1111lIl1l1.ll111lll1ll1l11lIl1l1:
            lllll1l1l1111ll1Il1l1 = lll1ll1ll1l1111lIl1l1.ll111lll1ll1l11lIl1l1.pop()
            if (lllll1l1l1111ll1Il1l1.is_active):
                try:
                    lllll1l1l1111ll1Il1l1.rollback()
                except :
                    pass

    def llll1lll1llll111Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().llll1lll1llll111Il1l1()

        while lll1ll1ll1l1111lIl1l1.ll111lll1ll1l11lIl1l1:
            lllll1l1l1111ll1Il1l1 = lll1ll1ll1l1111lIl1l1.ll111lll1ll1l11lIl1l1.pop()
            if (lllll1l1l1111ll1Il1l1.is_active):
                try:
                    lllll1l1l1111ll1Il1l1.commit()
                except :
                    pass


@dataclass
class ll1lll1ll1l111llIl1l1(l11ll1ll11lllll1Il1l1):
    ll11ll1l1llll1l1Il1l1 = 'Sqlalchemy'

    lllll1111lll1111Il1l1: List["Engine"] = field(init=False, default_factory=list)
    lll1l1ll1lll111lIl1l1: Set["Session"] = field(init=False, default_factory=set)
    l1l1ll11l1l111llIl1l1: Tuple[int, ...] = field(init=False)

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> None:
        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(l111ll1l1111l1l1Il1l1, 'sqlalchemy')):
            lll1ll1ll1l1111lIl1l1.lll1l11l1l11lll1Il1l1(l111ll1l1111l1l1Il1l1)

        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(l111ll1l1111l1l1Il1l1, 'sqlalchemy.engine.base')):
            lll1ll1ll1l1111lIl1l1.l1l1l11ll111l1l1Il1l1(l111ll1l1111l1l1Il1l1)

    def lll1l11l1l11lll1Il1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: Any) -> None:
        lll11ll1ll1l1ll1Il1l1 = Path(l111ll1l1111l1l1Il1l1.__file__).read_text(encoding='utf-8')
        __version__ = re.findall('__version__\\s*?=\\s*?"(.*?)"', lll11ll1ll1l1ll1Il1l1)[0]

        l111l1l1ll1ll11lIl1l1 = [int(l1lllll1ll111ll1Il1l1) for l1lllll1ll111ll1Il1l1 in __version__.split('.')]
        lll1ll1ll1l1111lIl1l1.l1l1ll11l1l111llIl1l1 = tuple(l111l1l1ll1ll11lIl1l1)

    def ll1111l1111lll1lIl1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional["llll1l11l1ll1lllIl1l1"]:
        llllll111111l111Il1l1 = l1ll111l1ll111l1Il1l1(lll11111l111llllIl1l1=lll11111l111llllIl1l1, llllllllll1l1ll1Il1l1=lll1ll1ll1l1111lIl1l1)
        llllll111111l111Il1l1.l1l111l1l11lll11Il1l1()
        return llllll111111l111Il1l1

    def l1l1l11ll111l1l1Il1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: Any) -> None:
        l1l11111l1ll111lIl1l1 = locals().copy()

        l1l11111l1ll111lIl1l1.update({'original': l111ll1l1111l1l1Il1l1.Engine.__init__, 'reloader_code': llll11l11l11ll1lIl1l1, 'engines': lll1ll1ll1l1111lIl1l1.lllll1111lll1111Il1l1})





        l11l1l11lll11lllIl1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    proxy: Any = None,\n                    execution_options: Any = None,\n                    hide_parameters: Any = None,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         proxy,\n                         execution_options,\n                         hide_parameters\n                         )\n                with reloader_code():\n                    engines.append(self2)')
























        l1ll111lll111111Il1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    query_cache_size: Any = 500,\n                    execution_options: Any = None,\n                    hide_parameters: Any = False,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         query_cache_size,\n                         execution_options,\n                         hide_parameters)\n                with reloader_code():\n                    engines.append(self2)\n        ')
























        if (lll1ll1ll1l1111lIl1l1.l1l1ll11l1l111llIl1l1 <= (1, 3, 24, )):
            exec(l11l1l11lll11lllIl1l1, {**globals(), **l1l11111l1ll111lIl1l1}, l1l11111l1ll111lIl1l1)
        else:
            exec(l1ll111lll111111Il1l1, {**globals(), **l1l11111l1ll111lIl1l1}, l1l11111l1ll111lIl1l1)

        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(l111ll1l1111l1l1Il1l1.Engine, '__init__', l1l11111l1ll111lIl1l1['patched'])
