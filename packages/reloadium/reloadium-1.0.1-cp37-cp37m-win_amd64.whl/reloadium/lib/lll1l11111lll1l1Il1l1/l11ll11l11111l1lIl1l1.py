from contextlib import contextmanager
from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type

from reloadium.lib.environ import env
from reloadium.corium.l11l1ll1l1l1l11lIl1l1 import llll11l11l11ll1lIl1l1
from reloadium.lib.lll1l11111lll1l1Il1l1.ll1l11l11ll1ll11Il1l1 import l11ll1l1l11l11llIl1l1
from reloadium.corium.ll11111l1111ll1lIl1l1 import l1llll1l11l111l1Il1l1, l1ll11l111l111llIl1l1, llllll1l11l1l11lIl1l1, l1l1111lll1lllllIl1l1
from reloadium.corium.l1ll1l1ll111lll1Il1l1 import lll11l1ll11llll1Il1l1
from reloadium.corium.l111lll111111lllIl1l1 import lll1l1lllll1l1llIl1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass
else:
    from reloadium.vendored.dataclasses import dataclass


__RELOADIUM__ = True


@dataclass(**l1l1111lll1lllllIl1l1)
class l111ll1l11l111llIl1l1(llllll1l11l1l11lIl1l1):
    ll1ll11l1l1ll1l1Il1l1 = 'FlaskApp'

    @classmethod
    def lll111ll111111l1Il1l1(ll1ll11l1111l11lIl1l1, lllll1l11ll1l111Il1l1: lll11l1ll11llll1Il1l1.l1111lll11ll1lllIl1l1, llllllll11lll11lIl1l1: Any, l1l11l111lll1lllIl1l1: l1llll1l11l111l1Il1l1) -> bool:
        import flask

        if (isinstance(llllllll11lll11lIl1l1, flask.Flask)):
            return True

        return False

    def l1l11l11lll111l1Il1l1(lll1ll1ll1l1111lIl1l1) -> bool:
        return True

    @classmethod
    def ll11l1lll1l111llIl1l1(ll1ll11l1111l11lIl1l1) -> int:
        return (super().ll11l1lll1l111llIl1l1() + 10)


@dataclass(**l1l1111lll1lllllIl1l1)
class l1l11l1l1ll11ll1Il1l1(llllll1l11l1l11lIl1l1):
    ll1ll11l1l1ll1l1Il1l1 = 'Request'

    @classmethod
    def lll111ll111111l1Il1l1(ll1ll11l1111l11lIl1l1, lllll1l11ll1l111Il1l1: lll11l1ll11llll1Il1l1.l1111lll11ll1lllIl1l1, llllllll11lll11lIl1l1: Any, l1l11l111lll1lllIl1l1: l1llll1l11l111l1Il1l1) -> bool:
        if (repr(llllllll11lll11lIl1l1) == '<LocalProxy unbound>'):
            return True

        return False

    def l1l11l11lll111l1Il1l1(lll1ll1ll1l1111lIl1l1) -> bool:
        return True

    @classmethod
    def ll11l1lll1l111llIl1l1(ll1ll11l1111l11lIl1l1) -> int:

        return int(10000000000.0)


@dataclass
class l1111111lll1l11lIl1l1(l11ll1l1l11l11llIl1l1):
    ll11ll1l1llll1l1Il1l1 = 'Flask'

    @contextmanager
    def ll11ll1ll11lll11Il1l1(lll1ll1ll1l1111lIl1l1) -> Generator[None, None, None]:




        from flask import Flask as FlaskLib 

        def l111l1l11l111111Il1l1(*l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> Any:
            def ll111ll11ll1llllIl1l1(lll11l11ll1llll1Il1l1: Any) -> Any:
                return lll11l11ll1llll1Il1l1

            return ll111ll11ll1llllIl1l1

        l1ll1111l11l11llIl1l1 = FlaskLib.route
        FlaskLib.route = l111l1l11l111111Il1l1  # type: ignore

        try:
            yield 
        finally:
            FlaskLib.route = l1ll1111l11l11llIl1l1  # type: ignore

    def ll11l1lllll111l1Il1l1(lll1ll1ll1l1111lIl1l1) -> List[Type[l1ll11l111l111llIl1l1]]:
        return [l111ll1l11l111llIl1l1, l1l11l1l1ll11ll1Il1l1]

    def llll1ll1ll1lllllIl1l1(lll1ll1ll1l1111lIl1l1, lll111111lllll11Il1l1: types.ModuleType) -> None:
        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(lll111111lllll11Il1l1, 'flask.app')):
            lll1ll1ll1l1111lIl1l1.ll111l1lll1l1ll1Il1l1()
            lll1ll1ll1l1111lIl1l1.l1lllll111l1lll1Il1l1()
            lll1ll1ll1l1111lIl1l1.l1ll1ll111lllll1Il1l1()

        if (lll1ll1ll1l1111lIl1l1.ll11l11ll11l111lIl1l1(lll111111lllll11Il1l1, 'flask.cli')):
            lll1ll1ll1l1111lIl1l1.l1ll111111l1l1l1Il1l1()

    def ll111l1lll1l1ll1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        try:
            import werkzeug.serving
            import flask.cli
        except ImportError:
            return 

        ll11lllll111l1l1Il1l1 = werkzeug.serving.run_simple

        def l1l11l11l11l1ll1Il1l1(*l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> Any:
            with llll11l11l11ll1lIl1l1():
                lll1lllll1ll1l1lIl1l1 = ll1lllll1l1ll11lIl1l1.get('port')
                if ( not lll1lllll1ll1l1lIl1l1):
                    lll1lllll1ll1l1lIl1l1 = l11111l11l111111Il1l1[1]

                lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1 = lll1ll1ll1l1111lIl1l1.lll1ll1ll111l111Il1l1(lll1lllll1ll1l1lIl1l1)
                if (env.page_reload_on_start):
                    lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.ll1l111l111l11l1Il1l1(1.0)
            ll11lllll111l1l1Il1l1(*l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1)

        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(werkzeug.serving, 'run_simple', l1l11l11l11l1ll1Il1l1)
        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(flask.cli, 'run_simple', l1l11l11l11l1ll1Il1l1)

    def l1ll1ll111lllll1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        try:
            import flask
        except ImportError:
            return 

        ll11lllll111l1l1Il1l1 = flask.app.Flask.__init__

        def l1l11l11l11l1ll1Il1l1(lll11ll11l111lllIl1l1: Any, *l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> Any:
            ll11lllll111l1l1Il1l1(lll11ll11l111lllIl1l1, *l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1)
            with llll11l11l11ll1lIl1l1():
                lll11ll11l111lllIl1l1.config['TEMPLATES_AUTO_RELOAD'] = True

        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(flask.app.Flask, '__init__', l1l11l11l11l1ll1Il1l1)

    def l1lllll111l1lll1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        try:
            import waitress  # type: ignore
        except ImportError:
            return 

        ll11lllll111l1l1Il1l1 = waitress.serve


        def l1l11l11l11l1ll1Il1l1(*l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> Any:
            with llll11l11l11ll1lIl1l1():
                lll1lllll1ll1l1lIl1l1 = ll1lllll1l1ll11lIl1l1.get('port')
                if ( not lll1lllll1ll1l1lIl1l1):
                    lll1lllll1ll1l1lIl1l1 = int(l11111l11l111111Il1l1[1])

                lll1lllll1ll1l1lIl1l1 = int(lll1lllll1ll1l1lIl1l1)

                lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1 = lll1ll1ll1l1111lIl1l1.lll1ll1ll111l111Il1l1(lll1lllll1ll1l1lIl1l1)
                if (env.page_reload_on_start):
                    lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.ll1l111l111l11l1Il1l1(1.0)

            ll11lllll111l1l1Il1l1(*l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1)

        lll1l1lllll1l1llIl1l1.l1l1l1ll1l1l111lIl1l1(waitress, 'serve', l1l11l11l11l1ll1Il1l1)

    def l1ll111111l1l1l1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        try:
            from flask import cli
        except ImportError:
            return 

        ll111lll11ll1111Il1l1 = Path(cli.__file__).read_text(encoding='utf-8')
        ll111lll11ll1111Il1l1 = ll111lll11ll1111Il1l1.replace('.tb_next', '.tb_next.tb_next')

        exec(ll111lll11ll1111Il1l1, cli.__dict__)

    def l11ll11l1ll1l1l1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        super().l11ll11l1ll1l1l1Il1l1()
        import flask.app

        ll11lllll111l1l1Il1l1 = flask.app.Flask.dispatch_request

        def l1l11l11l11l1ll1Il1l1(*l11111l11l111111Il1l1: Any, **ll1lllll1l1ll11lIl1l1: Any) -> Any:
            ll11111l111ll11lIl1l1 = ll11lllll111l1l1Il1l1(*l11111l11l111111Il1l1, **ll1lllll1l1ll11lIl1l1)

            if ( not lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1):
                return ll11111l111ll11lIl1l1

            if (isinstance(ll11111l111ll11lIl1l1, str)):
                llllll111111l111Il1l1 = lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.l11l11ll11lll1llIl1l1(ll11111l111ll11lIl1l1)
                return llllll111111l111Il1l1
            elif ((isinstance(ll11111l111ll11lIl1l1, flask.app.Response) and 'text/html' in ll11111l111ll11lIl1l1.content_type)):
                ll11111l111ll11lIl1l1.data = lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.l11l11ll11lll1llIl1l1(ll11111l111ll11lIl1l1.data.decode('utf-8')).encode('utf-8')
                return ll11111l111ll11lIl1l1
            else:
                return ll11111l111ll11lIl1l1

        flask.app.Flask.dispatch_request = l1l11l11l11l1ll1Il1l1  # type: ignore
