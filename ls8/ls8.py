#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

if len(sys.argv) != 2:
    print("usage: ls8.py progname")
    sys.exit(1)

cpu = CPU()

cpu.load()
cpu.run()