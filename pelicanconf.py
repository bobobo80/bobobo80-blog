#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'bobobo80'
SITENAME = 'On the wing 展翼'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

OUTPUT_PATH = 'docs/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         )

# Social widget
SOCIAL = (('github', 'https://github.com/bobobo80'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme
THEME = 'attila'
HEADER_COVERS_BY_TAG  = {}
HEADER_COVERS_BY_CATEGORY = {}

# Analytics
GOOGLE_ANALYTICS = None