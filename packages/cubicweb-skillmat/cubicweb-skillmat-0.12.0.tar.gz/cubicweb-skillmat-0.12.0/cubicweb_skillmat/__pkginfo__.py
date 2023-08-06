# pylint: disable-msg=W0622
"""cubicweb-skillmat application packaging information"""

modname = 'skillmat'
distname = 'cubicweb-skillmat'

numversion = (0, 12, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
description = 'skill matrix component for the CubicWeb framework'
author = 'Logilab'
author_email = 'contact@logilab.fr'
web = 'http://www.cubicweb.org/project/%s' % distname

__depends__ = {'cubicweb': ">=3.38.0,<3.39.0",
               'cubicweb-folder': ">=2.1.0,<2.2.0",
               'cubicweb-comment': ">=2.0.0,<2.1.0",
               "pandas": ">=1.5.0,<1.6.0"}

classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    ]
