""" Tests hash-checking functions. 
Run with:
    nosetests test_data.py
"""

from __future__ import absolute_import, division, print_function

import tempfile
import sys
import os

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import get_hashes
import get_all_hashes


def test_check_hashes():
    with tempfile.NamedTemporaryFile() as temp:
        temp.write(b'Some data')
        temp.flush()
        fname = temp.name
        d = {fname: "5b82f8bf4df2bfb0e66ccaa7306fd024"}
        assert get_hashes.check_hashes(d)
        d = {fname: "4b82f8bf4df2bfb0e66ccaa7306fd024"}
        assert not get_hashes.check_hashes(d)
