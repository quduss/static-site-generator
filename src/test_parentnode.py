import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild", {"class": "grand-child"})
        child_node = ParentNode("span", [grandchild_node], {"class": "child-node"})
        parent_node = ParentNode("div", [child_node], {"class": "parent-node"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="parent-node"><span class="child-node"><b class="grand-child">grandchild</b></span></div>',
        )



if __name__ == "__main__":
    unittest.main()