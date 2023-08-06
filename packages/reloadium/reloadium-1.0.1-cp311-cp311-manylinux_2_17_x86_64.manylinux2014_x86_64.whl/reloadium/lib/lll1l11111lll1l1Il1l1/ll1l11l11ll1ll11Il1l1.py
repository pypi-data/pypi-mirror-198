import logging
from pathlib import Path
from threading import Thread
import time
from typing import TYPE_CHECKING, List, Optional

from reloadium.corium import l11111111l11l111Il1l1, l111lll111111lllIl1l1
from reloadium.lib.lll1l11111lll1l1Il1l1.llllllllll1l1ll1Il1l1 import l11ll1ll11lllll1Il1l1
from reloadium.corium.lll111l11lllll11Il1l1 import l111l11111l11111Il1l1
from reloadium.corium.l1l11lll1llll111Il1l1 import l1111l1l1l11lll1Il1l1
from reloadium.corium.ll11111l1111ll1lIl1l1 import llllllll1l1l1lllIl1l1
from reloadium.corium.lllll1l1l11l1111Il1l1 import lllll1l1l11l1111Il1l1

if (TYPE_CHECKING):
    from dataclasses import dataclass, field

    from reloadium.vendored.websocket_server import WebsocketServer
else:
    from reloadium.vendored.dataclasses import dataclass, field


__RELOADIUM__ = True

__all__ = ['l111l1111l1l1111Il1l1']



llll111llll11l1lIl1l1 = '\n<!--{info}-->\n<script type="text/javascript">\n   // <![CDATA[  <-- For SVG support\n     function refreshCSS() {\n        var sheets = [].slice.call(document.getElementsByTagName("link"));\n        var head = document.getElementsByTagName("head")[0];\n        for (var i = 0; i < sheets.length; ++i) {\n           var elem = sheets[i];\n           var parent = elem.parentElement || head;\n           parent.removeChild(elem);\n           var rel = elem.rel;\n           if (elem.href && typeof rel != "string" || rel.length === 0 || rel.toLowerCase() === "stylesheet") {\n              var url = elem.href.replace(/(&|\\?)_cacheOverride=\\d+/, \'\');\n              elem.href = url + (url.indexOf(\'?\') >= 0 ? \'&\' : \'?\') + \'_cacheOverride=\' + (new Date().valueOf());\n           }\n           parent.appendChild(elem);\n        }\n     }\n     let protocol = window.location.protocol === \'http:\' ? \'ws://\' : \'wss://\';\n     let address = protocol + "{address}:{port}";\n     let socket = undefined;\n     let lost_connection = false;\n\n     function connect() {\n        socket = new WebSocket(address);\n         socket.onmessage = function (msg) {\n            if (msg.data === \'reload\') window.location.href = window.location.href;\n            else if (msg.data === \'refreshcss\') refreshCSS();\n         };\n     }\n\n     function checkConnection() {\n        if ( socket.readyState === socket.CLOSED ) {\n            lost_connection = true;\n            connect();\n        }\n     }\n\n     connect();\n     setInterval(checkConnection, 500)\n\n   // ]]>\n</script>\n'














































@dataclass
class l111l1111l1l1111Il1l1:
    l1lll1ll111ll1llIl1l1: str
    lll1lllll1ll1l1lIl1l1: int
    lll1l111l1l1l111Il1l1: l1111l1l1l11lll1Il1l1

    l1l1lll1l1l1ll11Il1l1: Optional["WebsocketServer"] = field(init=False, default=None)
    ll1llll11ll11l1lIl1l1: str = field(init=False, default='')

    lll11l1llll111llIl1l1 = 'Reloadium page reloader'

    def l1111llll1llll1lIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        from reloadium.vendored.websocket_server import WebsocketServer

        lll1ll1ll1l1111lIl1l1.lll1l111l1l1l111Il1l1.lll11l1llll111llIl1l1(''.join(['Starting reload websocket server on port ', '{:{}}'.format(lll1ll1ll1l1111lIl1l1.lll1lllll1ll1l1lIl1l1, '')]))

        lll1ll1ll1l1111lIl1l1.l1l1lll1l1l1ll11Il1l1 = WebsocketServer(host=lll1ll1ll1l1111lIl1l1.l1lll1ll111ll1llIl1l1, port=lll1ll1ll1l1111lIl1l1.lll1lllll1ll1l1lIl1l1, loglevel=logging.CRITICAL)
        lll1ll1ll1l1111lIl1l1.l1l1lll1l1l1ll11Il1l1.run_forever(threaded=True)

        lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1 = llll111llll11l1lIl1l1

        lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1 = lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1.replace('{info}', str(lll1ll1ll1l1111lIl1l1.lll11l1llll111llIl1l1))
        lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1 = lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1.replace('{port}', str(lll1ll1ll1l1111lIl1l1.lll1lllll1ll1l1lIl1l1))
        lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1 = lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1.replace('{address}', lll1ll1ll1l1111lIl1l1.l1lll1ll111ll1llIl1l1)

    def l11l11ll11lll1llIl1l1(lll1ll1ll1l1111lIl1l1, l1ll1ll11111lll1Il1l1: str) -> str:
        l111lllll1l111llIl1l1 = l1ll1ll11111lll1Il1l1.find('<head>')
        if (l111lllll1l111llIl1l1 ==  - 1):
            l111lllll1l111llIl1l1 = 0
        llllll111111l111Il1l1 = ((l1ll1ll11111lll1Il1l1[:l111lllll1l111llIl1l1] + lll1ll1ll1l1111lIl1l1.ll1llll11ll11l1lIl1l1) + l1ll1ll11111lll1Il1l1[l111lllll1l111llIl1l1:])
        return llllll111111l111Il1l1

    def l111111l11ll1ll1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        try:
            lll1ll1ll1l1111lIl1l1.l1111llll1llll1lIl1l1()
        except Exception as l1ll1l11llll1111Il1l1:
            l11111111l11l111Il1l1.lllll1l111l1lll1Il1l1(l1ll1l11llll1111Il1l1)
            lll1ll1ll1l1111lIl1l1.lll1l111l1l1l111Il1l1.l11llll11l1l1ll1Il1l1('Could not start server')

    def l11111l11111llllIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        if ( not lll1ll1ll1l1111lIl1l1.l1l1lll1l1l1ll11Il1l1):
            return 

        lll1ll1ll1l1111lIl1l1.lll1l111l1l1l111Il1l1.lll11l1llll111llIl1l1('Reloading page')
        lll1ll1ll1l1111lIl1l1.l1l1lll1l1l1ll11Il1l1.send_message_to_all('reload')
        lllll1l1l11l1111Il1l1.l11ll111l1l1l11lIl1l1()

    def ll1l111l111l11l1Il1l1(lll1ll1ll1l1111lIl1l1, l1lll1l1l1ll11llIl1l1: float) -> None:
        def lll1lll1llll1l1lIl1l1() -> None:
            time.sleep(l1lll1l1l1ll11llIl1l1)
            lll1ll1ll1l1111lIl1l1.l11111l11111llllIl1l1()

        Thread(target=lll1lll1llll1l1lIl1l1, daemon=True, name=l111lll111111lllIl1l1.l111l111lll11l11Il1l1.l11111ll1l11llllIl1l1('page-reloader')).start()


@dataclass
class l11ll1l1l11l11llIl1l1(l11ll1ll11lllll1Il1l1):
    llll111llll11l1lIl1l1: Optional[l111l1111l1l1111Il1l1] = field(init=False, default=None)

    l1ll1ll1l11l1lllIl1l1 = '127.0.0.1'
    l11l11111l1lllllIl1l1 = 4512

    def ll1ll11l11l1l1llIl1l1(lll1ll1ll1l1111lIl1l1) -> None:
        l111l11111l11111Il1l1.l11llll1lll1ll11Il1l1.l1111ll1l11l1ll1Il1l1.ll1l11l111l1l111Il1l1('html')

    def l1l11l1l1l1111l1Il1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path, lllll1l11ll11111Il1l1: List[llllllll1l1l1lllIl1l1]) -> None:
        if ( not lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1):
            return 

        from reloadium.corium.ll1ll1llll11111lIl1l1.ll1lll1ll1llll11Il1l1 import lll11ll1llll1ll1Il1l1

        if ( not any((isinstance(ll1l111l1l1l1111Il1l1, lll11ll1llll1ll1Il1l1) for ll1l111l1l1l1111Il1l1 in lllll1l11ll11111Il1l1))):
            if (lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1):
                lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.l11111l11111llllIl1l1()

    def ll1l1l1lll11llllIl1l1(lll1ll1ll1l1111lIl1l1, l1l1l1lll1llll1lIl1l1: Path) -> None:
        if ( not lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1):
            return 
        lll1ll1ll1l1111lIl1l1.llll111llll11l1lIl1l1.l11111l11111llllIl1l1()

    def lll1ll1ll111l111Il1l1(lll1ll1ll1l1111lIl1l1, lll1lllll1ll1l1lIl1l1: int) -> l111l1111l1l1111Il1l1:
        while True:
            lll1111l1111ll11Il1l1 = (lll1lllll1ll1l1lIl1l1 + lll1ll1ll1l1111lIl1l1.l11l11111l1lllllIl1l1)
            try:
                llllll111111l111Il1l1 = l111l1111l1l1111Il1l1(l1lll1ll111ll1llIl1l1=lll1ll1ll1l1111lIl1l1.l1ll1ll1l11l1lllIl1l1, lll1lllll1ll1l1lIl1l1=lll1111l1111ll11Il1l1, lll1l111l1l1l111Il1l1=lll1ll1ll1l1111lIl1l1.l11lll11111l1111Il1l1)
                llllll111111l111Il1l1.l111111l11ll1ll1Il1l1()
                lll1ll1ll1l1111lIl1l1.l11ll11l1ll1l1l1Il1l1()
                break
            except OSError:
                lll1ll1ll1l1111lIl1l1.l11lll11111l1111Il1l1.lll11l1llll111llIl1l1(''.join(["Couldn't create page reloader on ", '{:{}}'.format(lll1111l1111ll11Il1l1, ''), ' port']))
                lll1ll1ll1l1111lIl1l1.l11l11111l1lllllIl1l1 += 1

        return llllll111111l111Il1l1

    def l11ll11l1ll1l1l1Il1l1(lll1ll1ll1l1111lIl1l1) -> None:
        lll1ll1ll1l1111lIl1l1.l11lll11111l1111Il1l1.lll11l1llll111llIl1l1('Injecting page reloader')
