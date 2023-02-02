import markdown
from src.highlighter import pygments_highlighter_callable

def convert_markdown_to_html(markdown_text: str) -> str:
    """
    Converts Markdown text to HTML, including syntax highlighting for code blocks
    using Pygments via the custom highlighter in `src.highlighter`.

    This function initializes the Markdown converter with a set of common extensions
    to provide a rich conversion experience, including tables, footnotes, and
    improved list handling. Crucially, it configures the `fenced_code` extension
    to use our custom Pygments-based callable for syntax highlighting.

    Args:
        markdown_text: The input Markdown string to be converted.

    Returns:
        The converted HTML string.
    