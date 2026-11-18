"""
PathSnap - Laptop 2 UI Entry Point.
Run this file directly to start the Evaluator Dashboard:
    streamlit run ui.py
"""

import sys
import os

# Ensure project root is in Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Run the Streamlit UI application
from src.ui.app import *
