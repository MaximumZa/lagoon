import os
import sys

# Minimal required Sphinx settings
project = 'Lagoon Documentation'
copyright = '2025'
author = 'Author'

# Required Sphinx stubs
extensions = []
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Basic theme (will be overwritten)
html_theme = 'alabaster'