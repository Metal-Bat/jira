# ruff: noqa

import os
import sys

import django

if os.getenv("READTHEDOCS", default=False) == "True":
    sys.path.insert(0, os.path.abspath(".."))
    os.environ["DJANGO_READ_DOT_ENV_FILE"] = "True"
    os.environ["USE_DOCKER"] = "no"
else:
    sys.path.insert(0, os.path.abspath("/app"))

os.environ["DATABASE_URL"] = "sqlite:///readthedocs.db"
os.environ["CELERY_BROKER_URL"] = os.getenv("REDIS_URL", "redis://redis:6379")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django.local")
django.setup()

# -- Project information -----------------------------------------------------
project = "jira"
copyright = """2024, Erfan Ehsany"""
author = "Erfan Ehsany"


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "alabaster"
