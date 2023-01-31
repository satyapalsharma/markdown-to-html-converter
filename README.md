# Markdown to HTML Converter

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A command-line interface (CLI) tool that converts Markdown files to styled HTML, complete with syntax highlighting for code blocks.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Custom Styling](#custom-styling)
- [Contributing](#contributing)
- [License](#license)

## Description

The Markdown to HTML Converter is a lightweight and efficient CLI tool designed to transform your Markdown documents into beautiful, web-ready HTML files. It leverages popular Python libraries to ensure accurate Markdown parsing and professional-grade syntax highlighting, making it ideal for documentation, blog posts, or any content that needs to be presented on the web.

## Features

*   **Markdown to HTML Conversion:** Converts standard Markdown syntax into valid HTML.
*   **Syntax Highlighting:** Automatically highlights code blocks using [Pygments](https://pygments.org/), supporting a wide range of programming languages.
*   **Default Styling:** Includes a default CSS stylesheet (`assets/default.css`) for a clean, readable presentation.
*   **Custom Styling:** Allows users to provide their own CSS files for complete control over the output's appearance.
*   **CLI Interface:** Easy-to-use command-line interface for quick conversions.
*   **Output Control:** Specify the output HTML file name and location.

## Tech Stack

*   **Python 3.8+**: The core programming language.
*   **`markdown`**: A Python library for converting Markdown to HTML.
*   **`pygments`**: A generic syntax highlighter for various languages.

## Installation

To get started with the Markdown to HTML Converter, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/markdown-to-html-converter.git
    cd markdown-to-html-converter
    ```

2.  **Install dependencies:**
    It's recommended to use a virtual environment.

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    pip install .
    ```
    This will install `markdown` and `pygments` as specified in `pyproject.toml`.

## Usage

The converter can be run directly from the command line.

### Basic Conversion

Convert a Markdown file to HTML. By default, the output HTML file will have the same name as the input Markdown file, but with a `.html` extension, and will be created in the current directory.

```bash
python -m src.main input.md
```

Example: `python -m src.main my_document.md` will create `my_document.html`.

### Specifying Output File

Use the `-o` or `--output` flag to specify the name and/or path of the output HTML file.

```bash
python -m src.main input.md -o output.html
```

Example: `python -m src.main notes.md -o build/notes_final.html`

### Using Custom CSS

By default, the tool includes `assets/default.css`. To use your own stylesheet, provide its path using the `-c` or `--css` flag.

```bash
python -m src.main input.md -c path/to/your/custom.css
```

Example: `python -m src.main article.md -c styles/dark_theme.css`

### Full Example

```bash
python -m src.main my_report.md -o reports/final_report.html -c assets/custom_report.css
```

### Help

To see all available options:

```bash
python -m src.main --help
```

## Custom Styling

The project includes a default stylesheet at `assets/default.css`. This file provides basic styling for common Markdown elements and Pygments-generated syntax highlighting.

If you wish to customize the look and feel:
1.  Create your own `.css` file.
2.  Pass its path using the `-c` flag during conversion.

The custom CSS will be embedded directly into the `<head>` section of the generated HTML, overriding or complementing the default styles as per CSS specificity rules.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug reports, or want to add new features, please follow these steps:

1.  **Fork** the repository.
2.  **Create a new branch** for your feature or bug fix: `git checkout -b feature/your-feature-name` or `bugfix/issue-description`.
3.  **Make your changes** and ensure the code adheres to the project's style guidelines (e.g., using `black` for formatting).
4.  **Write tests** for your changes if applicable.
5.  **Commit your changes** with a clear and descriptive message.
6.  **Push your branch** to your forked repository.
7.  **Open a Pull Request** to the `main` branch of the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.