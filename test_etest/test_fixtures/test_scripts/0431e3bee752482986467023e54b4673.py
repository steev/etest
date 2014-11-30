# Copyright (C) 2014 by Alex Brandt <alunduil@alunduil.com>
#
# etest is freely distributable under the terms of an MIT-style license.
# See COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_etest.test_fixtures.test_scripts import SCRIPTS

_ = '''
# comment
'''[1:-1]

_ = {
    'uuid': '0431e3bee752482986467023e54b4673',

    'description': 'single comment',

    'text': _,

    'symbols': {},
}

SCRIPTS.setdefault('all', []).append(_)
SCRIPTS.setdefault('bash', []).append(_)
