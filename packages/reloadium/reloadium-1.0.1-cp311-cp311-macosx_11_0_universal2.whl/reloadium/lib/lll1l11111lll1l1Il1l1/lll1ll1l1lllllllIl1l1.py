from contextlib import contextmanager
import os
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type

from reloadium.lib.environ import env
from reloadium.corium.l11l1ll1l1l1l11lIl1l1 import llll11l11l11ll1lIl1l1
from reloadium.lib.lll1l11111lll1l1Il1l1.llllllllll1l1ll1Il1l1 import lll1l1ll11l111l1Il1l1, l11ll1lll1lll11lIl1l1
from reloadium.lib.lll1l11111lll1l1Il1l1.ll1l11l11ll1ll11Il1l1 import l11ll1l1l11l11llIl1l1
from reloadium.corium.ll11111l1111ll1lIl1l1 import llllllll1l1l1lllIl1l1, l1llll1l11l111l1Il1l1, l1ll11l111l111llIl1l1, llllll1l11l1l11lIl1l1, l1l1111lll1lllllIl1l1
from reloadium.corium.lllll1lllllll1l1Il1l1 import llll1l11l1ll1lllIl1l1, llll1llll111l11lIl1l1
from reloadium.corium.l1ll1l1ll111lll1Il1l1 import lll11l1ll11llll1Il1l1
from reloadium.corium.l111lll111111lllIl1l1 import lll1l1lllll1l1llIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from django.db import transaction
    from django.db.transaction import Atomic
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass(**l1l1111lll1lllllIl1l1)
class ll1l1lll1ll1l111Il1l1(llllll1l11l1l11lIl1l1):
    ll1ll11l1l1ll1l1Il1l1 = 'Field'

    @classmethod
    def lll111ll111111l1Il1l1(ll1ll11l1111l11lIl1l1, lllll1l11ll1l111Il1l1: lll11l1ll11llll1Il1l1.l1111lll11ll1lllIl1l1, llllllll11lll11lIl1l1: Any, l1l11l111lll1lllIl1l1: l1llll1l11l111l1Il1l1) -> bool:
        from django.db.models.fields import Field

        if ((hasattr(llllllll11lll11lIl1l1, 'field') and isinstance(llllllll11lll11lIl1l1.field, Field))):
            return True

        return False

    def ll1l1ll1111ll1l1Il1l1(lll1ll1ll1l1111lIl1l1, ll1l11l1ll1ll11lIl1l1: l1ll11l111l111llIl1l1) -> bool:
        return True

    @classmethod
    def ll11l1lll1l111llIl1l1(ll1ll11l1111l11lIl1l1) -> int:
        return 200


@dataclass(repr=False)
class l1ll111l1ll111l1Il1l1(lll1l1ll11l111l1Il1l1):
    l1ll1l111l11ll1lIl1l1: "Atomic" = field(init=False)

    l111l11111l1ll11Il1l1: bool = field(init=False, default=False)

    def l1l111l1l11lll11Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().l1l111l1l11lll11Il1l1()
        from django.db import transaction

        lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1 = transaction.atomic()
        lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1.__enter__()

    def lll1l11ll1l11lllIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().lll1l11ll1l11lllIl1l1()
        if (lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1):
            return 

        lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1 = True
        from django.db import transaction

        transaction.set_rollback(True)
        lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1.__exit__(None, None, None)

    def llll1lll1llll111Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().llll1lll1llll111Il1l1()

        if (lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1):
            return 

        lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1 = True
        lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1.__exit__(None, None, None)

    def __repr__(lll1ll1ll1l1111lIl1l1) -> str:
        return 'DbMemento'


@dataclass(repr=False)
class lll1l1lll1111ll1Il1l1(l11ll1lll1lll11lIl1l1):
    l1ll1l111l11ll1lIl1l1: "Atomic" = field(init=False)

    l111l11111l1ll11Il1l1: bool = field(init=False, default=False)

    async def l1l111l1l11lll11Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        await super().l1l111l1l11lll11Il1l1()
        from django.db import transaction
        from asgiref.sync import sync_to_async

        lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1 = transaction.atomic()
        await sync_to_async(lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1.__enter__)()

    async def lll1l11ll1l11lllIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().lll1l11ll1l11lllIl1l1()
        if (lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1):
            return 

        lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1 = True
        from django.db import transaction

        def ll1llll1111l1ll1Il1l1() -> None:
            transaction.set_rollback(True)
            lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1.__exit__(None, None, None)
        await sync_to_async(ll1llll1111l1ll1Il1l1)()

    async def llll1lll1llll111Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().llll1lll1llll111Il1l1()

        if (lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1):
            return 

        lll1ll1ll1l1111lIl1l1.l111l11111l1ll11Il1l1 = True
        await sync_to_async(lll1ll1ll1l1111lIl1l1.l1ll1l111l11ll1lIl1l1.__exit__)(None, None, None)

    def __repr__(lll1ll1ll1l1111lIl1l1) -> str:
        return 'AsyncDbMemento'


@dataclass
class llllllll11l111l1Il1l1(l11ll1l1l11l11llIl1l1):
    ll11ll1l1llll1l1Il1l1 = 'Django'

    llll11l1111lll1lIl1l1: Optional[int] = field(init=False)
    lll1l1ll1l1ll11lIl1l1: Optional[Callable[..., Any]] = field(init=False, default=None)

    def __post_init__(lll1ll1ll1l1111lIl1l1) -> None:
        super().__post_init__()
        lll1ll1ll1l1111lIl1l1.llll11l1111lll1lIl1l1 = None

    def ll11l1lllll111l1Il1l1(lll1ll1ll1l1111lIl1l1) -> List[Type[l1ll11l111l111llIl1l1]]:
        return [ll1l1lll1ll1l111Il1l1]

    def ll1ll11l11l1l1llIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().ll1ll11l11l1l1llIl1l1()
        if ('runserver' in sys.argv):
            sys.argv.append('--noreload')

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, l111ll1l1111l1l1Il1l1: types.ModuleType) -> None:
        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(l111ll1l1111l1l1Il1l1, 'django.core.management.commands.runserver')):
            lll1ll1ll1l1111lIl1l1.ll1ll11lll11l1llIl1l1()
            lll1ll1ll1l1111lIl1l1.ll1ll1l11l1l1l11Il1l1()

    def ll1111l1111lll1lIl1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional["llll1l11l1ll1lllIl1l1"]:
        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        llllll111111l111Il1l1 = l1ll111l1ll111l1Il1l1(lll11111l111llllIl1l1=lll11111l111llllIl1l1, llllllllll1l1ll1Il1l1=lll1ll1ll1l1111lIl1l1)
        llllll111111l111Il1l1.l1l111l1l11lll11Il1l1()
        return llllll111111l111Il1l1

    async def l11ll1l1l1l1lll1Il1l1(lll1ll1ll1l1111lIl1l1, lll11111l111llllIl1l1: str) -> Optional["llll1llll111l11lIl1l1"]:
        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        llllll111111l111Il1l1 = lll1l1lll1111ll1Il1l1(lll11111l111llllIl1l1=lll11111l111llllIl1l1, llllllllll1l1ll1Il1l1=lll1ll1ll1l1111lIl1l1)
        await llllll111111l111Il1l1.l1l111l1l11lll11Il1l1()
        return llllll111111l111Il1l1

    def ll1ll11lll11l1llIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        import django.core.management.commands.runserver

        ll11lllll111l1l1Il1l1 = django.core.management.commands.runserver.Command.handle

        def l1l11l11l11l1ll1Il1l1(*l11111l11l111111Il1l1: Any, **l1l1lllll1llll11Il1l1: Any) -> Any:
            with llll11l11l11ll1lIl1l1():
                lll1lllll1ll1l1lIl1l1 = l1l1lllll1llll11Il1l1.get('addrport')
                if ( not lll1lllll1ll1l1lIl1l1):
                    lll1lllll1ll1l1lIl1l1 = django.core.management.commands.runserver.Command.default_port

                lll1lllll1ll1l1lIl1l1 = lll1lllll1ll1l1lIl1l1.split(':')[ - 1]
                lll1lllll1ll1l1lIl1l1 = int(lll1lllll1ll1l1lIl1l1)
                lll1ll1ll1l1111lIl1l1.llll11l1111lll1lIl1l1 = lll1lllll1ll1l1lIl1l1

            return ll11lllll111l1l1Il1l1(*l11111l11l111111Il1l1, **l1l1lllll1llll11Il1l1)

        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(django.core.management.commands.runserver.Command, 'handle', l1l11l11l11l1ll1Il1l1)

    def ll1ll1l11l1l1l11Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        import django.core.management.commands.runserver

        ll11lllll111l1l1Il1l1 = django.core.management.commands.runserver.Command.get_handler

        def l1l11l11l11l1ll1Il1l1(*l11111l11l111111Il1l1: Any, **l1l1lllll1llll11Il1l1: Any) -> Any:
            with llll11l11l11ll1lIl1l1():
                assert lll1ll1ll1l1111lIl1l1.llll11l1111lll1lIl1l1
                lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1 = lll1ll1ll1l1111lIl1l1.lll1ll1ll111l111Il1l1(lll1ll1ll1l1111lIl1l1.llll11l1111lll1lIl1l1)
                if (env.page_reload_on_start):
                    lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.ll1l111l111l11l1Il1l1(2.0)

            return ll11lllll111l1l1Il1l1(*l11111l11l111111Il1l1, **l1l1lllll1llll11Il1l1)

        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(django.core.management.commands.runserver.Command, 'get_handler', l1l11l11l11l1ll1Il1l1)

    def l11ll11l1ll1l1l1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().l11ll11l1ll1l1l1Il1l1()

        import django.core.handlers.base

        ll11lllll111l1l1Il1l1 = django.core.handlers.base.BaseHandler.get_response

        def l1l11l11l11l1ll1Il1l1(l11l111111l111l1Il1l1: Any, l1111ll11l1lllllIl1l1: Any) -> Any:
            ll11111l111ll11lIl1l1 = ll11lllll111l1l1Il1l1(l11l111111l111l1Il1l1, l1111ll11l1lllllIl1l1)

            if ( not lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1):
                return ll11111l111ll11lIl1l1

            l111llll11111lllIl1l1 = ll11111l111ll11lIl1l1.get('content-type')

            if (( not l111llll11111lllIl1l1 or 'text/html' not in l111llll11111lllIl1l1)):
                return ll11111l111ll11lIl1l1

            lll11ll1ll1l1ll1Il1l1 = ll11111l111ll11lIl1l1.content

            if (isinstance(lll11ll1ll1l1ll1Il1l1, bytes)):
                lll11ll1ll1l1ll1Il1l1 = lll11ll1ll1l1ll1Il1l1.decode('utf-8')

            l111l1ll111lll1lIl1l1 = lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.l11l11ll11lll1llIl1l1(lll11ll1ll1l1ll1Il1l1)

            ll11111l111ll11lIl1l1.content = l111l1ll111lll1lIl1l1.encode('utf-8')
            ll11111l111ll11lIl1l1['content-length'] = str(len(ll11111l111ll11lIl1l1.content)).encode('ascii')
            return ll11111l111ll11lIl1l1

        django.core.handlers.base.BaseHandler.get_response = l1l11l11l11l1ll1Il1l1  # type: ignore

    def l1l111llll1lll1lIl1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path) -> None:
        super().l1l111llll1lll1lIl1l1(l1l1l1lll1llll1lIl1l1)

        from django.apps.registry import Apps

        lll1ll1ll1l1111lIl1l1.lll1l1ll1l1ll11lIl1l1 = Apps.register_model

        def l1l1111l1ll111l1Il1l1(*l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> Any:
            pass

        Apps.register_model = l1l1111l1ll111l1Il1l1

    def l1l11l1l1l1111l1Il1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path, lllll1l11ll11111Il1l1: List[llllllll1l1l1lllIl1l1]) -> None:
        super().l1l11l1l1l1111l1Il1l1(l1l1l1lll1llll1lIl1l1, lllll1l11ll11111Il1l1)

        if ( not lll1ll1ll1l1111lIl1l1.lll1l1ll1l1ll11lIl1l1):
            return 

        from django.apps.registry import Apps

        Apps.register_model = lll1ll1ll1l1111lIl1l1.lll1l1ll1l1ll11lIl1l1
