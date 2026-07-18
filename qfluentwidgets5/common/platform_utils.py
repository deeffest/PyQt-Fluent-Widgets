# coding:utf-8
import sys
import subprocess

IS_LINUX = sys.platform == "linux"

def hasCompositor() -> bool:
    if not IS_LINUX:
        return True
    if not hasattr(hasCompositor, "_cache"):
        try:
            out = subprocess.run(
                ["xprop", "-root", "_NET_WM_CM_S0"],
                capture_output=True, text=True, timeout=1
            )
            hasCompositor._cache = "not found" not in out.stdout
        except Exception:
            hasCompositor._cache = False
    return hasCompositor._cache
