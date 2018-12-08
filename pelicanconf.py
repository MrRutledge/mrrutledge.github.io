#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")


AUTHOR = 'MrRutledge'
SITENAME = 'Karim2km.github.io'
SITEURL = 'https://mrrutledge.github.io'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'
 

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

THEME = "./pelican-octopress-theme"
#RELATIVE_URLS = True

PLUGIN_PATH = ['../pelican-plugins']
PLUGIN = ['a-plugin']



MARKUP = ('rst', 'md', 'ipynb', )
#MARKUP = ('rst', 'md', )
IGNORE_FILES = ['.ipynb_checkpoints']