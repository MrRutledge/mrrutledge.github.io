#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'MrRutledge'
SITENAME = u'MrRutledge'
SITEURL = ''

PATH = '.\content'
OUTPUT_PATH = '../'

#CURRENT_YEAR = time.strftime("%Y")

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
SITETAG = "Text that's displayed in the title on the home page."

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

# See https://pythonhosted.org/Markdown/reference.html#lazy_ol for lazy_ol settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
    'lazy_ol': False 
}

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"] 

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Google+', 'http://plus.google.com/userid',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/kareemrim',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin-url',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/mrrutledge',
         'fa fa-github-square fa-fw fa-lg'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../voidy-bootstrap'


