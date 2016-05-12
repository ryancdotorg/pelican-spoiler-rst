#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers import rst

def spoiler_role(name, rawtext, text, lineno, inliner,
                 options={}, content=[]):
    html = ('<label>'+\
           '<input type="checkbox" class="spoiler" checked />'+\
           '<span class="spoiler">{text}</span>'+\
           '</label>').format(text=text)
    return [nodes.raw('', html, format='html')], []
 
def register():
    rst.roles.register_local_role('spoiler', spoiler_role)
