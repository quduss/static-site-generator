from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag")
        if self.children is None:
            raise ValueError("parent node must have children")
        else:
            container = []
            for child in self.children:
                container.append(child.to_html())
            concatenated = "".join(container)
            if self.props is None:
                prop_html = ""
            else:
                prop_html = self.props_to_html()
            return f"<{self.tag}{prop_html}>{concatenated}</{self.tag}>"
