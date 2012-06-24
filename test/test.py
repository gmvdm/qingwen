# -*- coding: utf-8 -*-

import qingwen
import unittest

class TestParser(unittest.TestCase):
    def test_parse_empty_defn(self):
        self.assertEqual(qingwen.parse_definitions(''), [])

    def test_parse_single_numbered_defn(self):
        self.assertEqual(qingwen.parse_definitions(u' ① share '), [u'share'])

    def test_parse_single_defn(self):
        self.assertEqual(qingwen.parse_definitions(u'share'), [u'share'])

    def test_parse_multi_defn(self):
        res = qingwen.parse_definitions(u' ① share ② stock (market)')
        print res
        self.assertTrue(u'share' in res)

    def test_parse(self):
        test_str = u'股票[股票] gǔpiào ① share ② stock (market)'
        res = qingwen.parse(test_str)
        self.assertEqual(res["hanzi"], u'\u80a1\u7968')
        self.assertEqual(res["pinyin"], u'gǔpiào')
        self.assertTrue(u'share' in res["defs"])

    def test_parse_empty(self):
        res = qingwen.parse('')
        self.assertEqual(res, {})

    def test_no_numbers(self):
        res = qingwen.parse(u'斯德哥尔摩[斯德哥爾摩] Sīdégē\'ěrmó Stockholm, capital of Sweden')
        self.assertTrue('Stockholm, capital of Sweden' in res['defs'])

    def test_no_numbers2(self):
        res = qingwen.parse(u'一切[一切] yīqiè everything')
        self.assertTrue('everything' in res['defs'])


class TestFormatter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual('', qingwen.format_output_line({}))

    def test_single(self):
        res = {"hanzi": "H", "pinyin": "P", "defs": ['D1']}
        self.assertEqual('H\tD1\tP', qingwen.format_output_line(res))

    def test_multi(self):
        res = {"hanzi": "H", "pinyin": "P", "defs": ['D1', 'D2']}
        self.assertEqual('H\tD1 / D2\tP', qingwen.format_output_line(res))

if __name__ == '__main__':
    unittest.main()
