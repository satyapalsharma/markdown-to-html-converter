```python
import argparse
import sys
from pathlib import Path

# Import the converter module from our project's src directory.
# This allows us to use functions defined in src/converter.py.
from src import converter

def main():
    """
    Main function for the Markdown to HTML Converter CLI tool.

    It parses command-line arguments, reads the input Markdown file,
    delegates the conversion to the `converter` module, and writes
    the resulting HTML to an output file.
    """
    # 1. Argument Parsing
    # -------------------
    parser = argparse.ArgumentParser(
        description="Convert Markdown files to styled HTML with syntax highlighting.",
        formatter_class=argparse.RawTextHelpFormatter # Preserves newlines in help messages
    )

    parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        help="Path to the input Markdown file."
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Path to the output HTML file. If not specified, it defaults to\n"
             "<input_file_name>.html in the same directory as the input file."
    )
    parser.add_argument(
        "-s", "--style",
        type=str,
        default="default",
        help="Name of the Pygments style to use for syntax highlighting (e.g., 'default', 'monokai', 'solarized-light').\n"
             "The 'default' style also includes the base styling from assets/default.css."
    )

    args = parser.parse_args()

    input_path: Path = args.input
    output_path: Path = args.output
    style_name: str = args.style

    # 2. Input File Validation
    # ------------------------
    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)
    if not input_path.is_file():
        print(f"Error: Input path '{input_path}' is not a file.", file=sys.stderr)
        sys.exit(1)

    # 3. Determine Output Path
    # ------------------------
    # If the output path is not provided, derive it from the input file's name.
    if output_path is None:
        output_path = input_path.with_suffix(".html")
        print(f"Output file not specified. Defaulting to '{output_path}'.")

    # 4. Read Markdown Content
    # ------------------------
    markdown_content: str
    try:
        # Read the entire content of the Markdown file using UTF-8 encoding.
        markdown_content = input_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # This case should ideally be caught by input_path.exists(), but kept for robustness.
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        # Catch general I/O errors during file reading (e.g., permission denied).
        print(f"Error reading input file '{input_path}': {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors during file reading.
        print(f"An unexpected error occurred while reading '{input_path}': {e}", file=sys.stderr)
        sys.exit(1)

    # 5. Convert Markdown to HTML
    # ---------------------------
    html_content: str
    try:
        # Delegate the core conversion logic to the converter module.
        # It handles Markdown parsing, syntax highlighting, and CSS embedding.
        html_content = converter.convert_markdown_to_html(markdown_content, style_name)
    except ValueError as e:
        # Catch specific errors from the converter, e.g., an invalid style name.
        print(f"Conversion error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors during the conversion process.
        print(f"An unexpected error occurred during conversion: {e}", file=sys.stderr)
        sys.exit(1)

    # 6. Write HTML Content to Output File
    # ------------------------------------
    try:
        # Write the generated HTML content to the specified output file.
        # This will overwrite the file if it already exists.
        output_path.write_text(html_content, encoding='utf-8')
        print(f"Successfully converted '{input_path}' to '{output_path}' using style '{style_name}'.")
    except IOError as e:
        # Catch general I/O errors during file writing (e.g., permission denied, disk full).
        print(f"Error writing output file '{output_path}': {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors during file writing.
        print(f"An unexpected error occurred while writing to '{output_path}': {e}", file=sys.stderr)
        sys.exit(1)

# Entry point for the script.
# This ensures that `main()` is called only when the script is executed directly.
if __name__ == "__main__":
    main()
```