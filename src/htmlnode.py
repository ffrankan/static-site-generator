
class HTMLNode:
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def to_html(self):
           raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        # Sort the props by key
        sorted_props = sorted(self.props.items(), key=lambda x: x[0])
        return " ".join([f"{k}=\"{v}\"" for k, v in sorted_props])
    

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

