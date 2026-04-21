# coding: utf-8
import sys


_safeMode: bool = sys.platform == "linux"


def isSafeMode() -> bool:
    return _safeMode


def setSafeMode(enabled: bool):
    global _safeMode
    _safeMode = enabled
