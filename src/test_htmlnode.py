from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # given
        expected = 'href="https://www.google.com" target="_blank"'
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank"})
        # when
        result = node.props_to_html()
        # then
        self.assertEqual(result, expected)

    def test_props_to_html_with_no_props(self):
        # given
        expected = ""
        node = HTMLNode(tag="a", value="Google")
        # when
        result = node.props_to_html()
        # then
        self.assertEqual(result, expected)
    
    def test_eq(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertNotEqual(node, node2)

if __name__ == '__main__':
    unittest.main()
