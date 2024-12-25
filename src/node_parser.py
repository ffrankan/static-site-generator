import re
from src.textnode import TextType, TextNode

class CompositeNodeParser:
    def __init__(self, parser_list = None):
        self.parsers = parser_list or []

    def parse(self, text: str):
        current_text = text
        result = [TextNode(current_text, TextType.TEXT)]

        for parser in self.parsers:
            new_result = []
            for node in result:
                if node.text_type == TextType.TEXT:
                    parsed_nodes = parser.parse(node.text)
                    new_result.extend(parsed_nodes)
                else:
                    new_result.append(node)
            result = new_result

        return result

class NodeParser:
    def __init__(self, text_type: TextType = None):
        self.text_type = text_type

    def parse(self, text: str):
    # 如果是纯文本类型，直接返回一个文本节点
        if self.text_type == TextType.TEXT:
            return [TextNode(text, TextType.TEXT)]

        result = []
        last_end = 0
        pattern = self.text_type.value.regex_pattern

        for match in re.finditer(pattern, text):
            start = match.start()
            if start > last_end:
                result.append(TextNode(text[last_end:start], TextType.TEXT))

            if self.text_type in (TextType.LINK, TextType.IMAGE):
                result.append(TextNode(match.group(1), self.text_type, match.group(2)))
            else:
                # 直接使用捕获组中的内容
                content = match.group(1)
                result.append(TextNode(content, self.text_type))

            last_end = match.end()

        if last_end < len(text):
            result.append(TextNode(text[last_end:], TextType.TEXT))

        return result