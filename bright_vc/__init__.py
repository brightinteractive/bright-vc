# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

"""
Bright Interactive Version Control

Based on Semantic Versioning (http://semver.org/) but simpler - only "normal"
(X.Y.Z) versions are allowed, not pre-release (1.0.0-alpha.1) or build
(1.0.0+build.1) versions.
"""

import re


# Version number of the bright_vc package 
__version__ = '1.1.1'


# Constants
VERSION_PATTERN = """[0-9]+\.[0-9]+\.[0-9]+((a|b|pr)[0-9]+)?$"""
VERSION_RE = re.compile(VERSION_PATTERN)
TAG_RE = re.compile("""v""" + VERSION_PATTERN)


def check_tag(tag_name):
    """
    Check that tag_name is a valid tag name and raise an exception if not.
    """
    if not TAG_RE.match(tag_name):
        raise Exception("%s is not a valid tag name" % tag_name)
