#!/usr/bin/env python3

import os
from unittest import TestLoader, TextTestRunner

def get_rel_path(relpath):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), relpath))

if __name__ == "__main__":
    test_suite = TestLoader().discover(get_rel_path("tests"))
    TextTestRunner().run(test_suite)
