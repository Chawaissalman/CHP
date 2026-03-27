"""Streamlit entrypoint for deployment.

This thin wrapper lets you deploy using a standard root-level `app.py`
while keeping the main application code in `app_improved_same_structure.py`.
"""

from app_improved_same_structure import *  # noqa: F401,F403
