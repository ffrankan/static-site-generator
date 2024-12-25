import unittest
from src.parent_node import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_parent_node_creation(self):
        node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),],)
        self.assertEqual(node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_parent_node_with_props(self):
        props = {"class": "greeting", "id": "hello"}
        node = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")], props)
        self.assertEqual(node.to_html(), '<div class="greeting" id="hello"><b>Bold text</b><i>italic text</i></div>')
    
    def test_parent_node_without_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag=None, children=[LeafNode("b", "Bold text"), LeafNode("i", "italic text")])
            node.to_html()

    def test_parent_node_without_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("div", children=None)
            node.to_html()

    def test_parent_node_equality(self):
        node1 = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")])
        node2 = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")])
        self.assertEqual(node1, node2)
    def test_parent_node_inequality(self):
        node1 = ParentNode("div", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")])
        node2 = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode("i", "italic text")])
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()