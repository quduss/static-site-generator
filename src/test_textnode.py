import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node = TextNode("This is a text node with url", TextType.NORMAL, "https://x.com")
        node2 = TextNode("This is a text node with url", TextType.NORMAL, "https://x.com")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a link", TextType.LINK, 'https://google.com')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        node = TextNode("This is an italic text with url", TextType.ITALIC, 'https://google.com')
        node2 = TextNode("This is an italic text with no url", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        node = TextNode("This is bold text", TextType.BOLD)
        node2 = TextNode("This is normal text", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_convert_to_leaf_node(self):
        text_node = TextNode("A normal text", TextType.NORMAL)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(), "A normal text")
        text_node = TextNode("A bold text", TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(), "<b>A bold text</b>")
        text_node = TextNode("An image", TextType.IMAGE, "https://x.com")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(), '<img src="https://x.com" alt="An image">')
        text_node = TextNode("A Link to google", TextType.LINK, "https://google.com")
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(), '<a href="https://google.com">A Link to google</a>')


if __name__ == "__main__":
    unittest.main()