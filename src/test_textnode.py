import unittest

from textnode import TextNode, TextType


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



if __name__ == "__main__":
    unittest.main()