# -*- coding: utf-8 -*-
# Copyright (c) 2012 Geoff Wilson


def format_output_line(vals):
    """Given a dict, produce a tab separated output line"""
    if len(vals) < 3:
        return ''

    defns = ' / '.join(vals.get('defs', ''))
    return u'%s\t%s\t%s' % (vals.get('hanzi', ''),
                            defns,
                            vals.get('pinyin', ''))
