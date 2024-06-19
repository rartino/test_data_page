#!/usr/bin/env python3

import os, shutil, sys

from httk.httkweb import publish

if not os.path.exists("public"):
    os.mkdir("public")

for filename in os.listdir("public"):
    if not filename.startswith("."):
        f = os.path.join("public",filename)
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.unlink(f)

publish("src","public",'http://127.0.0.1/')
