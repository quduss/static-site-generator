from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value
        if self.props is None:
            prop_html = ""
        else:
            prop_html = self.props_to_html()
        return f"<{self.tag}{prop_html}>{self.value}</{self.tag}>"