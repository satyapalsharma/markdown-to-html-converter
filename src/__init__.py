"""
Markdown to HTML Converter package initialization.

This file marks the 'src' directory as a Python package and defines its public API.
It also sets the package version.
"""

# Define the package version.
# This is a common practice to make the version easily accessible programmatically
# (e.g., `import src; print(src.__version__)`).
__version__ = "0.1.0"

# Import core components from submodules to make them directly accessible
# from the 'src' package namespace. This simplifies imports for users of the package.
# For example, instead of `from src.converter import MarkdownConverter`,
# users can write `from src import MarkdownConverter`.

# Import the main conversion function and class from the converter module.
from .converter import convert_markdown_to_html, MarkdownConverter

# Import the code highlighter class from the highlighter module.
from .highlighter import CodeHighlighter

# Define __all__ to explicitly list the public API of the package.
# When a user does `from src import *`, only the names listed here will be imported.
# This helps prevent accidental exposure of internal modules or variables.
__all__ = [
    "__version__",
    "convert_markdown_to_html",
    "MarkdownConverter",
    "CodeHighlighter",
]

# Any package-level initialization or configuration can be placed here.
# For this project, no specific initialization is required at the package level.
# Examples might include setting up logging, loading configuration files, etc.
# if the package had more complex global state.
#
# import logging
# logging.basicConfig(level=logging.INFO)
#
# Or, if there were default styles or assets that needed to be loaded once:
# from pathlib import Path
# DEFAULT_CSS_PATH = Path(__file__).parent.parent / "assets" / "default.css"
# if not DEFAULT_CSS_PATH.exists():
#     logging.warning(f"Default CSS file not found at {DEFAULT_CSS_PATH}")
```