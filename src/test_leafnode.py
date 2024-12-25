import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_creation(self):
        # 测试基本创建
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, World!")
        self.assertIsNone(node.children)
        
    def test_leaf_node_with_props(self):
        # 测试带属性的节点
        props = {"class": "greeting", "id": "hello"}
        node = LeafNode("div", "Hello", props)
        self.assertEqual(node.to_html(), '<div class="greeting" id="hello">Hello</div>')

    def test_leaf_node_without_props(self):
        # 测试不带属性的节点
        node = LeafNode("div", "Hello")
        self.assertEqual(node.to_html(), '<div>Hello</div>')
    
    def test_leaf_node_without_value(self):
        # 测试没有value时应该抛出异常
        with self.assertRaises(ValueError):
            node = LeafNode(tag="p", value=None)
            node.to_html()
            
    def test_leaf_node_without_tag(self):
        # 测试没有tag的情况
        node = LeafNode(tag=None, value="text")
        self.assertEqual(node.to_html(), "text")

if __name__ == "__main__":
    unittest.main() 