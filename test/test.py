# -*- coding: utf-8 -*-

import qingwen
import unittest

class TestParser(unittest.TestCase):
    def test_parse_empty_defn(self):
        self.assertEqual(qingwen.parse_definitions(''), [])

    def test_parse_single_defn(self):
        self.assertEqual(qingwen.parse_definitions(u' ① share '), [u'share'])

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


class TestFormatter(unittest.TestCase):
    def test_empty(self):
        self.assertEqual('', qingwen.format_csv_entry({}))

    def test_single(self):
        res = {"hanzi": "H", "pinyin": "P", "defs": ['D1']}
        self.assertEqual('H,P,D1', qingwen.format_csv_entry(res))

    def test_multi(self):
        res = {"hanzi": "H", "pinyin": "P", "defs": ['D1', 'D2']}
        self.assertEqual('H,P,D1 / D2', qingwen.format_csv_entry(res))

if __name__ == '__main__':
    unittest.main()
