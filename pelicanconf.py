#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'pybombs'
SITENAME = u'The Comprehensive GNU Radio Archive Network'

PATH = 'content'

TIMEZONE = 'US/Eastern'
#SITEURL = 'http://nathanwest.us/cgran'
SITEURL = 'http://www.cgran.org'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

FILES_TO_COPY = (
            ('src/projects.html', 'projects/index.html'),
            )
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME= 'pybombs-theme'

PLUGIN_PATHS = ['plugins/pelican-md-metayaml']
PLUGINS = ['md_metayaml']
DIRECT_TEMPLATES = ['index',]
PAGE_PATHS = ['oot_modules']
LOAD_CONTENT_CACHE=False
ARTICLE_EXCLUDE=['oot_modules']
#STATIC_PATHS = ["js"]

## custom page generated with a jinja2 template
