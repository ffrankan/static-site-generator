from unittest import TestCase

from src.node_parser import NodeParser, CompositeNodeParser
from src.textnode import TextType, TextNode


class TestNodeParser(TestCase):
    def test_node_parser_text(self):
        text = "Simple text"
        parser = NodeParser(TextType.TEXT)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 1)
        self.assertListEqual([
            TextNode("Simple text", TextType.TEXT)
        ], actual_result)

    def test_node_parser_bold(self):
        text = "This is **bold** text"
        parser = NodeParser(TextType.BOLD)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ], actual_result)

    def test_node_parser_italic(self):
        text = "This is *italic* text"
        parser = NodeParser(TextType.ITALIC)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ], actual_result)

    def test_node_parser_code(self):
        text = "This is `code` text"
        parser = NodeParser(TextType.CODE)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ], actual_result)

    def test_node_parser_link(self):
        text = "This is [link](https://example.com) text"
        parser = NodeParser(TextType.LINK)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" text", TextType.TEXT)
        ], actual_result)

    def test_node_parser_image(self):
        text = "This is ![image](https://example.com/img.png) text"
        parser = NodeParser(TextType.IMAGE)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" text", TextType.TEXT)
        ], actual_result)

    def test_node_parser_empty_text(self):
        text = ""
        parser = NodeParser(TextType.BOLD)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 0)
        self.assertListEqual([], actual_result)

    def test_node_parser_multiple_matches(self):
        text = "**bold1** normal **bold2**"
        parser = NodeParser(TextType.BOLD)
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("bold1", TextType.BOLD),
            TextNode(" normal ", TextType.TEXT),
            TextNode("bold2", TextType.BOLD)
        ], actual_result)


class TestCompositeNodeParser(TestCase):
    def test_parse_bold(self):
        text = "This is **bold** text"
        parser = CompositeNodeParser([NodeParser(TextType.BOLD)])
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ], actual_result)

    def test_parse_mixed_content(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        parser = CompositeNodeParser([
            NodeParser(TextType.BOLD),
            NodeParser(TextType.CODE),
            NodeParser(TextType.ITALIC),
            NodeParser(TextType.IMAGE),
            NodeParser(TextType.LINK)
        ])
        actual_result = parser.parse(text)
        print(actual_result)

        self.assertEqual(10, len(actual_result))
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], actual_result)

    def test_parse_link(self):
        text = "Click [here](https://example.com) to visit"
        parser = CompositeNodeParser([NodeParser(TextType.LINK)])
        actual_result = parser.parse(text)

        self.assertEqual(len(actual_result), 3)
        self.assertListEqual([
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://example.com"),
            TextNode(" to visit", TextType.TEXT)
        ], actual_result)

    def test_parse_italic_with_asterisk(self):
        text = "Disney *didn't ruin it*"
        parser = CompositeNodeParser([NodeParser(TextType.ITALIC)])
        actual_result = parser.parse(text)

        expected_result = [
            TextNode("Disney ", TextType.TEXT),
            TextNode("didn't ruin it", TextType.ITALIC),
        ]
        
        self.assertEqual(len(actual_result), 2)
        self.assertEqual(actual_result, expected_result)
