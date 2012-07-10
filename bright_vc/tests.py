#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

import os.path
import sys
# put parent dir on sys.path so that "import bright_vc" will work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import bright_vc
import unittest


class TagCheckTests(unittest.TestCase):
    def test_valid_tag_accepted(self):
        bright_vc.check_tag("v10.20.30")

    def test_invalid_tag_not_accepted(self):
        with self.assertRaises(Exception):
            bright_vc.check_tag("v10.20.30b")

if __name__ == '__main__':
    unittest.main()
