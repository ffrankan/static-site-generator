from unittest import TestCase
from src.block_parser import markdown_to_blocks, identify_block_type


class Test(TestCase):
    def test_markdown_to_blocks(self):
        # Given
        markdown_content = """
        # This is a heading
        
        This is a paragraph of text. It has some **bold** and *italic* words inside of it.
        
        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """

        # When
        actual_result = markdown_to_blocks(markdown_content)

        # Then
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        
        self.assertEqual(len(actual_result), 3)
        self.assertEqual(actual_result, expected_blocks)

    def test_identify_paragraph_blocks(self):
        # Test cases for paragraphs
        test_cases = [
            (
                "This is a simple paragraph.",
                "paragraph"
            ),
            (
                "This is a paragraph\nwith multiple lines\njoined together.",
                "paragraph"
            ),
            (
                "This paragraph has **bold** and *italic* text.",
                "paragraph"
            )
        ]
        
        for test_input, expected_type in test_cases:
            with self.subTest(test_input=test_input):
                self.assertEqual(identify_block_type(test_input), expected_type)
            
    def test_identify_heading_blocks(self):
        # Test cases for headings
        test_cases = [
            (
                "# This is a heading",
                "heading1"
            ),
            (
                "## This is a heading",
                "heading2"
            ),
            (
                "### This is a heading",
                "heading3"
            ),
            (
                "#### This is a heading",
                "heading4"
            ),
            (
                "##### This is a heading",
                "heading5"
            ),
            (
                "###### This is a heading",
                "heading6"
            )
        ]

        for test_input, expected_type in test_cases:
            with self.subTest(test_input=test_input):
                self.assertEqual(identify_block_type(test_input), expected_type)

    def test_identify_code_blocks(self):
        # Test cases for list blocks
        test_cases = [
            (
                "```python\nprint('Hello, World!')\n```",
                "code"
            ),
            (
                "```javascript\nconsole.log('Hello, World!')\n```",
                "code"
            )
        ]

        for test_input, expected_type in test_cases:
            with self.subTest(test_input=test_input):
                self.assertEqual(identify_block_type(test_input), expected_type)

    def test_identify_quote_blocks(self):
        # Test cases for quote blocks
        test_cases = [
            (
                "> This is a quote",
                "quote"
            ),
            (
                "> This is a quote\n> with multiple lines\n> joined together.",
                "quote"
            )
        ]

        for test_input, expected_type in test_cases:
            with self.subTest(test_input=test_input):
                self.assertEqual(identify_block_type(test_input), expected_type)

    def test_identify_unordered_list_blocks(self):
        # Test cases for unordered list blocks
        test_cases = [
            (
                "* This is a list item",
                "unordered_list"
            ),
            (
                "- This is a list item",
                "unordered_list"
            )
        ]

        for test_input, expected_type in test_cases:
            with self.subTest(test_input=test_input):
                self.assertEqual(identify_block_type(test_input), expected_type)

    def test_identify_ordered_list_blocks(self):
        # Test cases for ordered list blocks
        test_cases = [
            (
                "1. This is a list item",
                "ordered_list"
            ),
            (
                "1. This is a list item\n2. This is another list item\n3. This is another list item",
                "ordered_list"
            )
        ]

        for test_input, expected_type in test_cases:
            with self.subTest(test_input=test_input):
                self.assertEqual(identify_block_type(test_input), expected_type)
    
    def test_multiple_quotes_to_blocks(self):
        markdown_text = (
            "> First quote\n"
            "> Still first quote\n"
            ">\n"  # Empty line separator
            "> Second quote\n"
            ">\n"
            "> Third quote"
        )
        
        expected_blocks = [
            "First quote\nStill first quote",
            "Second quote", 
            "Third quote"
        ]
        
        result = markdown_to_blocks(markdown_text)

        self.assertEqual(len(result), 3)
        self.assertEqual(result, expected_blocks)