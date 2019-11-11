import msmb_theme

# Project Information
project = "Sphinx-Themes template"
copyright = "2018, sphinx-themes.org"
author = "sphinx-themes.org"
version = ""
release = "1"

# Setup Extensions.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
]

# Setup core configuration.
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

# Define Satic Asset Location.
html_static_path = ["_static"]

# Setup theme
html_theme = "msmb_theme"
html_theme_path = [msmb_theme.get_html_theme_path()]
