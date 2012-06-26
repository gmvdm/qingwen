#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson

import re
import sys


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


def format_output_line(vals):
    """Given a dict, produce a tab separated output line"""
    if len(vals) < 3:
        return ''

    defns = ' / '.join(vals.get('defs', ''))
    return u'%s\t%s\t%s' % (vals.get('hanzi', ''),
                            defns,
                            vals.get('pinyin', ''))


def process_file(in_filename, out_filename):
    with open(out_filename, 'w') as out_file:
        with open(in_filename) as in_file:
            for l in in_file:
                res = parse(l.decode('utf8'))
                if len(res) >= 3:
                    out_line = format_output_line(res)
                    out_file.write(out_line.encode('utf-8'))
                    out_file.write('\n')


def help_text(name):
    return "usage: %s [infile] [outfile]" % name


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print help_text(sys.argv[0])
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2])
