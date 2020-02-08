#!/usr/bin/env python3

""" Helper module to be able to import modules in tests. """

import os
import sys

def rootpath(relpath):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relpath))

for p in ("../", "../stubs",):
    sys.path.insert(1, rootpath(p))
