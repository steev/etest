# Copyright (C) 2014 by Alex Brandt <alunduil@alunduil.com>
#
# etest is freely distributable under the terms of an MIT-style license.
# See COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
import unittest

from test_etest.test_fixtures.test_helpers import BASH_TEXTS

from etest.helpers import bash_to_dict, ParseError

logger = logging.getLogger(__name__)


class TestBashToDict(unittest.TestCase):
    def setUp(self):
        self.texts = BASH_TEXTS

    def test_correct(self):
        '''helpers.bash_to_dict()—correct parse'''

        for text in self.texts['CORRECT']:
            self.assertEqual(text['dictionary'], bash_to_dict(text['bash']))

    def test_incorrect(self):
        '''helpers.bash_to_dict()—incorrect parse'''

        for text in self.texts['INCORRECT']:
            self.assertRaises(ParseError, bash_to_dict, test['bash'])
