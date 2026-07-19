# coding:utf-8
import os
import sys

IS_LINUX = sys.platform == "linux"

if IS_LINUX:
    from Xlib import display, X


def hasCompositor() -> bool:
    if not IS_LINUX:
        return True

    if not hasattr(hasCompositor, "_cache"):
        hasCompositor._cache = _checkCompositor()

    return hasCompositor._cache


def _checkCompositor() -> bool:
    if os.environ.get("WAYLAND_DISPLAY") or not os.environ.get("DISPLAY"):
        return True

    d = None
    try:
        d = display.Display()
        screen_num = d.get_default_screen()
        atom = d.intern_atom(f"_NET_WM_CM_S{screen_num}")
        owner = d.get_selection_owner(atom)
        return owner != X.NONE
    except Exception:
        return False
    finally:
        if d is not None:
            d.close()
