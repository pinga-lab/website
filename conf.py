from __future__ import unicode_literals
import os
import subprocess
import datetime

AUTHOR = u'Leonardo Uieda'
SITETITLE = u'<strong>PINGA</strong>lab'
SITENAME = u"PINGA lab"
SITEKEYWORDS = u'geophysics, earth, earthscience, science, foss, scientific software'
SITEURL = ''
SITELOGO = 'images/pinga-logo.png'
REPOURL = 'https://github.com/pinga-lab/website'

# Language and time
DEFAULT_LANG = u'en'
TIMEZONE = u'America/Sao_Paulo'
BUILD_TIME = datetime.date.today().strftime(format='%d-%b-%Y')

# Get the current git commit hash
COMMIT = ''
process = subprocess.Popen('git rev-parse HEAD'.split(), cwd='.',
                           stdout=subprocess.PIPE)
git_hash = process.communicate()[0].strip().decode('utf-8')
if git_hash:
    COMMIT = ' (<a href="{url}/commit/{commit}">{commit_link}</a>)'.format(
            url=REPOURL, commit=git_hash, commit_link=git_hash[:7])

# This goes at the footer of the site
FOOTER_LEFT = """
This work is licensed
<a rel="license"
 href="http://creativecommons.org/licenses/by/4.0/deed.en_US">CC-BY</a>.
<br/>
Powered by <a href="http://getpelican.com/">Pelican</a>,
<a href="http://python.org">Python</a>,
and <a href="http://getbootstrap.com/">Bootstrap</a>.
</br>
Icons by <a href="http://fontawesome.io/">Font Awesome</a>
and <a href="http://jpswalsh.github.io/academicons/">Academicons</a>.
"""
FOOTER_RIGHT = """
Built by <a href="https://travis-ci.org/">Travis CI</a>
and
hosted on <a href="https://pages.github.com/">Github Pages</a>.
</br>
Latest build on {date}{commit}.
</br>
Source code at
<a href="{repo}">{repo_name}</a>.
""".format(date=BUILD_TIME, commit=COMMIT, repo=REPOURL, repo_name=REPOURL[8:])

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
