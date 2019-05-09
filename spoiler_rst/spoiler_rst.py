#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers import rst

# state class to contain the counter
class _spoiler:
    counter = 0

    @staticmethod
    def id():
        _spoiler.counter += 1
        return 'spoil%d' % _spoiler.counter

def spoiler_role(name, rawtext, text, lineno, inliner,
                 options={}, content=[]):
    html = (
        '<input id="{id}" type="checkbox" class="spoiler" checked />'+\
        '<label for="{id}" class="spoiler">{text}</label>'
    ).format(text=text, id=_spoiler.id())
    return [nodes.raw('', html, format='html')], []
 
def register():
    rst.roles.register_local_role('spoiler', spoiler_role)
