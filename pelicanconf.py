#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'bobobo80'
SITENAME = 'On the wing 展翼'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# theme
THEME = 'attila'
HEADER_COVERS_BY_TAG = {}
HEADER_COVERS_BY_CATEGORY = {}

STATIC_PATHS = ['assets', 'images']
EXTRA_PATH_METADATA = {
    'assets/CNAME': {'path': 'CNAME'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/robots.txt': {'path': 'robots.txt'},
}
HOME_COVER = 'images/post-bg.jpg'

COLOR_SCHEME_CSS = 'tomorrow.css'

PLUGIN_PATHS = ["pelican-plugins"]

PLUGINS = [
    "sitemap",
]

SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.3},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/bobobo80'),
          )

AUTHOR_META = {
    "bobobo80": {
        "name": "bobobo80",
        "image": "images/avatar.png",
        "website": "https://about.me/bobobo80",
        "github": "bobobo80",
        "location": "Singapore",
    }
}

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# PAGE_URL = 'pages/{slug}/'
# PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
