# -*- coding: utf-8 -*-

import sys
import os
import sphinx_rtd_theme
#from better import better_theme_path

# -- General configuration ------------------------------------------------

def setup(app):
    app.add_stylesheet('extra.css')

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'RUPIN'
copyright = u'2019-2020 rateionn@gmail.com 天埜零士'
author = u'rateionn@天埜零士'

version = u'1.0.0'
release = u'1.0.0'

pygments_style = 'sphinx'

highlight_language = "python"

# -- Options for HTML output ----------------------------------------------

from recommonmark.parser import CommonMarkParser
 
source_parsers = {
    '.md': CommonMarkParser,
}
 
source_suffix = ['.rst', '.md']
html_theme = 'sphinx_rtd_theme'

# html_theme_options = {
    # 'sidebarwidth': '20rem',
    # 'cssfiles': ['_static/extra.css']
# }

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = "After Effects Scripting Guide"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = "Home"

# html_logo = None
locale_dirs = [
    'locale/',
]

# html_favicon = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['.static']
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# html_extra_path = []

# html_last_updated_fmt = ''

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     '**': ['searchbox.html', 'localtoc.html', 'globaltoc.html'],
#     'index': ['searchbox.html']
# }

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# html_show_sphinx = True

# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# html_search_language = 'en'

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'rupin'