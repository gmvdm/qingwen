# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson

import re


def parse_definitions(val):
    """Given a definition string, return an array of definitions"""
    if len(val) == 0:
        return []

    res = re.sub(u'[①②③④⑤⑥⑦⑧⑨]+', '|', val)
    vals = map((lambda s: s.strip()), res.split('|'))
    if len(vals[0]) == 0:
        return vals[1:9]
    else:
        return vals[0:9]


def parse(val):
    """Given a unicode string from Qingwen, parse main parts"""
    re_QW = re.compile('^([\w]+)\[[^\]]*\]\s+(\S+)\s+(.*)', re.UNICODE)
    res = re.match(re_QW, val)
    if res is None:
        return {}

    definitions = parse_definitions(res.group(3))
    return {'hanzi': res.group(1), 'pinyin': res.group(2), 'defs': definitions}
