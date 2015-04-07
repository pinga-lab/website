from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'
SITETITLE = u'<strong>PINGA</strong>lab'
SITENAME = u"PINGA lab"
SITEKEYWORDS = u'geophysics, earth, earthscience, science, foss, scientific software'
SITEURL = ''
SITELOGO = 'images/pinga-logo.png'

# Language and time
DEFAULT_LANG = u'en'
TIMEZONE = u'America/Sao_Paulo'

# This goes at the footer of the site
COPYRIGHT_NOTICE = """
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
>Creative Commons Attribution 4.0 International License</a>.
"""
EXTRA_FOOTER = """
Built by <a href="https://travis-ci.org/">Travis CI</a>
and
hosted on <a href="https://pages.github.com/">Github Pages</a>.
</br>
Icons by <a href="http://fontawesome.io/">Font Awesome</a>
and <a href="http://jpswalsh.github.io/academicons/">Academicons</a>.
</br>
Source code at <a href="https://github.com/pinga-lab/website">github.com/pinga-lab/website</a>.
"""

# Where to put generated files
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
USE_FOLDER_AS_CATEGORY = True
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = [
    'images',
    'pdf',
    'extra/CNAME',
    'extra/.nojekyll',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/.nojekyll': {'path': '.nojekyll'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

ARTICLES_FRONT_PAGE = 5
SUMMARY_MAX_LENGTH = 25
DEFAULT_PAGINATION = 0
DISPLAY_CATEGORIES_ON_MENU = False

# Feeds
FEED_ALL_RSS = False
FEED_ALL_ATOM = False

THEME = 'theme'

# Top menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('About', '/index.html'),
    ('Research', '/research.html'),
    ('People', '/people'),
    ('Papers', '/papers'),
    #('Talks', '/talks'),
    ('<i class="fa fa-github fa-lg" title="Github repositories"></i>',
        'https://github.com/pinga-lab'),
]

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary',
           'render_math',
           'sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5},
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'}
}

RESPONSIVE_IMAGES = False
FIGURE_NUMBERS = True
