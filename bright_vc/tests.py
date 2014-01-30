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
        bright_vc.check_tag("v10.20.30a1")
        bright_vc.check_tag("v10.20.30a10")
        bright_vc.check_tag("v10.20.30b100")
        bright_vc.check_tag("v1.0.1pr5")
        bright_vc.check_tag("v0.1.0pr5000")

    def test_invalid_tag_not_accepted(self):
        self.assertRaises(Exception, bright_vc.check_tag, "v10.20.30-a")
        self.assertRaises(Exception, bright_vc.check_tag, "v10.0.b")
        self.assertRaises(Exception, bright_vc.check_tag, "v10.c.30")
        self.assertRaises(Exception, bright_vc.check_tag, "vd.1.30")
        self.assertRaises(Exception, bright_vc.check_tag, "v1.1.1p")
        self.assertRaises(Exception, bright_vc.check_tag, "v1.1.1r")
        self.assertRaises(Exception, bright_vc.check_tag, "v1.1.1a")
        self.assertRaises(Exception, bright_vc.check_tag, "v1.1.1ba")


if __name__ == '__main__':
    unittest.main()
