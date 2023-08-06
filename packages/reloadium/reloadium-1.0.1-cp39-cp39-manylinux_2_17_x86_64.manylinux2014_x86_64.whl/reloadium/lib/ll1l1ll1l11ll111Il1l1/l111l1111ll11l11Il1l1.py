import sys

__RELOADIUM__ = True


def ll1111l11ll1lll1Il1l1(lll11ll11l111lllIl1l1, ll1l111111lll1llIl1l1):
    from pathlib import Path
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    import io
    import os

    def llll11l1l11lllllIl1l1(*llll1111ll1l11llIl1l1):

        for llll111l1111lll1Il1l1 in llll1111ll1l11llIl1l1:
            os.close(llll111l1111lll1Il1l1)

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
    else:
        from multiprocessing import semaphore_tracker as tracker 

    l1ll1l1ll1l1l111Il1l1 = tracker.getfd()
    lll11ll11l111lllIl1l1._fds.append(l1ll1l1ll1l1l111Il1l1)
    l111l1lll1ll1l1lIl1l1 = spawn.get_preparation_data(ll1l111111lll1llIl1l1._name)
    llll11ll1ll1l1llIl1l1 = io.BytesIO()
    set_spawning_popen(lll11ll11l111lllIl1l1)

    try:
        reduction.dump(l111l1lll1ll1l1lIl1l1, llll11ll1ll1l1llIl1l1)
        reduction.dump(ll1l111111lll1llIl1l1, llll11ll1ll1l1llIl1l1)
    finally:
        set_spawning_popen(None)

    ll1lll11l1l1l111Il1l1l1ll1l11ll1l11l1Il1l1l1111l1l1l111l1lIl1l1ll1l1l1lll1lll11Il1l1 = None
    try:
        (ll1lll11l1l1l111Il1l1, l1ll1l11ll1l11l1Il1l1, ) = os.pipe()
        (l1111l1l1l111l1lIl1l1, ll1l1l1lll1lll11Il1l1, ) = os.pipe()
        ll1l1ll1l1l111l1Il1l1 = spawn.get_command_line(tracker_fd=l1ll1l1ll1l1l111Il1l1, pipe_handle=l1111l1l1l111l1lIl1l1)


        l1l1l11l1l11ll11Il1l1 = str(Path(l111l1lll1ll1l1lIl1l1['sys_argv'][0]).absolute())
        ll1l1ll1l1l111l1Il1l1 = [ll1l1ll1l1l111l1Il1l1[0], '-B', '-m', 'reloadium', 'spawn_process', str(l1ll1l1ll1l1l111Il1l1), 
str(l1111l1l1l111l1lIl1l1), l1l1l11l1l11ll11Il1l1]
        lll11ll11l111lllIl1l1._fds.extend([l1111l1l1l111l1lIl1l1, l1ll1l11ll1l11l1Il1l1])
        lll11ll11l111lllIl1l1.pid = util.spawnv_passfds(spawn.get_executable(), 
ll1l1ll1l1l111l1Il1l1, lll11ll11l111lllIl1l1._fds)
        lll11ll11l111lllIl1l1.sentinel = ll1lll11l1l1l111Il1l1
        with open(ll1l1l1lll1lll11Il1l1, 'wb', closefd=False) as lll11l11ll1llll1Il1l1:
            lll11l11ll1llll1Il1l1.write(llll11ll1ll1l1llIl1l1.getbuffer())
    finally:
        l1l1lllll111l1llIl1l1 = []
        for llll111l1111lll1Il1l1 in (ll1lll11l1l1l111Il1l1, ll1l1l1lll1lll11Il1l1, ):
            if (llll111l1111lll1Il1l1 is not None):
                l1l1lllll111l1llIl1l1.append(llll111l1111lll1Il1l1)
        lll11ll11l111lllIl1l1.finalizer = util.Finalize(lll11ll11l111lllIl1l1, llll11l1l11lllllIl1l1, l1l1lllll111l1llIl1l1)

        for llll111l1111lll1Il1l1 in (l1111l1l1l111l1lIl1l1, l1ll1l11ll1l11l1Il1l1, ):
            if (llll111l1111lll1Il1l1 is not None):
                os.close(llll111l1111lll1Il1l1)


def __init__(lll11ll11l111lllIl1l1, ll1l111111lll1llIl1l1):
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    from multiprocessing.popen_spawn_win32 import TERMINATE, WINEXE, WINSERVICE, WINENV, _path_eq
    from pathlib import Path
    import os
    import msvcrt
    import sys
    import _winapi

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
        from multiprocessing.popen_spawn_win32 import _close_handles
    else:
        from multiprocessing import semaphore_tracker as tracker 
        _close_handles = _winapi.CloseHandle

    l111l1lll1ll1l1lIl1l1 = spawn.get_preparation_data(ll1l111111lll1llIl1l1._name)







    (l1ll1ll11ll11lllIl1l1, l1l11ll1111l11l1Il1l1, ) = _winapi.CreatePipe(None, 0)
    l11ll1l1l11111l1Il1l1 = msvcrt.open_osfhandle(l1l11ll1111l11l1Il1l1, 0)
    l11l1l11l1lll11lIl1l1 = spawn.get_executable()
    l1l1l11l1l11ll11Il1l1 = str(Path(l111l1lll1ll1l1lIl1l1['sys_argv'][0]).absolute())
    ll1l1ll1l1l111l1Il1l1 = ' '.join([l11l1l11l1lll11lIl1l1, '-B', '-m', 'reloadium', 'spawn_process', str(os.getpid()), 
str(l1ll1ll11ll11lllIl1l1), l1l1l11l1l11ll11Il1l1])



    if ((WINENV and _path_eq(l11l1l11l1lll11lIl1l1, sys.executable))):
        l11l1l11l1lll11lIl1l1 = sys._base_executable
        l111ll1ll11l11llIl1l1 = os.environ.copy()
        l111ll1ll11l11llIl1l1['__PYVENV_LAUNCHER__'] = sys.executable
    else:
        l111ll1ll11l11llIl1l1 = None

    with open(l11ll1l1l11111l1Il1l1, 'wb', closefd=True) as l111l1l1l11l111lIl1l1:

        try:
            (l11l1l1llll1lll1Il1l1, l1l111l11l111lllIl1l1, lll11llll1lllll1Il1l1, ll1l11111ll1ll1lIl1l1, ) = _winapi.CreateProcess(l11l1l11l1lll11lIl1l1, ll1l1ll1l1l111l1Il1l1, None, None, False, 0, l111ll1ll11l11llIl1l1, None, None)


            _winapi.CloseHandle(l1l111l11l111lllIl1l1)
        except :
            _winapi.CloseHandle(l1ll1ll11ll11lllIl1l1)
            raise 


        lll11ll11l111lllIl1l1.pid = lll11llll1lllll1Il1l1
        lll11ll11l111lllIl1l1.returncode = None
        lll11ll11l111lllIl1l1._handle = l11l1l1llll1lll1Il1l1
        lll11ll11l111lllIl1l1.sentinel = int(l11l1l1llll1lll1Il1l1)
        if (sys.version_info > (3, 8, )):
            lll11ll11l111lllIl1l1.finalizer = util.Finalize(lll11ll11l111lllIl1l1, _close_handles, (lll11ll11l111lllIl1l1.sentinel, int(l1ll1ll11ll11lllIl1l1), 
))
        else:
            lll11ll11l111lllIl1l1.finalizer = util.Finalize(lll11ll11l111lllIl1l1, _close_handles, (lll11ll11l111lllIl1l1.sentinel, ))



        set_spawning_popen(lll11ll11l111lllIl1l1)
        try:
            reduction.dump(l111l1lll1ll1l1lIl1l1, l111l1l1l11l111lIl1l1)
            reduction.dump(ll1l111111lll1llIl1l1, l111l1l1l11l111lIl1l1)
        finally:
            set_spawning_popen(None)
