import unittest
from src.leafnode import LeafNode
from src.markdown_parser import markdown_to_html, extract_title
from src.htmlnode import HTMLNode
from src.parent_node import ParentNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        markdown = "This is a paragraph.\n\nThis is another paragraph."
        html = markdown_to_html(markdown)
        expected = ParentNode(
            "div",
            [
                LeafNode("p", "This is a paragraph."),
                LeafNode("p", "This is another paragraph."),
            ],
        )
        self.assertEqual(html.to_html(), expected.to_html())

    def test_headings(self):
        markdown = "# Heading 1\n\n## Heading 2\n\n### Heading 3"
        html = markdown_to_html(markdown)
        expected = ParentNode(
            "div",
            [
                LeafNode("h1", "Heading 1"),
                LeafNode("h2", "Heading 2"),
                LeafNode("h3", "Heading 3"),
            ],
        )
        self.assertEqual(html.to_html(), expected.to_html())

    def test_lists(self):
        markdown = "* Item 1\n* Item 2\n* Item 3\n\n1. First\n2. Second\n3. Third"
        html = markdown_to_html(markdown)
        expected = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                        LeafNode("li", "Item 3"),
                    ],
                ),
                ParentNode(
                    "ol",
                    [
                        LeafNode("li", "First"),
                        LeafNode("li", "Second"),
                        LeafNode("li", "Third"),
                    ],
                ),
            ],
        )
        self.assertEqual(html.to_html(), expected.to_html())

    def test_code_blocks(self):
        markdown = "```\nprint('Hello World')\n```"
        html = markdown_to_html(markdown)
        expected = ParentNode(
            "div",
            [
                LeafNode("code", "\nprint('Hello World')\n"),
            ],
        )
        self.assertEqual(html.to_html(), expected.to_html())

    def test_blockquotes(self):
        markdown = ">This is a quote"
        html = markdown_to_html(markdown)
        expected = ParentNode(
            "div",
            [
                LeafNode("blockquote", "This is a quote"),
            ],
        )
        self.assertEqual(html.to_html(), expected.to_html())

    def test_mixed_content(self):
        markdown = "# Title\n\nParagraph here\n\n* List item 1\n* List item 2"
        html = markdown_to_html(markdown)
        expected = ParentNode(
            "div",
            [
                LeafNode("h1", "Title"),
                LeafNode("p", "Paragraph here"),
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "List item 1"),
                        LeafNode("li", "List item 2"),
                    ],
                ),
            ],
        )
        self.assertEqual(html.to_html(), expected.to_html())

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        self.assertEqual(extract_title("# My Title"), "My Title")

    def test_extract_title_with_extra_whitespace(self):
        self.assertEqual(extract_title("#    Spacey    Title    "), "Spacey    Title")

    def test_extract_title_with_multiple_headers(self):
        markdown = """# Main Title
        ## Secondary Title
        ### Tertiary Title"""
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_with_content(self):
        markdown = """Some content
        # Main Title
        More content"""
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_extract_title_missing(self):
        markdown = """## Secondary Title
        Regular paragraph
        ### Another header"""
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No h1 header found in markdown file")

    def test_extract_title_empty(self):
        with self.assertRaises(ValueError) as context:
            extract_title("")
        self.assertEqual(str(context.exception), "No h1 header found in markdown file")

if __name__ == "__main__":
    unittest.main() 