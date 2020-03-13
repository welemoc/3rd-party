#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

import shutil

WorkDir = "."

def install():
    pisitools.insinto("/opt/dotnet", "*")
    pisitools.dosym("/opt/dotnet/dotnet", "/usr/bin/dotnet")
