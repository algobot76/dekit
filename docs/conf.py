# Project
project = 'Dekit'
copyright = '2019 Kaitian Xie'
author = 'Kaitian Xie'
version = 'v0.0.1'
release = 'v0.0.1'

# General
master_doc = 'index'
extensions = ["sphinx.ext.autodoc"]
exclude_patterns = ['_build']

# HTML
html_theme = 'default'
html_static_path = ['_static']
html_title = f'Dekit Documentation ({version})'
html_show_sourcelink = False

# LaTex
latex_documents = [
    (master_doc, f'dekit-{version}.tex', html_title, author, 'manual'),
]
