#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

import shutil

WorkDir = "."

def install():
    pisitools.insinto("/opt/microsoft/powershell/7", "*")
    pisitools.dosym("/opt/microsoft/powershell/7/pwsh", "/usr/bin/pwsh")
