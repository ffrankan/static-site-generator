import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node
from src.node_parser import CompositeNodeParser, NodeParser


class TestTextNode(unittest.TestCase):


    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_text_node_to_html_node_italic(self):
        # Test italic text conversion
        node = TextNode("didn't ruin it", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "didn't ruin it")
        self.assertEqual(html_node.to_html(), "<i>didn't ruin it</i>")

    def test_complete_text_to_html_flow(self):
        # Test the complete flow from parsing to HTML generation
        text = "Disney *didn't ruin it*"
        parser = CompositeNodeParser([NodeParser(TextType.ITALIC)])
        nodes = parser.parse(text)
        
        html = "".join([text_node_to_html_node(node).to_html() for node in nodes])
        
        # 验证每个节点的内容
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "Disney ")  # 注意这里的空格
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "didn't ruin it")
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        
        # 验证最终的HTML输出
        self.assertEqual(html, "Disney <i>didn't ruin it</i>")  # 注意空格的位置

if __name__ == "__main__":
    unittest.main()
