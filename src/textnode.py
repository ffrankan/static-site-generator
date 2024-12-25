from enum import Enum
from typing import NamedTuple
from src.leafnode import LeafNode


class TextAttributes(NamedTuple):
    value: str
    regex_pattern: str = None
    delimiter: str = None


class TextType(Enum):
    TEXT = TextAttributes("text", r".*?", None)
    BOLD = TextAttributes("bold", r"\*\*(.*?)\*\*", "**")
    ITALIC = TextAttributes("italic", r"\*((?!\*)(.*?))\*", "*")
    CODE = TextAttributes("code", r"`(.*?)`", "`")
    LINK = TextAttributes("link", r"\[(.*?)\]\((.*?)\)")
    IMAGE = TextAttributes("image", r"!\[(.*?)\]\((.*?)\)")


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __str__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                    self.text == other.text and
                    self.text_type == other.text_type and
                    self.url == other.url
            )
        return False

    def __repr__(self):
        return self.__str__()


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")
