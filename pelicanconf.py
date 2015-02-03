#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'pybombs'
SITENAME = u'CGRAN-Frontend'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME= 'proto-pybombs'

DIRECT_TEMPLATES = ('index', 'recipelist',)
PAGE_PATHS = ["oot_modules"]

## custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/recipelist.html': 'recipelist.html'}
