#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

import os
import platform

s = "/"
if platform.system() == "Windows":
    s = "\\"

os.chdir(s.join(os.path.abspath(__file__).split(s)[:-1]))

from appfolder import app
from config import APP_ADDRESS, APP_PORT, DEBUG

if __name__ == "__main__":

    app.run(host=APP_ADDRESS, port=APP_PORT, debug=DEBUG)

