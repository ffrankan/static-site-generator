from src.htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict=None):
        super().__init__(tag = tag, value = value, children = None, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if not self.tag:
            return self.value
        
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.props == other.props





                


