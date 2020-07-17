Bright Interactive Version Control
==================================

**Version control utilities for Bright Interactive projects.**

**Author:** Francis Devereux, [Bright Interactive][1].


Publishing releases to PyPI
===========================

Only Bright Interactive employees can publish a release. Ensure you have a .pypirc file in your home directory configured to publish to the bright PyPI account (real password has been redacted).

```
[pypirc]
servers = pypi

[server-login]
username:bright
password:******
```

To publish a new version of this package to PyPI, set the `__version__`
string in `bright_vc/__init__.py`, then run:

    # Run the tests against multiple environments
    tox
    # Publish to PyPI
    ./setup.py publish
    # Tag (change 1.0.0 to the version you are publishing!)
    git tag -a v1.0.0 -m 'Version 1.0.0'
    git push --tags


Running the tests
=================

To run the tests against the current environment:

    python -m bright_vc.tests

To run the tests against multiple environments, install `tox` using
`pip install tox`, make sure you're not currently in a virtual environment,
then simply run `tox`:

    tox

Changelog
=========
1.1.1
-----
* Support Python 3

1.1.0
-----

* Added support for alpha, beta and pre-release versions (e.g. 1.0.0a4)

1.0.0
-----

* Initial release

License
=======

Copyright (c) Bright Interactive Limited.

All rights reserved.

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or 
other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

[1]: http://www.bright-interactive.com/
