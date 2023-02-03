```python
import logging
from typing import Optional

from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

# Configure logging for this module.
# The root logger is used here, but in a larger application, you might
# configure a specific logger for this module.
logger = logging.getLogger(__name__)

# --- Constants and Configuration ---

# Default Pygments style to use for syntax highlighting.
# Pygments comes with many built-in styles (e.g., 'default', 'monokai', 'solarized-light').
DEFAULT_HIGHLIGHT_STYLE = 'default'

# Default CSS class applied to the <pre> tag containing highlighted code.
# This allows for consistent styling of code blocks across the application.
DEFAULT_CSS_CLASS = 'highlight'

# --- Public Functions ---

def highlight_code(code: str, lang: Optional[str] = None, style: str = DEFAULT_HIGHLIGHT_STYLE) -> str:
    """
    Syntax highlights a given code string using Pygments and returns the HTML representation.

    This function attempts to find a suitable Pygments lexer based on the provided
    language hint. If no language is specified, or if the specified language is
    not found, Pygments will attempt to guess the language from the code content.
    If no lexer can be determined even after guessing, the code will be returned
    wrapped in a simple <pre> tag without syntax highlighting, but with HTML
    special characters escaped to prevent XSS and ensure correct rendering.

    Args:
        code: The raw code string to highlight.
        lang: The