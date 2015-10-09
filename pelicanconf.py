#!/usr/bin/env python
# -*- coding: gbk -*- #
from __future__ import unicode_literals

AUTHOR = r'heifrank'
SITENAME = r'新世界'
SITEURL = 'http://heifrank.github.io'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
ARCHIVES_URL = 'archives.html'
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('my sina blog', 'http://blog.sina.com.cn/u/2310559855'),
          ('google', 'http://www.google.com'),)

DEFAULT_PAGINATION = 10



DISQUS_SITENAME = 'heifrank27'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GOOGLE_ANALYTICS = 'UA-44573192-1'


THEME = r'/Users/heifrank/Downloads/pelican-themes/gum'
# PLUGIN_PATH = r"C:/Users/songyang/AppData/Local/GitHub/pelican-plugins"
# PLUGINS = ["sitemap"]

SITEMAP = {
	"format": "xml",
	"priorities": {
		"articles": 0.7,
		"indexes": 0.5,
		"pages": 0.3,
	},
	"changefreqs": {
		"articles": "monthly",
		"indexes": "daily",
		"pages": "monthly",
	}
}
