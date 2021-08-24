#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers import rst

from hashlib import sha256

# state class to contain the counter
class _spoiler:
    count = {}

    @staticmethod
    def id(src):
        if src in _spoiler.count:
            n = _spoiler.count[src] = _spoiler.count[src] + 1
        else:
            n = _spoiler.count[src] = 1

        return 'spoil-%s%03d' % (sha256(src.encode()).hexdigest()[:7], n)

def spoiler_role(name, rawtext, text, lineno, inliner,
                 options={}, content=[]):
    src = inliner.document.attributes['source']
    html = (
        '<input id="{id}" type="checkbox" class="spoiler" checked />'+\
        '<label for="{id}" class="spoiler">{text}</label>'
    ).format(text=text, id=_spoiler.id(src))
    return [nodes.raw('', html, format='html')], []

def register():
    rst.roles.register_local_role('spoiler', spoiler_role)
