# Static Site Generator

This project is a static site generator that converts markdown files into HTML pages using a specified template. It supports various markdown features such as headings, lists, code blocks, and more.

## Features

- Converts markdown to HTML
- Supports headings, lists, blockquotes, code blocks, and inline styles (bold, italic, links, images)
- Maintains directory structure when generating HTML files
- Uses a template to wrap generated HTML content
- Includes a simple web server to serve the generated site

## Project Structure

- `src/`: Contains the source code for the markdown parser and HTML generation.
  - `markdown_parser.py`: Main module for converting markdown to HTML.
  - `block_parser.py`: Parses markdown into blocks and identifies block types.
  - `node_parser.py`: Parses text nodes for inline styles.
  - `textnode.py`, `leafnode.py`, `parent_node.py`, `htmlnode.py`: Define the node structure for HTML generation.
- `content/`: Contains markdown files to be converted.
- `static/`: Contains static assets like CSS files.
- `public/`: Output directory for generated HTML files.
- `template.html`: HTML template used for wrapping generated content.
- `main.py`: Main script to generate the site.
- `test/`: Contains unit tests for the project.

## Getting Started

### Prerequisites

- Python 3.9 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies (if any).

### Usage

1. Place your markdown files in the `content/` directory.

2. Run the main script to generate the site:
   ```bash
   python3 src/main.py
   ```

3. Start the web server to view the site:
   ```bash
   bash main.sh
   ```

4. Open your browser and navigate to `http://localhost:8888` to view the generated site.

## Testing

Run the unit tests to ensure everything is working correctly: