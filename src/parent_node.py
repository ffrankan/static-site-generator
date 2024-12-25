from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props:dict=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        # 检查必需的 tag
        if not self.tag:
            raise ValueError("ParentNode must have a tag.")
        
        # 检查必需的 children
        if not self.children:
            raise ValueError("ParentNode must have at least one child.")
            
        # 生成开始标签（包含属性）
        html = f"<{self.tag}"
        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'
        html += ">"
        
        # 递归处理所有子节点
        for child in self.children:
            html += child.to_html()
            
        # 添加结束标签
        html += f"</{self.tag}>"
        
        return html

    def __eq__(self, other):
        return self.tag == other.tag and self.children == other.children and self.props == other.props

