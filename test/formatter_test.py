# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson

import unittest

from qingwen import formatter


class TestFormatter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual('', formatter.format_output_line({}))

    def test_single(self):
        res = {"hanzi": "H", "pinyin": "P", "defs": ['D1']}
        self.assertEqual('H\tD1\tP', formatter.format_output_line(res))

    def test_multi(self):
        res = {"hanzi": "H", "pinyin": "P", "defs": ['D1', 'D2']}
        self.assertEqual('H\tD1 / D2\tP', formatter.format_output_line(res))


if __name__ == '__main__':
    unittest.main()
