# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson

from qingwen import parse
import unittest


class TestParser(unittest.TestCase):
    def test_parse_empty_defn(self):
        self.assertEqual(parse.parse_definitions(''), [])

    def test_parse_single_numbered_defn(self):
        self.assertEqual(parse.parse_definitions(u' ① share '), [u'share'])

    def test_parse_single_defn(self):
        self.assertEqual(parse.parse_definitions(u'share'), [u'share'])

    def test_parse_multi_defn(self):
        res = parse.parse_definitions(u' ① share ② stock (market)')
        print res
        self.assertTrue(u'share' in res)

    def test_parse(self):
        test_str = u'股票[股票] gǔpiào ① share ② stock (market)'
        res = parse.parse(test_str)
        self.assertEqual(res["hanzi"], u'\u80a1\u7968')
        self.assertEqual(res["pinyin"], u'gǔpiào')
        self.assertTrue(u'share' in res["defs"])

    def test_parse_empty(self):
        res = parse.parse('')
        self.assertEqual(res, {})

    def test_no_numbers(self):
        res = parse.parse(u'斯德哥尔摩[斯德哥爾摩] Sīdégē\'ěrmó Stockholm, capital of Sweden')
        self.assertTrue('Stockholm, capital of Sweden' in res['defs'])

    def test_no_numbers2(self):
        res = parse.parse(u'一切[一切] yīqiè everything')
        self.assertTrue('everything' in res['defs'])

    def test_extra_brackets(self):
        res = parse.parse(u'加油[加油] jiāyóu ① to add oil ② to top up with gas ③ to refuel ④ to accelerate ⑤ abbr. for 加大油門|加大油门[jia1 da4 you2 men2] ⑥ to step on the gas ⑦ fig. to make an extra effort ⑧ fig. to cheer sb on')
        self.assertEqual(u'jiāyóu', res['pinyin'])


if __name__ == '__main__':
    unittest.main()
