#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import sys

def parse_definitions(val):
    if len(val) == 0:
        return []

    res = re.sub(u'[①②③④⑤⑥⑦⑧⑨]+', '|', val)
    vals = map((lambda s: s.strip()), res.split('|'))
    return vals[1:9]

def parse(val):
    re_QW = re.compile('^([\w]+)\[.*\]\s+(\w+)\s+(.*)', re.UNICODE)
    res = re.match(re_QW, val)
    if res is None:
        return {}

    definitions = parse_definitions(res.group(3))
    return {'hanzi': res.group(1), 'pinyin': res.group(2), 'defs': definitions}

def format_csv_entry(vals):
    if len(vals) < 3:
        return ''

    defns = ' / '.join(vals.get('defs', ''))
    return unicode(','.join([vals.get('hanzi', ''),
                             vals.get('pinyin', ''),
                             defns]))

def process_file(in_filename, out_filename):
    with open(out_filename, 'w') as out_file:
        with open(in_filename) as in_file:
            for l in in_file:
                res = parse(l.decode('utf8'))
                if len(res) >= 3:
                    out_line = format_csv_entry(res)
                    out_file.write(out_line.encode('utf-8'))
                    out_file.write('\n')

def help_text(name):
    return "usage: %s [infile] [outfile]" % name

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print help_text(sys.argv[0])
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2])
